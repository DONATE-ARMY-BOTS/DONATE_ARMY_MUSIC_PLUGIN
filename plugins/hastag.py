from DONATE_ARMY_TG_MUSIC_PLAYER import app
from pyrogram import filters
from TheApi import api


@app.on_message(filters.command("hastag"))
async def hastag(bot, message):

    try:
        text = message.text.split(" ", 1)[1]
        res = await api.gen_hashtag(text)
    except IndexError:
        return await message.reply_text("Example:\n\n/hastag python")

    await message.reply_text(f"ʜᴇʀᴇ ɪs ʏᴏᴜʀ  ʜᴀsᴛᴀɢ :\n<pre>{res}</pre>", quote=True)


__MODULE__ = "Hᴀsʜᴛᴀɢ"
__HELP__ = """
**ʜᴀsʜᴛᴀɢ ɢᴇɴᴇʀᴀᴛᴏʀ:**

• `/hashtag [text]`: Gᴇɴᴇʀᴀᴛᴇ ʜᴀsʜᴛᴀɢs ғᴏʀ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ.
"""
