import asyncio
from time import time

from pyrogram import *
from pyrogram.types import *
from DONATE_ARMY_MUSIC import app

# Define a dictionary to track the last message timestamp for each user
user_last_message_time = {}
user_command_count = {}
# Define the threshold for command spamming (e.g., 20 commands within 60 seconds)
SPAM_THRESHOLD = 2
SPAM_WINDOW_SECONDS = 5


@app.on_message(filters.command(["bin", "ccbin", "bininfo"], [".", "!", "/"]))
async def check_ccbin(client, message):
    user_id = message.from_user.id
    current_time = time()
    # Update the last message timestamp for the user
    last_message_time = user_last_message_time.get(user_id, 0)

    if current_time - last_message_time < SPAM_WINDOW_SECONDS:
        # If less than the spam window time has passed since the last message
        user_last_message_time[user_id] = current_time
        user_command_count[user_id] = user_command_count.get(user_id, 0) + 1
        if user_command_count[user_id] > SPAM_THRESHOLD:
            # Block the user if they exceed the threshold
            hu = await message.reply_text(
                f"**{message.from_user.mention} ᴘʟᴇᴀsᴇ ᴅᴏɴᴛ ᴅᴏ sᴘᴀᴍ, ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴀғᴛᴇʀ 5 sᴇᴄ**"
            )
            await asyncio.sleep(3)
            await hu.delete()
            return
    else:
        # If more than the spam window time has passed, reset the command count and update the message timestamp
        user_command_count[user_id] = 1
        user_last_message_time[user_id] = current_time

    if len(message.command) < 2:
        return await message.reply_text(
            "<b>Please Give Me a Bin To\nGet Bin Details !</b>"
        )
    try:
        await message.delete()
    except:
        pass
    aux = await message.reply_text("<b>Checking ...</b>")
    bin = message.text.split(None, 1)[1]
    if len(bin) < 6:
        return await aux.edit("<b>❌ Wrong Bin❗...</b>")
    try:
        resp = await api.bininfo(bin)
        await aux.edit(
            f"""
<b>💠 Bin Full Details:</b>

<b>🏦 Bank:</b> <tt>{resp.bank}</tt>
<b>💳 Bin:</b> <tt>{resp.bin}</tt>
<b>🏡 Country:</b> <tt>{resp.country}</tt>
<b>🇮🇳 Flag:</b> <tt>{resp.flag}</tt>
<b>🧿 ISO:</b> <tt>{resp.iso}</tt>
<b>⏳ Level:</b> <tt>{resp.level}</tt>
<b>🔴 Prepaid:</b> <tt>{resp.prepaid}</tt>
<b>🆔 Type:</b> <tt>{resp.type}</tt>
<b>ℹ️ Vendor:</b> <tt>{resp.vendor}</tt>"""
        )
    except:
        return await aux.edit(
            f"""
🚫 BIN not recognized. Please enter a valid BIN."""
        )


__MODULE__ = "CC-BIN"
__HELP__ = """
## CC-BIN Cᴏᴍᴍᴀɴᴅ

### Cᴏᴍᴍᴀɴᴅ: /ʙɪɴ, /ᴄᴄʙɪɴ, /ʙɪɴɪɴғᴏ
**Dᴇsᴄʀɪᴘᴛɪᴏɴ:**
Fᴇᴛᴄʜᴇs ᴅᴇᴛᴀɪs ᴀʙᴏᴜᴛ ᴀ ɢɪᴠᴇɴ BIN (Bᴀɴᴋ Iᴅᴇɴᴛɪғɪᴄᴀᴛɪᴏɴ Nᴜᴍʙᴇʀ).

**Usᴀɢᴇ:**
/ʙɪɴ BIN_NUMBER
/ᴄᴄʙɪɴ BIN_NUMBER
/ʙɪɴɪɴғᴏ BIN_NUMBER

**Dᴇᴛᴀɪs:**
- Pʀᴏᴠɪᴅᴇs ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴀɴᴋ, ᴄᴏᴜɴᴛʀʏ, ᴛʏᴘᴇ, ᴀɴᴅ ᴠᴇɴᴅᴏʀ ғᴏʀ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ BIN.
- Aɴᴛɪ-sᴘᴀᴍ ᴍᴇᴀsᴜʀᴇs ᴀʀᴇ ɪɴ ᴘᴀᴄᴇ ᴛᴏ ᴘʀᴇᴠᴇɴᴛ ᴄᴏᴍᴍᴀɴᴅ sᴘᴀᴍᴍɪɴɢ. Usᴇʀs ᴄᴀɴ ᴏɴʏ ᴜsᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ ᴛᴡɪᴄᴇ ᴡɪᴛʜɪɴ 5 sᴇᴄᴏɴᴅs.

**Exᴀᴍᴘᴇs:**
- /ʙɪɴ 123456: Rᴇᴛʀɪᴇᴠᴇs BIN ᴅᴇᴛᴀɪs ғᴏʀ 123456.

**Nᴏᴛᴇs:**
- Iғ ᴛʜᴇ BIN ɪs ɴᴏᴛ ʀᴇᴄᴏɢɴɪᴢᴇᴅ ᴏʀ ɪs ɪɴᴠᴀɪᴅ, ᴀɴ ᴇʀʀᴏʀ ᴍᴇssᴀɢᴇ ɪs ᴅɪsᴘᴀʏᴇᴅ.

### Aɴᴛɪ-Sᴘᴀᴍ:
- Usᴇʀs ᴀʀᴇ ʙᴏᴄᴋᴇᴅ ғʀᴏᴍ sᴘᴀᴍᴍɪɴɢ ᴄᴏᴍᴍᴀɴᴅs ʙʏ ɪᴍɪᴛɪɴɢ ᴛᴏ 2 ᴄᴏᴍᴍᴀɴᴅs ᴡɪᴛʜɪɴ 5 sᴇᴄᴏɴᴅs.
"""
