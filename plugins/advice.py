from DONATE_ARMY_TG_MUSIC_PLAYER import app
from pyrogram import filters
from TheApi import api


@app.on_message(filters.command("advice"))
async def advice(_, message):
    A = await message.reply_text("...")
    res = await api.get_advice()
    await A.edit(res)


__MODULE__ = "Aᴅᴠɪᴄᴇ"
__HELP__ = """
/advice - Gᴇᴛ ʀᴀɴᴅᴏᴍ ᴀᴅᴠɪᴄᴇ"""
