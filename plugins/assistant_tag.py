import asyncio

from pyrogram import filters
from pyrogram.enums import ParseMode

from DONATE_ARMY_MUSIC import app
from DONATE_ARMY_MUSIC.misc import SUDOERS
from DONATE_ARMY_MUSIC.utils.database import get_assistant
from DONATE_ARMY_MUSIC.utils.vip_ban import admin_filter

SPAM_CHATS = []


@app.on_message(
    filters.command(
        ["atag", "aall", "amention", "amentionall"], prefixes=["/", "@", "#"]
    )
    & SUDOERS
)
async def tag_all_useres(_, message):
    userbot = await get_assistant(message.chat.id)
    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss ɪs ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴛᴏᴘ sᴏ ᴜsᴇ /acancel"
        )
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text(
            "** ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ, ʟɪᴋᴇ »** `@aall Hi Friends`"
        )
        return
    if replied:
        SPAM_CHATS.append(message.chat.id)
        usernum = 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id):
            if message.chat.id not in SPAM_CHATS:
                break
            usernum += 1
            usertxt += (
                f"\n⊚ [{m.user.first_name}](tg://openmessage?user_id={m.user.id})\n"
            )
            if usernum == 5:
                await replied.reply_text(usertxt, ParseMode.MARKDOWN)
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        text = message.text.split(None, 1)[1]

        SPAM_CHATS.append(message.chat.id)
        usernum = 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id):
            if message.chat.id not in SPAM_CHATS:
                break
            usernum += 1
            usertxt += f'\n⊚ <a href="tg://openmessage?user_id={m.user.id}">{m.user.first_name}</a>\n'

            if usernum == 5:
                await userbot.send_message(
                    message.chat.id,
                    f"{text}\n{usertxt}\n\n|| ➥ ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ » /acancel ||",
                    ParseMode.HTML,
                )
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass


@app.on_message(
    filters.command(
        [
            "astopmention",
            "aoffall",
            "acancel",
            "aallstop",
            "astopall",
            "acancelmention",
            "aoffmention",
            "amentionoff",
            "aalloff",
            "acancelall",
            "aallcancel",
        ],
        prefixes=["/", "@", "#"],
    )
    & admin_filter
)
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass
        return await message.reply_text("**ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ!**")

    else:
        await message.reply_text("**ɴᴏ ᴘʀᴏᴄᴇss ᴏɴɢᴏɪɴɢ!**")
        return


__MODULE__ = "Usᴇʀʙᴏᴛ Tᴀɢ"
__HELP__ = """
**Tᴀɢ A Usᴇʀs (Bʏ Assɪsᴛᴀɴᴛ)**

Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀᴏᴡs sᴜᴅᴏ ᴜsᴇʀs ᴛᴏ ᴛᴀɢ ᴀ ᴜsᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇ.

Cᴏᴍᴍᴀɴᴅs:
- /ᴀᴛᴀɢ <ᴛᴇxᴛ>: Tᴀɢ ᴀ ᴜsᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇ ᴡɪᴛʜ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴛᴇxᴛ.
- /ᴀᴀ <ᴛᴇxᴛ>: Tᴀɢ ᴀ ᴜsᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇ ᴡɪᴛʜ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴛᴇxᴛ.
- /ᴀᴍᴇɴᴛɪᴏɴ <ᴛᴇxᴛ>: Tᴀɢ ᴀ ᴜsᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇ ᴡɪᴛʜ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴛᴇxᴛ.
- /ᴀᴍᴇɴᴛɪᴏɴᴀ <ᴛᴇxᴛ>: Tᴀɢ ᴀ ᴜsᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇ ᴡɪᴛʜ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴛᴇxᴛ.

Tᴏ sᴛᴏᴘ ᴛᴀɢɢɪɴɢ:
- /ᴀsᴛᴏᴘᴍᴇɴᴛɪᴏɴ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴀᴏғғᴀ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴀᴄᴀɴᴄᴇ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴀᴀsᴛᴏᴘ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴀsᴛᴏᴘᴀ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴀᴄᴀɴᴄᴇᴍᴇɴᴛɪᴏɴ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴀᴏғғᴍᴇɴᴛɪᴏɴ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴀᴍᴇɴᴛɪᴏɴᴏғғ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴀᴀᴏғғ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴀᴄᴀɴᴄᴇᴀ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴀᴀᴄᴀɴᴄᴇ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.

Nᴏᴛᴇ: Oɴʏ sᴜᴅᴏ ᴜsᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs.
"""
