from pyrogram import filters

from DONATE_ARMY_MUSIC import app


@app.on_message(filters.command(["qr"]))
async def write_text(client, message):
    if len(message.command) < 2:
        await message.reply_text("**Usage**:- `/qr https://t.me/DONATE_ARMY_BOTS`")
        return
    text = " ".join(message.command[1:])
    photo_url = "https://apis.xditya.me/qr/gen?text=" + text
    await app.send_photo(
        chat_id=message.chat.id, photo=photo_url, caption="Here is your qrcode"
    )


__MODULE__ = "Qʀɢᴇɴ"

__HELP__ = """
Ƭʜɪs ᴍᴏᴅᴜʟᴇ ɢᴇɴᴇʀᴀᴛᴇs Qʀ ᴄᴏᴅᴇs. Usᴇ ᴛʜᴇ /qr ᴄᴏᴍᴍᴀɴᴅ ғᴏʟʟᴏᴡᴇᴅ ʙʏ ᴛʜᴇ ᴛᴇxᴛ ᴏʀ URL ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴇɴᴄᴏᴅᴇ ɪɴᴛᴏ ᴀ Qʀ ᴄᴏᴅᴇ. Fᴏʀ ᴇxᴀᴍᴘʟᴇ, `/qr https://t.me/DONATE_ARMY_BOTS`. Tʜᴇ ʙᴏᴛ ᴡɪʟʟ ᴛʜᴇɴ ɢᴇɴᴇʀᴀᴛᴇ ᴀ Qʀ ᴄᴏᴅᴇ ғᴏʀ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ɪɴᴘᴜᴛ. Mᴀᴋᴇ sᴜʀᴇ ᴛᴏ ɪɴᴄʟᴜᴅᴇ ᴛʜᴇ ᴘʀᴏᴛᴏᴄᴏʟ (http:// ᴏʀ https://) ғᴏʀ URLs. Eɴᴊᴏʏ ᴄʀᴇᴀᴛɪɴɢ Qʀ ᴄᴏᴅᴇs ᴡɪᴛʜ ᴇᴀsᴇ!
"""
