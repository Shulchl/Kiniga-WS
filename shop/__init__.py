import os

from quart import Quart
from quart_discord import DiscordOAuth2Session


def get_app():
    app = Quart(__name__)

    app.secret_key = b"%\xe0'\x01\xdeH\x8e\x85m|\xb3\xffCN\xc9g"
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"  # !! Only in development environment.

    app.config["DISCORD_CLIENT_ID"] = str(cfg.client_id)
    app.config["DISCORD_CLIENT_SECRET"] = str(cfg.client_secret)
    app.config["DISCORD_REDIRECT_URI"] = str(cfg.red_uri)
    app.config["DISCORD_BOT_TOKEN"] = str(cfg.prefix)

    app.discord = DiscordOAuth2Session(app, client_id=490732332240863233)

    return app