

import time

from pyKINGBOT import *
from pyKINGBOT.dB.core import *
from pyKINGBOT.functions import *
from pyKINGBOT.functions.all import *
from pyKINGBOT.functions.google_image import googleimagesdownload
from pyKINGBOT.functions.sudos import *
from pyKINGBOT.utils import *

start_time = time.time()
KINGBOT_version = "v0.0.1"
OWNER_NAME = KINGBOT_bot.me.first_name
OWNER_ID = KINGBOT_bot.me.id
DEVLIST = [
    "1259468938",
    "1452145387",
    "719195224",
    "1318486004",
    "1289422521",
    "1322549723",
    "611816596",
    "1003250439",
    "1152902819",
    "716243352",
    "1444249738",
    "559661211",
    "881536550",
    "954314021",
    "630654925",
]

# sudo
ok = udB.get("SUDOS")
if ok:
    SUDO_USERS = set(int(x) for x in ok.split())
else:
    SUDO_USERS = ""

if SUDO_USERS:
    sudos = list(SUDO_USERS)
else:
    sudos = ""

on = Var.SUDO

if Var.SUDO:
    sed = [KINGBOT_bot.uid, *sudos]
else:
    sed = [KINGBOT_bot.uid]


def grt(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


KANGING_STR = [
    "Using Witchery to kang this sticker...",
    "Plagiarising hehe...",
    "Inviting this sticker over to my pack...",
    "Kanging this sticker...",
    "Hey that's a nice sticker!\nMind if I kang?!..",
    "Hehe me stel ur stiker...",
    "Ay look over there (☉｡☉)!→\nWhile I kang this...",
    "Roses are red violets are blue, kanging this sticker so my pack looks cool",
    "Imprisoning this sticker...",
    "Mr.Steal-Your-Sticker is stealing this sticker... ",
]
