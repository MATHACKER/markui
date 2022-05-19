# -- coding: utf-8 --
from cgitb import text
from vkbottle.bot import Blueprint, Message
from vkbottle import GroupEventType, VKAPIError, API, PhotoMessageUploader, Bot, User, Keyboard, Callback, KeyboardButtonColor, Text, OpenLink, Location, EMPTY_KEYBOARD, CtxStorage, BaseStateGroup
from vkbottle_types import GroupTypes
from vkbottle.modules import json
import certifi
import asyncio
import json
import textwrap
import time
import asyncio
import random
import requests

bp = Blueprint('Создание базы')
bp.on.vbml_ignore_case = True

bot=Bot('d45b28d6c09cf9aae33cbf8e45cd34f755e3bbe80f310d8b7f65c1b5c5b9b45658446df40cb52e58741bb')
api=API('d45b28d6c09cf9aae33cbf8e45cd34f755e3bbe80f310d8b7f65c1b5c5b9b45658446df40cb52e58741bb')


res = requests.post('http://gdvkbot.pythonanywhere.com/')

print(res)




def write(data, filename):
	data = json.dumps(data)
	data = json.loads(str(data))
	with open(filename, 'w', encoding = 'utf-8') as file:
		json.dump(data, file, indent = 4, ensure_ascii=False)

baza = {}

def read(filename):
	with open(filename, 'r', encoding='utf-8') as file:
		return json.load(file)

bazadan_new = read('baza.json')



@bp.on.chat_message()
async def invite(message:Message):
    bazadan_new = read('baza.json')
    if message.text!='' and message.text.lower() not in bazadan_new:
        #await message.answer(str(message))
        #await message.answer(str(message.reply_message.text))
        #await message.answer(str(message.text))
        #
        keys=str(message.reply_message.text).lower()
        try:
            value=bazadan_new[message.reply_message.text.lower()]
            #time.sleep(1)
            #await message.answer(str(value))
            value.append(message.text.lower())
            #time.sleep(1)
            #await message.answer(str(value))
        except KeyError:
            value=[message.text.lower()]
        #await message.answer(str(value))
        #await message.answer(message.text.lower())
        baza[keys] = value
        #time.sleep(1)
        #await message.answer(str(baza))
        #######
        #time.sleep(1)
        ########## проблема тут
        ##############
        #############
        global baza_new
        baza_new = read('baza.json')
        baza_js_new = {**baza_new, **baza}
        #await message.answer(str(baza_js_new[message.reply_message.text]))
        ###############
        ########
        ##########
        write(baza_js_new, 'baza.json')
        #await message.answer(str(value))


        bazadan_new = read('baza.json')
        #time.sleep(1)
        #await message.answer(str(value))
        #await message.answer(str(bazadan_new[message.reply_message.text.lower()]))
        #await message.answer(bazadan_new[message.reply_message.text.lower()][0])
        res = requests.post(url='http://gdvkbot.pythonanywhere.com/', json=bazadan_new)

        print(res)
    #if message.text.lower() in bazadan_new and message.text!='':
        #znachenie = read('baza.json')
        #len = int(znachenie[message.text.lower()].len())
        #dlina = int(len(znachenie[message.text.lower()]))
        #await asyncio.sleep(0.1)
        #await message.answer(bazadan_new[message.text.lower()][random.randint(0, (dlina-1))])

bazadan_new = read('baza.json')
bazadan_new = read('baza.json')
