import os
import shutil

from pyrogram import filters

from DONATE_ARMY_MUSIC import app
from DONATE_ARMY_MUSIC.misc import SUDOERS


@app.on_message(filters.command("clean") & SUDOERS)
async def clean(_, message):
    A = await message.reply_text("ᴄʟᴇᴀɴɪɴɢ ᴛᴇᴍᴘ ᴅɪʀᴇᴄᴛᴏʀɪᴇs...")
    dir = "downloads"
    dir1 = "cache"
    shutil.rmtree(dir)
    shutil.rmtree(dir1)
    os.mkdir(dir)
    os.mkdir(dir1)
    await A.edit("ᴛᴇᴍᴘ ᴅɪʀᴇᴄᴛᴏʀɪᴇs ᴀʀᴇ ᴄʟᴇᴀɴᴇᴅ")


__MODULE__ = "Cʟᴇᴀɴ"
__HELP__ = """
## Cᴇᴀɴ Cᴏᴍᴍᴀɴᴅ

### Cᴏᴍᴍᴀɴᴅ: /ᴄᴇᴀɴ
**Dᴇsᴄʀɪᴘᴛɪᴏɴ:**
Cᴇᴀɴs ᴜᴘ ᴛᴇᴍᴘᴏʀᴀʀʏ ᴅɪʀᴇᴄᴛᴏʀɪᴇs ᴛᴏ ғʀᴇᴇ ᴜᴘ sᴘᴀᴄᴇ.

**Usᴀɢᴇ:**
/ᴄᴇᴀɴ

**Dᴇᴛᴀɪs:**
- Dᴇᴇᴛᴇs ᴛʜᴇ 'ᴅᴏᴡɴᴏᴀᴅs' ᴀɴᴅ 'ᴄᴀᴄʜᴇ' ᴅɪʀᴇᴄᴛᴏʀɪᴇs ᴀɴᴅ ʀᴇᴄʀᴇᴀᴛᴇs ᴛʜᴇᴍ ᴛᴏ ᴇɴsᴜʀᴇ ᴛᴇᴍᴘᴏʀᴀʀʏ ғɪᴇs ᴀʀᴇ ʀᴇᴍᴏᴠᴇᴅ.
- Oɴʏ ᴀᴄᴄᴇssɪʙᴇ ᴛᴏ ᴜsᴇʀs ɪɴ ᴛʜᴇ SUDOERS ɪsᴛ.
"""
