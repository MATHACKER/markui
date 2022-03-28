# -- coding: utf-8 --
from email import message
from vkbottle import Bot, load_blueprints_from_package, API
import certifi



bot=Bot('d45b28d6c09cf9aae33cbf8e45cd34f755e3bbe80f310d8b7f65c1b5c5b9b45658446df40cb52e58741bb')
api=API('d45b28d6c09cf9aae33cbf8e45cd34f755e3bbe80f310d8b7f65c1b5c5b9b45658446df40cb52e58741bb')


for bp in load_blueprints_from_package('blueprints'):
    bp.load(bot)



bot.run_forever()