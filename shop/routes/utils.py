import quart
import os
import requests
#import json
#
#from base.struct import Config
#
#cfg = None
#with open('config.json', 'r', encoding='utf-8') as f:
#    cfg = Config(json.loads(f.read()))
#    f.close()

app=quart.Quart("")
app.secret_key=os.urandom(24)

#app.secret_key=b"K\xa94j{\xb4J\xe4Q\xd4\xf5\x8em\xd1\x11,;*\xb7\x8b(\xd2#@"