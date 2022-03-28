# -- coding: utf-8 --
from cgitb import text
from email import message
from vkbottle.bot import Blueprint, Message
from vkbottle import GroupEventType, VKAPIError, API, PhotoMessageUploader, Bot, Keyboard, Callback, KeyboardButtonColor, Text, OpenLink, Location, EMPTY_KEYBOARD, CtxStorage, BaseStateGroup
from vkbottle_types import GroupTypes
from vkbottle.modules import json
import certifi
import asyncio

bp = Blueprint('Добавление бота')
bp.on.vbml_ignore_case = True

bot=Bot('d45b28d6c09cf9aae33cbf8e45cd34f755e3bbe80f310d8b7f65c1b5c5b9b45658446df40cb52e58741bb')
api=API('d45b28d6c09cf9aae33cbf8e45cd34f755e3bbe80f310d8b7f65c1b5c5b9b45658446df40cb52e58741bb')





@bp.on.chat_message(action=["chat_invite_user", "chat_invait_user_by_link"])
async def invite(message:Message):
    if message.action.member_id == -212164379:
        await message.answer('💬 Привет, меня зовут Mark! 💎 Я работаю на нейронной сети INFINITY, разработанной @darksnaper . 🧩 Я, как и любая нейросеть, развиваюсь со временем, просто общайтесь и вы поможете мне стать лучше. ❗ Для того, чтобы я работал, мне нужно выдать админа в беседе.')

