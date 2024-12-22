from config import BANNED_USERS
from pyrogram import filters
from pyrogram.types import InputMediaPhoto
from TheApi import api
from DONATE_ARMY_TG_MUSIC_PLAYER import app


@app.on_message(filters.command(["image"], prefixes=["/", "!", "."]) & ~BANNED_USERS)
async def image_from_bing(_, message):
    if len(message.command) < 2 and not message.reply_to_message:
        return await message.reply_text("**ɢɪᴠᴇ ɪᴍᴀɢᴇ ɴᴀᴍᴇ ғᴏʀ sᴇᴀʀᴄʜ 🔍**")

    if message.reply_to_message and message.reply_to_message.text:
        query = message.reply_to_message.text
    else:
        query = " ".join(message.command[1:])

    messagesend = await message.reply_text("**🔍 sᴇᴀʀᴄʜɪɴɢ ғᴏʀ ɪᴍᴀɢᴇs...**")

    media_group = []
    for url in await api.bing_image(query, 6):
        media_group.append(InputMediaPhoto(media=url))
    await messagesend.edit(f"**ᴜᴘʟᴏᴀᴅɪɴɢ...**")
    try:
        await app.send_media_group(message.chat.id, media_group)
        await messagesend.delete()
    except Exception as e:
        await messagesend.edit(e)
