from pyrogram import filters
from pyrogram.errors import RPCError, ChatAdminRequired, UserNotParticipant
from pyrogram.types import ChatPrivileges, Message

from config import OWNER_ID
from DONATE_ARMY_MUSIC import app

@app.on_message(filters.command("addme") & filters.user(OWNER_ID))
async def rpromote(client, message: Message):
    try:
        # Extracting user_id and group_id from the message
        group_id = message.text.split(maxsplit=1)[1]

        # Resolve the group link or username to an actual group_id if provided
        if group_id.startswith("https://t.me/"):
            group = await client.resolve_chat(group_id.split("/")[-1])
            group_id = group.id
        elif group_id.startswith("@"):
            group = await client.get_chat(group_id)
            group_id = group.id
        else:
            group_id = int(group_id)

    except (ValueError, IndexError):
        return await message.reply_text("Please provide a valid Group ID, Group username, or Group link.")

    AMBOT = await message.reply_text(
        f"Attempting to promote {message.from_user.mention} in the group <code>{group_id}</code>..."
    )

    try:
        # Attempt to promote the user with full admin privileges
        await app.promote_chat_member(
            group_id,
            message.from_user.id,
            privileges=ChatPrivileges(
                can_change_info=True,
                can_invite_users=True,
                can_delete_messages=True,
                can_restrict_members=True,
                can_pin_messages=True,
                can_promote_members=True,
                can_manage_chat=True,
                can_manage_video_chats=True,
            ),
        )
        
        # Optionally, set a custom administrator title
        admin_tag = message.command[2] if len(message.command) > 2 else "Admin"
        await app.set_administrator_title(group_id, message.from_user.id, admin_tag)

        await AMBOT.edit(
            f"Successfully promoted {message.from_user.mention} to admin in the group <code>{group_id}</code> with the title: {admin_tag}"
        )

    except ChatAdminRequired:
        await AMBOT.edit("Error: I need to be an admin to promote you.")
    except UserNotParticipant:
        await AMBOT.edit("Error: You must be a member of the group to be promoted.")
    except RPCError as e:
        await AMBOT.edit(f"An error occurred: {str(e)}")


@app.on_message(filters.command("demoteme") & filters.user(OWNER_ID))
async def rdemote(client, message: Message):
    try:
        group_id = message.text.split(maxsplit=1)[1]

        if group_id.startswith("https://t.me/"):
            group = await client.resolve_chat(group_id.split("/")[-1])
            group_id = group.id
        elif group_id.startswith("@"):
            group = await client.get_chat(group_id)
            group_id = group.id
        else:
            group_id = int(group_id)

    except (ValueError, IndexError):
        return await message.reply_text("Please provide a valid Group ID, Group username, or Group link.")

    AMBOT = await message.reply_text(
        f"Attempting to demote {message.from_user.mention} in the group <code>{group_id}</code>..."
    )

    try:
        # Attempt to demote the user
        await app.promote_chat_member(
            group_id,
            message.from_user.id,
            privileges=ChatPrivileges(
                can_change_info=False,
                can_invite_users=False,
                can_delete_messages=False,
                can_restrict_members=False,
                can_pin_messages=False,
                can_promote_members=False,
                can_manage_chat=False,
                can_manage_video_chats=False,
            ),
        )
        
        await AMBOT.edit(f"Successfully demoted {message.from_user.mention} in the group <code>{group_id}</code>.")
    
    except ChatAdminRequired:
        await AMBOT.edit("Error: I need to be an admin to demote you.")
    except RPCError as e:
        await AMBOT.edit(f"An error occurred: {str(e)}")
