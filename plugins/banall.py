from pyrogram import filters

from DONATE_ARMY_MUSIC import app
from DONATE_ARMY_MUSIC.misc import SUDOERS

BOT_ID = app.id


@app.on_message(filters.command("banall") & SUDOERS)
async def ban_all(_, msg):
    chat_id = msg.chat.id
    user_id = msg.from_user.id  # ID of the user who issued the command
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members == True

    if bot_permission:
        total_members = 0
        banned_count = 0

        async for member in app.get_chat_members(chat_id):
            total_members += 1

        ok = await msg.reply_text(
            f"Total members found: {total_members}\n**Started Banning..**"
        )

        async for member in app.get_chat_members(chat_id):
            try:
                if member.user.id != user_id and member.user.id not in SUDOERS:
                    await app.ban_chat_member(chat_id, member.user.id)
                    banned_count += 1

                    if banned_count % 5 == 0:
                        await ok.edit_text(
                            f"Banned {banned_count} members out of {total_members}"
                        )

            except Exception as e:
                pass

        await ok.edit_text(
            f"Total banned: {banned_count}\nFailed bans: {total_members - banned_count}"
        )

    else:
        await msg.reply_text(
            "Either I don't have the right to restrict users or you are not in sudo users"
        )


__MODULE__ = "Bᴀɴᴀʟʟ"
__HELP__ = """
**Bᴀɴ A**

Tʜɪs ᴍᴏᴅᴜᴇ ᴀᴏᴡs sᴜᴅᴏ ᴜsᴇʀs ᴛᴏ ʙᴀɴ ᴀ ᴍᴇᴍʙᴇʀs ғʀᴏᴍ ᴀ ɢʀᴏᴜᴘ, ᴇxᴄᴇᴘᴛ ᴛʜᴇᴍsᴇᴠᴇs.

Cᴏᴍᴍᴀɴᴅ:
- /ʙᴀɴᴀ: Bᴀɴ ᴀ ᴍᴇᴍʙᴇʀs ғʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ.

Nᴏᴛᴇ:
- Oɴʏ sᴜᴅᴏ ᴜsᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.
"""
