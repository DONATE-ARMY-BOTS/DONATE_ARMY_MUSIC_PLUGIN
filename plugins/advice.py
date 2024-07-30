from pyrogram import filters


from DONATE_ARMY_MUSIC import api, app


async def get_advice():
    b = await api.advice()
    c = b["advice"]
    return c


@app.on_message(filters.command("advice"))
async def clean(_, message):
    A = await message.reply_text("...")
    B = await get_advice()
    await A.edit(B)


__MODULE__ = "Aᴅᴠɪᴄᴇ"
__HELP__ = """
## Aᴅᴠɪᴄᴇ Cᴏᴍᴍᴀɴᴅ

### Cᴏᴍᴍᴀɴᴅ: /ᴀᴅᴠɪᴄᴇ
**Dᴇsᴄʀɪᴘᴛɪᴏɴ:**
Fᴇᴛᴄʜᴇs ᴀ ʀᴀɴᴅᴏᴍ ᴘɪᴇᴄᴇ ᴏғ ᴀᴅᴠɪᴄᴇ ғʀᴏᴍ ᴀɴ API ᴀɴᴅ ᴅɪsᴘᴀʏs ɪᴛ.
**Usᴀɢᴇ:**
/ᴀᴅᴠɪᴄᴇ

**Dᴇᴛᴀɪs:**
- Sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴘɪᴇᴄᴇ ᴏғ ᴀᴅᴠɪᴄᴇ ᴀs ᴀ ᴍᴇssᴀɢᴇ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.

**Exᴀᴍᴘᴇs:**
- /ᴀᴅᴠɪᴄᴇ: Rᴇᴛʀɪᴇᴠᴇs ᴀɴᴅ ᴅɪsᴘᴀʏs ᴀᴅᴠɪᴄᴇ.

**Nᴏᴛᴇs:**
- Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ᴜsᴇʀ ᴛᴏ ɢᴇᴛ ᴀ ʀᴀɴᴅᴏᴍ ᴀᴅᴠɪᴄᴇ.
"""
