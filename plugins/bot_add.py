import random

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import LOG_GROUP_ID
from DONATE_ARMY_MUSIC import app
from DONATE_ARMY_MUSIC.utils.database import add_served_chat, get_assistant

photo = [
    "https://telegra.ph/file/bcae8ac8c17384b16b4f0.jpg",
    "https://telegra.ph/file/2aa24f64d31dd85263fc7.jpg",
    "https://telegra.ph/file/668eb2603627d8eacd08b.jpg",
    "https://telegra.ph/file/272c27a0f7a8b5326348d.jpg",
    "https://telegra.ph/file/eb9abbc129c21bcc4bb1c.jpg",
]



@app.on_message(filters.new_chat_members, group=-10)
async def join_watcher(_, message):
    try:
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for members in message.new_chat_members:
            if members.id == app.id:
                count = await app.get_chat_members_count(chat.id)
                username = (
                    message.chat.username if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐆ʀᴏᴜᴘ"
                )
                msg = (
                    f"**📝𝐌ᴜsɪᴄ 𝐁ᴏᴛ 𝐀ᴅᴅᴇᴅ 𝐈ɴ 𝐀 #𝐍ᴇᴡ_𝐆ʀᴏᴜᴘ**\n\n"
                    f"**📌𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ:** {message.chat.title}\n"
                    f"**🍂𝐂ʜᴀᴛ 𝐈ᴅ:** `{message.chat.id}`\n"
                    f"**🔐𝐂ʜᴀᴛ 𝐔sᴇʀɴᴀᴍᴇ:** @{username}\n"
                    f"**📈𝐆ʀᴏᴜᴘ 𝐌ᴇᴍʙᴇʀs:** {count}\n"
                    f"**🤔𝐀ᴅᴅᴇᴅ 𝐁ʏ:** {message.from_user.mention}"
                )
                await app.send_photo(
                    LOG_GROUP_ID,
                    photo=random.choice(photo),
                    caption=msg,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    f"😍𝐀ᴅᴅᴇᴅ 𝐁ʏ😍",
                                    url=f"tg://openmessage?user_id={message.from_user.id}",
                                )
                            ]
                        ]
                    ),
                )
                await add_served_chat(message.chat.id)
                await userbot.join_chat(f"{username}")
                

    except Exception as e:
        print(f"Error: {e}")
