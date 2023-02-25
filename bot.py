import json
import logging
import logging.handlers
import os
import sys

import aiohttp
import discord
import asyncio

from discord.ext import commands

from base.struct import Config

from shop.routes.utils import app
from quart import Quart
from shop.app_blueprint import app_blueprint

from quart import Quart, redirect, url_for, render_template, request, Blueprint, abort
from quart_discord import DiscordOAuth2Session, requires_authorization, Unauthorized

TEST_GUILD = discord.Object(id=943170102759686174)

cfg = None
with open('config.json', 'r', encoding='utf-8') as f:
    cfg = Config(json.loads(f.read()))
    #f.close()

basePath = '.'
path = os.path.abspath(os.path.join(basePath, '_temp'))
isExist = os.path.exists(path)
if not isExist:
    os.mkdir(path)

def log_handler() -> logging.Logger:
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.handlers.RotatingFileHandler(
        filename='log.log',
        encoding='utf-8',
        maxBytes=32 * 1024 * 1024,  # 32 MiB
        backupCount=5,  # Rotaciona em 5 arquivos
    )
    dt_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(
        '[{asctime}] [{levelname}] {name}: {message}', dt_fmt, style='{')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


log = log_handler()

app = Quart(__name__)

app.config["DISCORD_CLIENT_ID"] = str(cfg.client_id)
app.config["DISCORD_CLIENT_SECRET"] = str(cfg.client_secret)
app.config["DISCORD_REDIRECT_URI"] = str(cfg.red_uri)
app.config["DISCORD_BOT_TOKEN"] = str(cfg.prefix)

app.register_blueprint(app_blueprint, url_prefix='/shop')

discord_ = DiscordOAuth2Session(app)

@app.route("/login/")
async def login():
    return await discord_.create_session(scope=["identify", "guilds"])

@app.route("/logout/")
async def logout():
    discord_.revoke()
    return redirect(url_for("shop.index"))

@app.route("/me/")
@requires_authorization
async def me():
  user = await discord_.fetch_user()
  return redirect(url_for("shop.index"))
  

@app.route("/callback/")
async def callback():
    await discord_.callback()
    try:
        return redirect(bot.url)
    except:
        return redirect(url_for(".me"))

@app.errorhandler(Unauthorized)
async def redirect_unauthorized(e):
    bot.url = request.url
    return redirect(url_for("shop.login"))

log.warning(app.url_map)

class SpinovelBot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.all()
        atividade = discord.Activity(type=discord.ActivityType.watching,
                                     name="Kiniga")
        super().__init__(
            intents=intents,
            command_prefix=commands.when_mentioned_or(cfg.prefix),
            description='Kiniga Brasil',
            activity=atividade
        )

        print('Excluindo arquivos temporários...')
        for filename in os.listdir('./_temp'):
            if filename.endswith(".png") or filename.endswith(".jpg"):
                print('Removendo %s ' % (filename, ))
                os.remove('./_temp/%s' % (filename, ))
                print('%s removido.' % (filename, ))

    async def load_cogs(self) -> None:
        for filename in os.listdir('base/cmds'):
            if filename.endswith('.py'):
                try:
                    await self.load_extension(f'base.cmds.{filename[ :-3 ]}')
                    print(f'Cog "{filename}" carregada.')
                except Exception as e:
                    print(
                        f'Ocorreu um erro enquanto a cog "{filename}" carregava.\n{e}')
                    log.error(e)
                    raise e

    async def setup_hook(self) -> None:
        print(
            f'Logado como {self.user} (ID: {self.user.id}) usando discord.py {discord.__version__}')
        print('------')
        await self.load_cogs()
        sys.stdout.flush()
        try:
            self.loop.create_task(
                app.run_task(
                    host = '0.0.0.0', 
                    debug = True 
                )
            )
        except Exception as e:
            log.error(e)
        # self.tree.copy_global_to(guild=TEST_GUILD)
        # await self.tree.sync(guild=TEST_GUILD)

    async def close(self) -> None:
        log.warning("desligando o bot...")
        await super().close()
        await self.session.close()


async def main() -> None:
    bot = SpinovelBot()
    async with aiohttp.ClientSession() as session, bot:
        bot.session = session
        await bot.start(cfg.bot_token)


async def warn() -> None:
    return log.warning("bot foi desligado usando ctrl+c no terminal!")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        asyncio.run(warn())