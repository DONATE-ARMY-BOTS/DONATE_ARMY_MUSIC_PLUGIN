#
# Copyright (C) 2024 by DONATE_ARMY™@Github, < https://github.com/DONATE-ARMY-BOTS >.
#
# This file is part of < https://github.com/DONATE-ARMY-BOTS/DONATE_ARMY_TG_MUSIC_PLAYER > project,
# and is released under the MIT License.
# Please see < https://github.com/DONATE-ARMY-BOTS/DONATE_ARMY_TG_MUSIC_PLAYER/blob/master/LICENSE >
#
# All rights reserved.

import traceback
from functools import wraps

from config import LOG_GROUP_ID
from pyrogram.errors.exceptions.forbidden_403 import ChatWriteForbidden
from DONATE_ARMY_TG_MUSIC_PLAYER import app


def split_limits(text):
    if len(text) < 2048:
        return [text]

    lines = text.splitlines(True)
    small_msg = ""
    result = []
    for line in lines:
        if len(small_msg) + len(line) < 2048:
            small_msg += line
        else:
            result.append(small_msg)
            small_msg = line

    result.append(small_msg)

    return result


def capture_err(func):
    @wraps(func)
    async def capture(client, message, *args, **kwargs):
        try:
            return await func(client, message, *args, **kwargs)
        except ChatWriteForbidden:
            await app.leave_chat(message.chat.id)
            return
        except Exception as err:
            errors = traceback.format_exc()
            error_feedback = split_limits(
                "**ERROR** | {} | {}\n```command\n{}```\n\n```python\n{}```\n".format(
                    0 if not message.from_user else message.from_user.mention,
                    (
                        0
                        if not message.chat
                        else (
                            f"@{message.chat.username}"
                            if message.chat.username
                            else f"`{message.chat.id}`"
                        )
                    ),
                    message.text or message.caption,
                    "".join(errors),
                ),
            )
            for x in error_feedback:
                await app.send_message(LOG_GROUP_ID, x)
            raise err

    return capture
