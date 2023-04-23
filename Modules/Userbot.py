
import os
import sys
import asyncio
import datetime
import time
from config import bot
from config import (HNDLR, SUDO_USERS, ALIVE_PIC, ALIVE_MSG, PING_MSG, __version__, start_time)
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import __version__ as pyro_vr             
                

pongg = PING_MSG if PING_MSG else "👑 𝗕𝗥𝗔𝗡𝗗𝗘𝗗 𝗕𝗢𝗧 𝗜𝗦 𝗢𝗡 𝗙𝗜𝗥𝗘 👑"
KAAL_PIC = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/5ef86d039b64df539acc2.jpg"
Alivemsg = ALIVE_MSG if ALIVE_MSG else "❤️🚩𝗝𝗔𝗜 𝗦𝗛𝗥𝗘𝗘 𝗥𝗔𝗠 𝗛𝗔𝗥 𝗛𝗔𝗥 𝗠𝗔𝗛𝗔𝗗𝗘𝗩 🚩❤️
👑 𝗕𝗥𝗔𝗡𝗗𝗘𝗗 𝗜𝗦 𝗢𝗡𝗟𝗜𝗡𝗘 𝗡𝗢𝗪 👑."


manjeet = f"⁂ {Alivemsg} ⁂\n\n"
manjeet += f"━───────╯•╰───────━\n"
manjeet += f"➠ **Python version** : `3.10.4`\n"
manjeet += f"➠ **Pyrogram version** : `{pyro_vr}`\n"
manjeet += f"➠ **version**  : `{__version__}`\n"
manjeet += f"➠ **Kali Linux**  : `Yes`\n"
manjeet += f"➠ **Database**  : `Mongo atlas`\n"
manjeet += f"➠ **Database Status **  : `Functional`\n"
manjeet += f"➠ **current Branch**  : `Master`\n"
manjeet += f"➠ **VC Modulesc**  : `Allow`\n"
manjeet += f"➠ **Channel** : [𝗦𝗨𝗣𝗣𝗢𝗥𝗧 𝗖𝗛𝗔𝗡𝗡𝗘𝗟l](https://t.me/BRANDED_LINK)\n"
manjeet += f"➠ **Group** : [𝗢𝗪𝗡𝗘𝗥](https://t.me/BRANDRD_21)\n"
manjeet += f"━───────╮•╭───────━\n\n"
manjeet += f"➠ **Channel** : [𝗙𝗥𝗘𝗘 𝗖𝗖](https://t.me/BRANDED_FREE_CC)\n"
manjeet += f"➠ **Source Code:** [•𝗥𝗘𝗣𝗢•](https://te.legra.ph/file/b5a457725d59cc7765dde.jpg)"


async def get_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    hmm = len(time_list)
    for x in range(hmm):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "
    time_list.reverse()
    up_time += ":".join(time_list)
    return up_time



@Client.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["ping"], prefixes=HNDLR))
async def ping(_, e: Message):       
      start = datetime.datetime.now()
      uptime = await get_time((time.time() - start_time))
      Fuk = await e.reply("**Pong !!**")
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await Fuk.edit_text(f"😍 {pongg} 😎 \n\n ❤ ᴘɪɴɢ: `{ms}` ᴍs \n 🌹 ᴜᴘᴛɪᴍᴇ: `{uptime}` \n 🤞 ᴠᴇʀsɪᴏɴ: `{__version__}`")




@Client.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["alive"], prefixes=HNDLR))
async def alive(xspam: Client, e: Message):
       if ".jpg" in KAAL_PIC or ".png" in KAAL_PIC:
              await xspam.send_photo(e.chat.id, KAAL_PIC, caption=manjeet)
       if ".mp4" in KAAL_PIC or ".MP4," in KAAL_PIC:
              await xspam.send_video(e.chat.id, KAAL_PIC, caption=manjeet)






@Client.on_message(filters.user(SUDO_USERS) & filters.command(["restart", "reboot"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["restart", "reboot"], prefixes=HNDLR))
async def restart_bot(_, message: Message):
    msg = await message.reply("`restarting bot...`")
    args = [sys.executable, "main.py"]
    await msg.edit("😊 bot restarted\n\n• now you can use this bot again.")
    execle(sys.executable, *args, environ)
    return
            
