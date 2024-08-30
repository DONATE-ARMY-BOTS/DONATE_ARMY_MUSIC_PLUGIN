from pyrogram import enums, filters

from DONATE_ARMY_MUSIC import app
from DONATE_ARMY_MUSIC.utils.branded_ban import admin_filter

BOT_ID = app.id


@app.on_message(filters.command("unbanall") & admin_filter)
async def unban_all(_, msg):
    chat_id = msg.chat.id
    x = 0
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members == True
    if bot_permission:
        banned_users = []
        async for m in app.get_chat_members(
            chat_id, filter=enums.ChatMembersFilter.BANNED
        ):
            banned_users.append(m.user.id)

        # Send message with total number of banned users found
        ok = await app.send_message(
            chat_id,
            f"Total **{len(banned_users)}** users found to unban.\n**Started unbanning..**",
        )

        for user_id in banned_users:
            try:
                await app.unban_chat_member(chat_id, user_id)
                x += 1

                # Edit message every 5 unbans to show progress
                if x % 5 == 0:
                    await ok.edit_text(
                        f"Unbanned {x} out of {len(banned_users)} users."
                    )

            except Exception:
                pass

        # Edit final message to show completion
        await ok.edit_text(f"Unbanned all {len(banned_users)} users.")

    else:
        await msg.reply_text(
            "ᴇɪᴛʜᴇʀ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs ᴏʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs"
        )


__MODULE__ = "Uɴʙᴀɴᴀʟʟ"
__HELP__ = """
**Uɴʙᴀɴ A**

Tʜɪs ᴍᴏᴅᴜᴇ ᴀᴏᴡs ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀs ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜsᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ ᴀᴛ ᴏɴᴄᴇ.

Cᴏᴍᴍᴀɴᴅs:
- /ᴜɴʙᴀɴᴀ: Sᴛᴀʀᴛ ᴜɴʙᴀɴɴɪɴɢ ᴀ ᴜsᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.

Nᴏᴛᴇ:
- Oɴʏ ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.
- Tʜᴇ ʙᴏᴛ ᴍᴜsᴛ ʜᴀᴠᴇ ᴛʜᴇ ɴᴇᴄᴇssᴀʀʏ ᴘᴇʀᴍɪssɪᴏɴs ᴛᴏ ᴜɴʙᴀɴ ᴜsᴇʀs.
"""
