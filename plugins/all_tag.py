import asyncio

from pyrogram import filters

from DONATE_ARMY_MUSIC import app
from DONATE_ARMY_MUSIC.utils.branded_ban import admin_filter

SPAM_CHATS = []


@app.on_message(
    filters.command(["all", "mention", "mentionall"], prefixes=["/", "@", "#"])
    & admin_filter
)
async def tag_all_users(_, message):
    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss ɪs ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴛᴏᴘ sᴏ ᴜsᴇ /cancel"
        )
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text(
            "** ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ, ʟɪᴋᴇ »** `@all Hi Friends`"
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
            usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
            if usernum == 5:
                await replied.reply_text(usertxt)
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
            usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
            if usernum == 5:
                await app.send_message(
                    message.chat.id,
                    f"{text}\n{usertxt}\n\n|| ➥ ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ » /cancel ||",
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
            "stopmention",
            "offall",
            "cancel",
            "allstop",
            "stopall",
            "cancelmention",
            "offmention",
            "mentionoff",
            "alloff",
            "cancelall",
            "allcancel",
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


__MODULE__ = "Tᴀɢ Aʟʟ"
__HELP__ = """
**Tᴀɢ A Usᴇʀs**

Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀᴏᴡs ᴀᴅᴍɪɴs ᴛᴏ ᴛᴀɢ ᴀ ᴜsᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇ.

Cᴏᴍᴍᴀɴᴅs:
- /ᴀ <ᴛᴇxᴛ>: Tᴀɢ ᴀ ᴜsᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇ ᴡɪᴛʜ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴛᴇxᴛ.
- /ᴍᴇɴᴛɪᴏɴ <ᴛᴇxᴛ>: Tᴀɢ ᴀ ᴜsᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇ ᴡɪᴛʜ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴛᴇxᴛ.
- /ᴍᴇɴᴛɪᴏɴᴀ <ᴛᴇxᴛ>: Tᴀɢ ᴀ ᴜsᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇ ᴡɪᴛʜ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴛᴇxᴛ.

Tᴏ sᴛᴏᴘ ᴛᴀɢɢɪɴɢ:
- /sᴛᴏᴘᴍᴇɴᴛɪᴏɴ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴏғғᴀ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴄᴀɴᴄᴇ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴀsᴛᴏᴘ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /sᴛᴏᴘᴀ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴄᴀɴᴄᴇᴍᴇɴᴛɪᴏɴ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴏғғᴍᴇɴᴛɪᴏɴ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴍᴇɴᴛɪᴏɴᴏғғ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴀᴏғғ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴄᴀɴᴄᴇᴀ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴀᴄᴀɴᴄᴇ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.

Nᴏᴛᴇ: Oɴʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs.
"""
