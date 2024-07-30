from io import BytesIO

import aiohttp
from pyrogram import filters

from DONATE_ARMY_MUSIC import app


async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@app.on_message(filters.command("carbon"))
async def _carbon(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("**ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴀ ᴄᴀʀʙᴏɴ.**")
        return
    if not (replied.text or replied.caption):
        return await message.reply_text("**ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴀ ᴄᴀʀʙᴏɴ.**")
    text = await message.reply("Processing...")
    carbon = await make_carbon(replied.text or replied.caption)
    await text.edit("**ᴜᴘʟᴏᴀᴅɪɴɢ...**")
    await message.reply_photo(carbon)
    await text.delete()
    carbon.close()


__MODULE__ = "Cᴀʀʙᴏɴ"
__HELP__ = """
**Cᴀʀʙᴏɴ Cᴏᴍᴍᴀɴᴅ**

Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀᴏᴡs ᴜsᴇʀs ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ Cᴀʀʙᴏɴ ɪᴍᴀɢᴇ ғʀᴏᴍ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ. Cᴀʀʙᴏɴ ɪs ᴀ ᴛᴏᴏ ғᴏʀ ᴄʀᴇᴀᴛɪɴɢ ʙᴇᴀᴜᴛɪғᴜ ɪᴍᴀɢᴇs ᴏғ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.

Fᴇᴀᴛᴜʀᴇs:
- Rᴇᴘʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴀ Cᴀʀʙᴏɴ ɪᴍᴀɢᴇ ғʀᴏᴍ ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴄᴏɴᴛᴇɴᴛ.
- Sᴜᴘᴘᴏʀᴛs ʙᴏᴛʜ ᴘᴀɪɴ ᴛᴇxᴛ ᴀɴᴅ ᴄᴀᴘᴛɪᴏɴᴇᴅ ᴍᴇssᴀɢᴇs.
- Dɪsᴘᴀʏs ᴀ ᴘʀᴏᴄᴇssɪɴɢ ᴍᴇssᴀɢᴇ ᴡʜɪᴇ ɢᴇɴᴇʀᴀᴛɪɴɢ ᴛʜᴇ Cᴀʀʙᴏɴ ɪᴍᴀɢᴇ.
- Uᴘᴏᴀᴅs ᴛʜᴇ ɢᴇɴᴇʀᴀᴛᴇᴅ Cᴀʀʙᴏɴ ɪᴍᴀɢᴇ ᴀs ᴀ ʀᴇᴘʏ ᴛᴏ ᴛʜᴇ ᴏʀɪɢɪɴᴀ ᴍᴇssᴀɢᴇ.

Cᴏᴍᴍᴀɴᴅs:
- /ᴄᴀʀʙᴏɴ: Rᴇᴘʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴀ Cᴀʀʙᴏɴ ɪᴍᴀɢᴇ ғʀᴏᴍ ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴄᴏɴᴛᴇɴᴛ.

Nᴏᴛᴇ: Mᴀᴋᴇ sᴜʀᴇ ᴛᴏ ʀᴇᴘʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴛʜᴇ Cᴀʀʙᴏɴ ɪᴍᴀɢᴇ sᴜᴄᴄᴇssғᴜʏ.
"""
