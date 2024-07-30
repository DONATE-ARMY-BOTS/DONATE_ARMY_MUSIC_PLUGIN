from pyrogram import filters
from pyrogram.types import InputMediaPhoto
from requests import get

from DONATE_ARMY_MUSIC import app


@app.on_message(
    filters.command(["image"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])
)
async def pinterest(_, message):
    chat_id = message.chat.id

    try:
        query = message.text.split(None, 1)[1]
    except:
        return await message.reply("**ɢɪᴠᴇ ɪᴍᴀɢᴇ ɴᴀᴍᴇ ғᴏʀ sᴇᴀʀᴄʜ 🔍**")

    images = get(f"https://pinterest-api-one.vercel.app/?q={query}").json()

    media_group = []
    count = 0

    msg = await message.reply(f"sᴄʀᴀᴘɪɴɢ ɪᴍᴀɢᴇs ғʀᴏᴍ ᴘɪɴᴛᴇʀᴇᴛs...")
    for url in images["images"][:6]:

        media_group.append(InputMediaPhoto(media=url))
        count += 1
        await msg.edit(f"=> ᴏᴡᴏ sᴄʀᴀᴘᴇᴅ ɪᴍᴀɢᴇs {count}")

    try:

        await app.send_media_group(
            chat_id=chat_id, media=media_group, reply_to_message_id=message.id
        )
        return await msg.delete()

    except Exception as e:
        await msg.delete()
        return await message.reply(f"ᴇʀʀᴏʀ : {e}")


__MODULE__ = "Iᴍᴀɢᴇ Sᴇᴀʀᴄʜ"
__HELP__ = """
**Pɪɴᴛᴇʀᴇsᴛ Iᴍᴀɢᴇ Sᴇᴀʀᴄʜ**

Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀᴏᴡs ᴜsᴇʀs ᴛᴏ sᴇᴀʀᴄʜ ғᴏʀ ɪᴍᴀɢᴇs ᴏɴ Pɪɴᴛᴇʀᴇsᴛ ᴀɴᴅ sᴇɴᴅs ᴀ ᴄᴏᴇᴄᴛɪᴏɴ ᴏғ ᴜᴘ ᴛᴏ 6 ɪᴍᴀɢᴇs.

Fᴇᴀᴛᴜʀᴇs:
- Rᴇᴘʏ ᴛᴏ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ᴀ ǫᴜᴇʀʏ ᴛᴏ sᴇᴀʀᴄʜ ғᴏʀ ɪᴍᴀɢᴇs ʀᴇᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ ǫᴜᴇʀʏ ᴏɴ Pɪɴᴛᴇʀᴇsᴛ.
- Sᴇɴᴅs ᴜᴘ ᴛᴏ 6 ɪᴍᴀɢᴇs ғᴏᴜɴᴅ ᴏɴ Pɪɴᴛᴇʀᴇsᴛ ʀᴇᴀᴛᴇᴅ ᴛᴏ ᴛʜᴇ ǫᴜᴇʀʏ.

Cᴏᴍᴍᴀɴᴅs:
- /ɪᴍᴀɢᴇ <ǫᴜᴇʀʏ>: Sᴇᴀʀᴄʜ ғᴏʀ ɪᴍᴀɢᴇs ʀᴇᴀᴛᴇᴅ ᴛᴏ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ǫᴜᴇʀʏ ᴏɴ Pɪɴᴛᴇʀᴇsᴛ.

Exᴀᴍᴘᴇ:
- /ɪᴍᴀɢᴇ <ǫᴜᴇʀʏ>: Sᴇᴀʀᴄʜᴇs ғᴏʀ ɪᴍᴀɢᴇs ʀᴇᴀᴛᴇᴅ ᴛᴏ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ǫᴜᴇʀʏ ᴏɴ Pɪɴᴛᴇʀᴇsᴛ ᴀɴᴅ sᴇɴᴅs ᴜᴘ ᴛᴏ 6 ɪᴍᴀɢᴇs.

Nᴏᴛᴇ: Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴜsᴇs ᴀɴ ᴇxᴛᴇʀɴᴀ Pɪɴᴛᴇʀᴇsᴛ API ᴛᴏ ғᴇᴛᴄʜ ɪᴍᴀɢᴇs.
"""
