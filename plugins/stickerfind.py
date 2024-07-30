from pyrogram import filters

from DONATE_ARMY_MUSIC import app


@app.on_message(filters.command("st"))
def generate_sticker(client, message):
    if len(message.command) == 2:
        sticker_id = message.command[1]
        try:
            client.send_sticker(message.chat.id, sticker=sticker_id)
        except Exception as e:
            message.reply_text(f"Error: {e}")
    else:
        message.reply_text("Please provide a sticker ID after /st command.")


__MODULE__ = "Sᴛɪᴄᴋᴇʀ Fɪɴᴅ"
__HELP__ = """
**Sᴛɪᴄᴋᴇʀ Cᴏᴍᴍᴀɴᴅ**

Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀᴏᴡs ᴜsᴇʀs ᴛᴏ sᴇɴᴅ sᴛɪᴄᴋᴇʀs ʙʏ ᴘʀᴏᴠɪᴅɪɴɢ ᴀ sᴛɪᴄᴋᴇʀ ID.

Fᴇᴀᴛᴜʀᴇs:
- Rᴇᴘʏ ᴛᴏ ᴀ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ᴀ sᴛɪᴄᴋᴇʀ ID ᴛᴏ sᴇɴᴅ ᴛʜᴇ ᴄᴏʀʀᴇsᴘᴏɴᴅɪɴɢ sᴛɪᴄᴋᴇʀ.

Cᴏᴍᴍᴀɴᴅs:
- /sᴛ <sᴛɪᴄᴋᴇʀ_ɪᴅ>: Sᴇɴᴅ ᴀ sᴛɪᴄᴋᴇʀ ʙʏ ᴘʀᴏᴠɪᴅɪɴɢ ɪᴛs ID.

Exᴀᴍᴘᴇ:
- /sᴛ <sᴛɪᴄᴋᴇʀ_ɪᴅ>: Sᴇɴᴅs ᴛʜᴇ sᴛɪᴄᴋᴇʀ ᴄᴏʀʀᴇsᴘᴏɴᴅɪɴɢ ᴛᴏ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ID.

Nᴏᴛᴇ: Sᴛɪᴄᴋᴇʀ IDs ᴄᴀɴ ʙᴇ ᴏʙᴛᴀɪɴᴇᴅ ғʀᴏᴍ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋs ᴏʀ ɪɴᴅɪᴠɪᴅᴜᴀ sᴛɪᴄᴋᴇʀs.
"""
