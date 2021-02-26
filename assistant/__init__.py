#CREDITS KINGBOT
from pyKINGBOT import *
from pyKINGBOT.dB.database import Var
from telethon import Button, custom

OWNER_NAME = KINGBOT_bot.me.first_name
OWNER_ID = KINGBOT_bot.me.id


async def setit(event, name, value):
    try:
        udB.set(name, value)
    except BaseException:
        return await event.edit("`Something W3nt Wrong!!`")
