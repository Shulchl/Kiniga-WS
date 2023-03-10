from __future__ import annotations


class Config:
    def __init__(self, cfg: dict) -> None:
        # COISAS DA DATABASE 
        self.dbName = cfg['db_Name']
        self.postgresql_user = cfg['postgresql_user']
        self.postgresql_password = cfg['postgresql_password']
        self.postgresql_host = cfg['postgresql_host']
        
        # COISAS DO EMAIL DO BOT
        self.bot_mail = cfg['bot_mail']
        self.bot_mailpass = cfg['bot_mailpass']
        self.bot_mailhost = cfg['bot_mailhost']
        
        # COISAS DO TRELLO
        self.trelloList = cfg['tidList']
        self.trelloKey = cfg['tkey']
        self.trelloToken = cfg['ttoken']
        
        # COISAS DO DISCORD
        self.bot_token = cfg['bot_token']
        self.client_id = cfg['client_id']
        self.client_secret = cfg['client_secret']
        self.red_uri = cfg['red_uri']
        
        self.min_message_xp = cfg['min_message_xp']
        self.max_message_xp = cfg['max_message_xp']
        self.coinsmin = cfg['coinsmin']
        self.coinsmax = cfg['coinsmax']
        self.lucky = cfg['lucky']
        self.prefix = cfg['prefix']
        self.bdayloop = cfg['bdayloop']
        self.guild = cfg['guild']
        self.chat_cmds = cfg['chat_cmds']
        self.coin_max = cfg['coin_max']
        self.setup = cfg['setup'] 
        
        self.ranks = cfg['ranks']  # NOMES DE CARGOS DE RANK
        self.colors = cfg['colors'] # CORES DE CARGOS DE RANK
        self.trash = cfg['trash'] # NOME DE ITENS LIXO

        self.eqp_role = cfg['eqp_role'] # CARGO DE EQUIPE
        self.mark_role = cfg['mark_role'] # CARGO SEPARADOR
        self.aut_role = cfg['aut_role'] # CARGO DE AUTOR
        self.creat_role = cfg['creat_role'] # CARGO DE CRIADOR
        
        self.chat_creators = cfg['chat_creators'] # CANAL EXCLUSIVO DE AUTORES
        self.chat_release = cfg['chat_release'] # CANAL EM QUE SERÃO ENVIADOS OS CAPÍTULOS RECENTES

        self.publish_c = cfg['publish_channel'] # CANAL EM QUE SERÁ ENVIADO OS PROJETOS ACEITOS 
        self.refuse_c = cfg['refuse_channel'] # CANAL EM QUE SERÁ ENVIADO OS PROJETOS RECUSADOS
        self.trello_l_c = cfg['trello_log_channel'] # CANAL EM QUE SERÁ ENVIADO O LOG DO TRELLO 

        # COISAS DO SITE

        self.web_session = cfg['web_session']
    