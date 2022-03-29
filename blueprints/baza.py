# -- coding: utf-8 --
from cgitb import text
from email import message
from vkbottle.bot import Blueprint, Message
from vkbottle import GroupEventType, VKAPIError, API, PhotoMessageUploader, Bot, Keyboard, Callback, KeyboardButtonColor, Text, OpenLink, Location, EMPTY_KEYBOARD, CtxStorage, BaseStateGroup
from vkbottle_types import GroupTypes
from vkbottle.modules import json
import certifi
import asyncio
import json
import textwrap
import time
import asyncio

bp = Blueprint('Создание базы')
bp.on.vbml_ignore_case = True

bot=Bot('d45b28d6c09cf9aae33cbf8e45cd34f755e3bbe80f310d8b7f65c1b5c5b9b45658446df40cb52e58741bb')
api=API('d45b28d6c09cf9aae33cbf8e45cd34f755e3bbe80f310d8b7f65c1b5c5b9b45658446df40cb52e58741bb')



def write(data, filename):
	data = json.dumps(data)
	data = json.loads(str(data))
	with open(filename, 'w', encoding = 'utf-8') as file:
		json.dump(data, file, indent = 4, ensure_ascii=False)

baza = {}

def read(filename):
	with open(filename, 'r', encoding='utf-8') as file:
		return json.load(file)

bazadann_new = read('baza.json')



@bp.on.chat_message()
async def invite(message:Message):
    bazadann_new = read('baza.json')
    if message.text!='' and message.text.lower() not in bazadann_new:
        #await message.answer(str(message))
        #await message.answer(str(message.reply_message.text))
        #await message.answer(str(message.text))
        keys=str(message.reply_message.text).lower()
        value=str(message.text).lower()
        baza[keys] = value
        global baza_new
        baza_new = read('baza.json')
        baza_js_new = {**baza, **baza_new}
        write(baza_js_new, 'baza.json')
        global bazadan_new
        bazadan_new = read('baza.json')
    elif message.text.lower() in bazadan_new and message.text!='':
        await message.answer(bazadan_new[message.text.lower()])

bazadan_new = read('baza.json')
