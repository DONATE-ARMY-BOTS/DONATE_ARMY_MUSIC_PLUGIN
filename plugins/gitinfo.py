import aiohttp
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from DONATE_ARMY_MUSIC import app


@app.on_message(filters.command(["github", "git"]))
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("/git DONATE-ARMY-BOTS")
        return

    username = message.text.split(None, 1)[1]
    URL = f"https://api.github.com/users/{username}"

    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()

            try:
                url = result["html_url"]
                name = result["name"]
                company = result["company"]
                bio = result["bio"]
                created_at = result["created_at"]
                avatar_url = result["avatar_url"]
                blog = result["blog"]
                location = result["location"]
                repositories = result["public_repos"]
                followers = result["followers"]
                following = result["following"]

                caption = f"""ɢɪᴛʜᴜʙ ɪɴғᴏ ᴏғ {name}
                
ᴜsᴇʀɴᴀᴍᴇ: {username}
ʙɪᴏ: {bio}
ʟɪɴᴋ: [Here]({url})
ᴄᴏᴍᴩᴀɴʏ: {company}
ᴄʀᴇᴀᴛᴇᴅ ᴏɴ: {created_at}
ʀᴇᴩᴏsɪᴛᴏʀɪᴇs: {repositories}
ʙʟᴏɢ: {blog}
ʟᴏᴄᴀᴛɪᴏɴ: {location}
ғᴏʟʟᴏᴡᴇʀs: {followers}
ғᴏʟʟᴏᴡɪɴɢ: {following}"""

            except Exception as e:
                print(str(e))

    # Create an inline keyboard with a close button
    close_button = InlineKeyboardButton("Close", callback_data="close")
    inline_keyboard = InlineKeyboardMarkup([[close_button]])

    # Send the message with the inline keyboard
    await message.reply_photo(
        photo=avatar_url, caption=caption, reply_markup=inline_keyboard
    )


__MODULE__ = "Gɪᴛʜᴜʙ"
__HELP__ = """
## GɪᴛHᴜʙ Cᴏᴍᴍᴀɴᴅs Hᴇᴘ

### 1. /ɢɪᴛʜᴜʙ ᴏʀ /ɢɪᴛ
**Dᴇsᴄʀɪᴘᴛɪᴏɴ:**
Fᴇᴛᴄʜᴇs GɪᴛHᴜʙ ᴜsᴇʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.

**Usᴀɢᴇ:**
/ɢɪᴛʜᴜʙ [ᴜsᴇʀɴᴀᴍᴇ]

**Dᴇᴛᴀɪs:**
- Rᴇᴛʀɪᴇᴠᴇs ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ GɪᴛHᴜʙ ᴜsᴇʀ.
- Dɪsᴘᴀʏs ᴅᴇᴛᴀɪs sᴜᴄʜ ᴀs ᴜsᴇʀɴᴀᴍᴇ, ʙɪᴏ, ᴄᴏᴍᴘᴀɴʏ, ʀᴇᴘᴏsɪᴛᴏʀɪᴇs, ғᴏᴏᴡᴇʀs, ᴀɴᴅ ᴍᴏʀᴇ.
- Pʀᴏᴠɪᴅᴇs ᴀ ɪɴᴋ ᴛᴏ ᴛʜᴇ ᴜsᴇʀ's GɪᴛHᴜʙ ᴘʀᴏғɪᴇ.
- Aᴄᴄᴇssɪʙᴇ ʙʏ ᴘʀᴏᴠɪᴅɪɴɢ ᴀ ᴠᴀɪᴅ GɪᴛHᴜʙ ᴜsᴇʀɴᴀᴍᴇ ᴀғᴛᴇʀ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ.

**Exᴀᴍᴘᴇs:**
- `/ɢɪᴛʜᴜʙ DONATE-ARMY-BOTS`
"""
