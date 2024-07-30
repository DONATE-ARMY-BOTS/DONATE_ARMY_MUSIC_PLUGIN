from pyrogram import filters
from pyrogram.types import Message

from DONATE_ARMY_MUSIC import app


@app.on_message(filters.command(["dice", "ludo"]))
async def dice(c, m: Message):
    dicen = await c.send_dice(m.chat.id, reply_to_message_id=m.id)
    await dicen.reply_text("results is {0}".format(dicen.dice.value))


__MODULE__ = "Fᴜɴ"
__HELP__ = """
## Fᴜɴ Cᴏᴍᴍᴀɴᴅs Hᴇᴘ

### 1. /ᴅɪᴄᴇ ᴏʀ /ᴜᴅᴏ
**Dᴇsᴄʀɪᴘᴛɪᴏɴ:**
Rᴏs ᴀ ᴠɪʀᴛᴜᴀ ᴅɪᴄᴇ ᴏʀ ᴘᴀʏs ᴀ ɢᴀᴍᴇ ᴏғ Lᴜᴅᴏ.

**Usᴀɢᴇ:**
/ᴅɪᴄᴇ ᴏʀ /ᴜᴅᴏ

**Dᴇᴛᴀɪs:**
- Iɴɪᴛɪᴀᴛᴇs ᴀ ᴅɪᴄᴇ ʀᴏ ᴏʀ ᴀ ɢᴀᴍᴇ ᴏғ Lᴜᴅᴏ.
- Sᴇɴᴅs ᴛʜᴇ ʀᴇsᴜᴛ ᴏғ ᴛʜᴇ ᴅɪᴄᴇ ʀᴏ.
- Fᴏʀ Lᴜᴅᴏ, ᴛʜᴇ ɢᴀᴍᴇ ɪs ᴘᴀʏᴇᴅ ᴅɪʀᴇᴄᴛʏ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.

**Exᴀᴍᴘᴇs:**
- `/ᴅɪᴄᴇ`
- `/ᴜᴅᴏ`

"""
