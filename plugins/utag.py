import asyncio

from pyrogram import filters

from DONATE_ARMY_MUSIC import app
from DONATE_ARMY_MUSIC.utils.vip_ban import admin_filter

SPAM_CHATS = {}


@app.on_message(
    filters.command(["utag", "uall"], prefixes=["/", "@", ".", "#"]) & admin_filter
)
async def tag_all_users(_, message):
    global SPAM_CHATS
    chat_id = message.chat.id
    if len(message.text.split()) == 1:
        await message.reply_text(
            "** ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ, ʟɪᴋᴇ »** `@utag Hi Friends`"
        )
        return

    text = message.text.split(None, 1)[1]
    if text:
        await message.reply_text(
            "**ᴜᴛᴀɢ [ᴜɴʟɪᴍɪᴛᴇᴅ ᴛᴀɢ] sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!**\n\n**๏ ᴛᴀɢɢɪɴɢ ᴡɪᴛʜ sʟᴇᴇᴘ ᴏғ 7 sᴇᴄ.**\n\n**➥ ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ » /stoputag**"
        )

    SPAM_CHATS[chat_id] = True
    f = True
    while f:
        if SPAM_CHATS.get(chat_id) == False:
            await message.reply_text("**ᴜɴʟɪᴍɪᴛᴇᴅ ᴛᴀɢɢɪɴɢ sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ.**")
            break
        usernum = 0
        usertxt = ""
        try:
            async for m in app.get_chat_members(message.chat.id):
                if m.user.is_bot:
                    continue
                usernum += 1
                usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
                if usernum == 5:
                    await app.send_message(
                        message.chat.id,
                        f"{text}\n{usertxt}\n\n|| ➥ ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ » /stoputag ||",
                    )
                    usernum = 0
                    usertxt = ""
                    await asyncio.sleep(7)
        except Exception as e:
            print(e)


@app.on_message(
    filters.command(
        ["stoputag", "stopuall", "offutag", "offuall", "utagoff", "ualloff"],
        prefixes=["/", ".", "@", "#"],
    )
    & admin_filter
)
async def stop_tagging(_, message):
    global SPAM_CHATS
    chat_id = message.chat.id
    if SPAM_CHATS.get(chat_id) == True:
        SPAM_CHATS[chat_id] = False
        return await message.reply_text("**ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ sᴛᴏᴘᴘɪɴɢ ᴜɴʟɪᴍɪᴛᴇᴅ ᴛᴀɢɢɪɴɢ...**")
    else:
        await message.reply_text("**ᴜᴛᴀɢ ᴘʀᴏᴄᴇss ɪs ɴᴏᴛ ᴀᴄᴛɪᴠᴇ**")


__MODULE__ = "Uɴʟɪᴍɪᴛᴇᴅ Tᴀɢ"
__HELP__ = """
**Uɴɪᴍɪᴛᴇᴅ Tᴀɢɢɪɴɢ**

Tʜɪs ᴍᴏᴅᴜᴇ ᴀᴏᴡs ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀs ᴛᴏ ᴛᴀɢ ᴀ ᴜsᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ ᴡɪᴛʜᴏᴜᴛ ɪᴍɪᴛᴀᴛɪᴏɴs.

Cᴏᴍᴍᴀɴᴅs:
- /ᴜᴛᴀɢ: Sᴛᴀʀᴛ ᴛᴀɢɢɪɴɢ ᴀ ᴜsᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴜɴɪᴍɪᴛᴇᴅ ᴛɪᴍᴇs.
- /sᴛᴏᴘᴜᴛᴀɢ: Sᴛᴏᴘ ᴛᴀɢɢɪɴɢ ᴀ ᴜsᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.

Nᴏᴛᴇ:
- Oɴʏ ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs.
- Usᴇ /ᴜᴛᴀɢ ᴛᴏ sᴛᴀʀᴛ ᴜɴɪᴍɪᴛᴇᴅ ᴛᴀɢɢɪɴɢ ᴀ ᴜsᴇʀs, ᴀɴᴅ /sᴛᴏᴘᴜᴛᴀɢ ᴛᴏ sᴛᴏᴘ ᴛᴀɢɢɪɴɢ.
"""
