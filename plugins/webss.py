from pyrogram import filters
from pyrogram.types import Message

from DONATE_ARMY_MUSIC import app
from DONATE_ARMY_MUSIC.utils.errors import capture_err


@app.on_message(
    filters.command("webss", prefixes=["/", "!", "%", ",", "", ".", "@", "#"])
)
@capture_err
async def take_ss(_, message: Message):
    try:
        if len(message.command) != 2:
            return await message.reply_text("**» ɢɪᴠᴇ ᴀ ᴜʀʟ ᴛᴏ ғᴇᴛᴄʜ sᴄʀᴇᴇɴsʜᴏᴛ...**")
        url = message.text.split(None, 1)[1]
        m = await message.reply_text("**» ᴛʀʏɪɴɢ ᴛᴏ ᴛᴀᴋᴇ sᴄʀᴇᴇɴsʜᴏᴛ...**")
        await m.edit("**» ᴜᴩʟᴏᴀᴅɪɴɢ ᴄᴀᴩᴛᴜʀᴇᴅ sᴄʀᴇᴇɴsʜᴏᴛ...**")
        try:
            await message.reply_photo(
                photo=f"https://webshot.amanoteam.com/print?q={url}",
                quote=False,
            )
        except TypeError:
            return await m.edit("**» ɴᴏ sᴜᴄʜ ᴡᴇʙsɪᴛᴇ.**")
        await m.delete()
    except Exception as e:
        await message.reply_text(str(e))


__MODULE__ = "Wᴇʙ Ss"
__HELP__ = """
**Wᴇʙ Sᴄʀᴇᴇɴsʜᴏᴛ**

Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀᴏᴡs ᴜsᴇʀs ᴛᴏ ᴛᴀᴋᴇ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴏғ ᴀ ᴡᴇʙᴘᴀɢᴇ ᴀɴᴅ sᴇɴᴅ ɪᴛ ᴀs ᴀ ᴘʜᴏᴛᴏ.

Fᴇᴀᴛᴜʀᴇs:
- Rᴇᴘʏ ᴛᴏ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ᴀ URL ᴛᴏ ᴛᴀᴋᴇ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴏғ ᴛʜᴀᴛ ᴡᴇʙᴘᴀɢᴇ ᴀɴᴅ sᴇɴᴅ ɪᴛ ᴀs ᴀ ᴘʜᴏᴛᴏ.

Cᴏᴍᴍᴀɴᴅs:
- /ᴡᴇʙss <ᴜʀ>: Tᴀᴋᴇ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴏғ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ URL ᴀɴᴅ sᴇɴᴅ ɪᴛ ᴀs ᴀ ᴘʜᴏᴛᴏ.

Exᴀᴍᴘᴇ:
- /ᴡᴇʙss <ᴜʀ>: Tᴀᴋᴇs ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴏғ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ URL ᴀɴᴅ sᴇɴᴅs ɪᴛ ᴀs ᴀ ᴘʜᴏᴛᴏ.

Nᴏᴛᴇ: Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴜsᴇs ᴀɴ ᴇxᴛᴇʀɴᴀ sᴇʀᴠɪᴄᴇ ᴛᴏ ᴛᴀᴋᴇ sᴄʀᴇᴇɴsʜᴏᴛs ᴏғ ᴡᴇʙᴘᴀɢᴇs.
"""
