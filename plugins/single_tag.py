import asyncio
import random

from DONATE_ARMY_TG_MUSIC_PLAYER import app
from pyrogram import filters
from pyrogram.enums import ChatMemberStatus, ChatType
from pyrogram.errors import UserNotParticipant


spam_chats = []

EMOJI = [
    "🦋🦋🦋🦋🦋",
    "🧚🌸🧋🍬🫖",
    "🥀🌷🌹🌺💐",
    "🌸🌿💮🌱🌵",
    "❤️💚💙💜🖤",
    "💓💕💞💗💖",
    "🌸💐🌺🌹🦋",
    "🍔🦪🍛🍲🥗",
    "🍎🍓🍒🍑🌶️",
    "🧋🥤🧋🥛🍷",
    "🍬🍭🧁🎂🍡",
    "🍨🧉🍺☕🍻",
    "🥪🥧🍦🍥🍚",
    "🫖☕🍹🍷🥛",
    "☕🧃🍩🍦🍙",
    "🍁🌾💮🍂🌿",
    "🌨️🌥️⛈️🌩️🌧️",
    "🌷🏵️🌸🌺💐",
    "💮🌼🌻🍀🍁",
    "🧟🦸🦹🧙👸",
    "🧅🍠🥕🌽🥦",
    "🐷🐹🐭🐨🐻‍❄️",
    "🦋🐇🐀🐈🐈‍⬛",
    "🌼🌳🌲🌴🌵",
    "🥩🍋🍐🍈🍇",
    "🍴🍽️🔪🍶🥃",
    "🕌🏰🏩⛩️🏩",
    "🎉🎊🎈🎂🎀",
    "🪴🌵🌴🌳🌲",
    "🎄🎋🎍🎑🎎",
    "🦅🦜🕊️🦤🦢",
    "🦤🦩🦚🦃🦆",
    "🐬🦭🦈🐋🐳",
    "🐔🐟🐠🐡🦐",
    "🦩🦀🦑🐙🦪",
    "🐦🦂🕷️🕸️🐚",
    "🥪🍰🥧🍨🍨",
    " 🥬🍉🧁🧇",
]

TAGMES = [
    " **𝐇𝐞𝐲 𝐁𝐚𝐛𝐲 𝐍𝐞𝐞𝐧𝐠𝐚 𝐄𝐧𝐠𝐞 𝐈𝐫𝐮𝐤𝐤𝐢𝐧𝐠𝐚🤗🥱** ",
    " **𝐎𝐧𝐠𝐚 𝐊𝐢𝐝𝐚𝐲𝐚 𝐒𝐨𝐧𝐧𝐚𝐦𝐚𝐚 𝐎𝐧𝐥𝐢𝐧𝐞 𝐕𝐚𝐧𝐠𝐨😊** ",
    " **𝐕𝐜 𝐕𝐚𝐫𝐮𝐦 𝐏𝐞𝐬𝐚𝐥𝐚𝐦𝐚𝐚𝐦𝐚 𝐊𝐨𝐧𝐣𝐚𝐦😃** ",
    " **𝐒𝐚𝐩𝐭𝐭𝐮𝐭𝐞𝐧𝐠𝐚𝐥𝐚 𝐉𝐢..??🥲** ",
    " **𝐕𝐞𝐢𝐭𝐭𝐮𝐤𝐚𝐫𝐚𝐧𝐠𝐚 𝐄𝐥𝐥𝐚𝐦𝐞 𝐒𝐚𝐧𝐭𝐡𝐨𝐬𝐚𝐦𝐚𝐚 𝐈𝐫𝐮𝐤𝐤𝐚𝐧𝐠𝐚 𝐉𝐢🥺** ",
    " **𝐄𝐧𝐚𝐤𝐤𝐮 𝐑𝐨𝐦𝐛𝐚 𝐌𝐢𝐬𝐬 𝐏𝐚𝐧𝐧𝐢𝐭𝐭𝐞𝐧 𝐔𝐧𝐧𝐚🤭** ",
    " **𝐇𝐚𝐥 𝐂𝐡𝐚𝐥 𝐄𝐩𝐩𝐚𝐝𝐢 𝐈𝐫𝐮𝐤𝐤𝐮..??🤨** ",
    " **𝐄𝐧𝐤𝐮𝐦 𝐎𝐫𝐮 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 𝐏𝐚𝐧𝐧𝐢 𝐊𝐨𝐝𝐮𝐤𝐢𝐧𝐠𝐚𝐥𝐚..??🙂** ",
    " **𝐔𝐧𝐠𝐚𝐥𝐨𝐝𝐚 𝐏𝐞𝐫 𝐄𝐧𝐧𝐚𝐦 𝐒𝐨𝐥𝐥𝐮𝐧𝐠𝐚..??🥲** ",
    " **𝐊𝐚𝐩𝐩𝐢 𝐀𝐭𝐭𝐚𝐭𝐡𝐮 𝐒𝐚𝐩𝐭𝐭𝐮𝐭𝐞𝐧𝐠𝐚𝐥𝐚..??😋** ",
    " **𝐄𝐧𝐤𝐮𝐦 𝐆𝐫𝐨𝐮𝐩𝐮𝐤𝐮 𝐊𝐢𝐝𝐧𝐚𝐩 𝐏𝐚𝐧𝐧𝐢 𝐕𝐚𝐧𝐠𝐨😍** ",
    " **𝐔𝐧𝐠𝐚 𝐏𝐚𝐫𝐭𝐧𝐞𝐫 𝐔𝐧𝐧𝐚 𝐓𝐡𝐞𝐝𝐮𝐫𝐚𝐧𝐠𝐚 𝐎𝐧𝐥𝐢𝐧𝐞 𝐕𝐚𝐧𝐠𝐨😅😅** ",
    " **𝐄𝐧𝐤𝐮𝐦 𝐍𝐚𝐦𝐦 𝐅𝐫𝐢𝐞𝐧𝐝𝐬 𝐀𝐚𝐠𝐚𝐦𝐮𝐦𝐚𝐚..??🤔** ",
    " **𝐒𝐨𝐧𝐚𝐦𝐚𝐚 𝐒𝐨𝐧𝐧𝐚𝐦𝐚𝐚𝐦𝐚 𝐏𝐨𝐢𝐭𝐭𝐢𝐧𝐠𝐚𝐥𝐚🙄🙄** ",
    " **𝐎𝐫𝐮 𝐏𝐚𝐭𝐭𝐮 𝐏𝐥𝐚𝐲 𝐏𝐚𝐧𝐧𝐮𝐯𝐞𝐧 𝐍𝐚 𝐏𝐥𝐬𝐬😕** ",
    " **𝐔𝐧𝐠𝐚 𝐄𝐧𝐝𝐡𝐮 𝐎𝐫𝐮 𝐈𝐝𝐚𝐦 𝐒𝐨𝐥𝐥𝐮𝐧𝐠𝐚..??🙃** ",
    " **𝐇𝐞𝐥𝐥𝐨 𝐉𝐢 𝐕𝐚𝐧𝐚𝐤𝐤𝐚𝐦😛** ",
    " **𝐇𝐞𝐥𝐥𝐨 𝐁𝐚𝐛𝐲 𝐄𝐩𝐩𝐚𝐝𝐢𝐫𝐮𝐤𝐤𝐞..?🤔** ",
    " **𝐍𝐞𝐞𝐧𝐠𝐚 𝐄𝐧𝐠𝐚𝐥𝐮𝐤𝐤𝐮 𝐎𝐰𝐧𝐞𝐫 𝐀𝐡 𝐓𝐡𝐞𝐫𝐢𝐲𝐮𝐦𝐚..?** ",
    " **𝐕𝐚𝐫𝐮𝐦 𝐕𝐢𝐥𝐚𝐢𝐚𝐭𝐭𝐮 𝐊𝐞𝐥𝐮𝐧𝐠𝐚 𝐏𝐨𝐭𝐭𝐮 𝐕𝐚𝐧𝐠𝐨🤗** ",
    " **𝐏𝐞𝐬𝐚𝐦𝐚 𝐍𝐚𝐦𝐦𝐚𝐥𝐮𝐤𝐤𝐮 𝐒𝐚𝐧𝐭𝐡𝐨𝐬𝐚𝐦𝐚𝐚𝐠𝐮𝐦😇** ",
    " **𝐔𝐧𝐠𝐚 𝐌𝐮𝐦𝐦𝐲 𝐄𝐧𝐧𝐚 𝐒𝐞𝐢𝐫𝐚𝐧𝐠𝐚..?🤭** ",
    " **𝐄𝐧𝐤𝐢𝐭𝐚𝐢𝐭𝐭𝐮 𝐏𝐞𝐬𝐮𝐧𝐠𝐚 𝐏𝐥𝐬🥺🥺** ",
    " **𝐎𝐧𝐥𝐢𝐧𝐞 𝐕𝐚𝐧𝐭𝐮 𝐍𝐚𝐭𝐚𝐦 𝐒𝐞𝐲𝐲𝐮😶** ",
    " **𝐒𝐜𝐡𝐨𝐨𝐥𝐮𝐤𝐤𝐮 𝐇𝐨𝐥𝐢𝐝𝐚𝐲 𝐒𝐨𝐧𝐧𝐚𝐦𝐚𝐚 𝐂𝐡𝐞𝐜𝐤 𝐏𝐚𝐧𝐧𝐮..??🤔** ",
    " **𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 😜** ",
    " **𝐎𝐫𝐮 𝐕𝐞𝐥𝐚𝐢 𝐒𝐞𝐲𝐲𝐚 𝐇𝐞𝐥𝐩 𝐏𝐚𝐧𝐧𝐢𝐭𝐮𝐦𝐚🙂** ",
    " **𝐎𝐫𝐮 𝐏𝐚𝐭𝐭𝐮 𝐕𝐚𝐢𝐭𝐡𝐮 𝐕𝐞𝐫𝐢𝐟𝐲 𝐏𝐚𝐧𝐧𝐮𝐦😪** ",
    " **𝐍𝐢𝐜𝐞 𝐓𝐨 𝐌𝐞𝐞𝐭 𝐔 ☺** ",
    " **𝐇𝐞𝐥𝐥𝐨 🙊** ",
    " **𝐎𝐧𝐠𝐚 𝐒𝐭𝐮𝐝𝐲 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞 𝐀𝐠𝐮𝐦𝐚?😺** ",
    " **𝐒𝐨𝐦𝐛𝐚𝐭𝐡𝐢𝐥𝐚𝐦𝐚 𝐏𝐞𝐬𝐚𝐭𝐡𝐞𝐧🥲** ",
    " **𝐒𝐨𝐧𝐚𝐥𝐢 𝐍𝐚𝐦𝐚𝐤𝐤𝐮 𝐓𝐡𝐞𝐫𝐢𝐲𝐮𝐦𝐚😅** ",
    " **𝐔𝐧 𝐏𝐡𝐨𝐭𝐨 𝐄𝐝𝐮𝐭𝐡𝐮𝐯𝐚𝐦𝐚?😅** ",
    " **𝐌𝐮𝐦𝐦𝐲 𝐕𝐚𝐧𝐝𝐡𝐮𝐫𝐚𝐚𝐧𝐠𝐚😆😆😆** ",
    " **𝐍𝐚𝐦𝐦𝐚 𝐅𝐫𝐢𝐞𝐧𝐝𝐬 𝐄𝐩𝐩𝐚𝐝𝐢 𝐈𝐫𝐮𝐤𝐤𝐚𝐧𝐠𝐚😉** ",
    " **𝐍𝐚𝐧 𝐔𝐧𝐧𝐚𝐢 𝐕𝐚𝐥𝐥𝐢𝐤𝐢𝐫𝐞𝐧🙈🙈🙈** ",
    " **𝐍𝐞𝐞 𝐕𝐚𝐥𝐥𝐢𝐤𝐢𝐫𝐢𝐲𝐚..?👀** ",
    " **𝐑𝐚𝐤𝐡𝐢 𝐒𝐞𝐢𝐲𝐲𝐚𝐮𝐦𝐚?🙉** ",
    " **𝐏𝐚𝐭𝐭𝐮 𝐊𝐞𝐭𝐤𝐚𝐦𝐚..?😹** ",
    " **𝐎𝐧𝐥𝐢𝐧𝐞 𝐕𝐚𝐧𝐝𝐡𝐮 𝐏𝐚𝐭𝐭𝐮 𝐏𝐥𝐚𝐲 𝐒𝐞𝐲𝐲𝐲𝐮😻** ",
    " **𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐔𝐬𝐞 𝐏𝐚𝐧𝐫𝐢𝐲𝐚?🙃** ",
    " **𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐍𝐮𝐦𝐛𝐞𝐫 𝐏𝐨𝐝𝐮𝐯𝐢𝐲𝐚..?😕** ",
    " **𝐔𝐧𝐠𝐚 𝐌𝐮𝐬𝐢𝐜 𝐓𝐚𝐧𝐝𝐡𝐢𝐤𝐚 𝐒𝐨𝐥𝐥𝐮𝐧𝐠𝐚..?🙃** ",
    " **𝐔𝐧𝐠𝐚 𝐕𝐞𝐥𝐚𝐢 𝐌𝐮𝐝𝐢𝐧𝐭𝐡𝐮𝐫𝐮𝐤𝐤𝐚?🙃** ",
    " **𝐎𝐧𝐠𝐚𝐥 𝐄𝐧𝐠𝐞𝐝𝐡𝐮 𝐕𝐚𝐫𝐮𝐯𝐚𝐧𝐠𝐚😊** ",
    " **𝐒𝐨𝐥𝐥𝐮 𝐍𝐚🧐** ",
    " **𝐄𝐧𝐤𝐮𝐦 𝐒𝐚𝐡𝐚𝐲𝐦 𝐒𝐞𝐲𝐲𝐲𝐮𝐦𝐚..?** ",
    " **𝐕𝐚𝐧𝐚𝐤𝐤𝐚𝐦, 𝐇𝐨𝐥𝐝 𝐒𝐞𝐲𝐲𝐲𝐮 😠** ",
    " **𝐔𝐧𝐠𝐚 𝐏𝐚𝐫𝐞𝐧𝐭𝐬 𝐄𝐩𝐩𝐚𝐝𝐢 𝐈𝐫𝐮𝐤𝐤𝐚𝐧𝐠𝐚..?❤** ",
    " **𝐄𝐧𝐧𝐚 𝐒𝐞𝐢𝐲𝐲𝐫𝐚𝐢𝐫𝐮..?👱** ",
    " **𝐔𝐧𝐧𝐚 𝐕𝐚𝐥𝐥𝐢 𝐍𝐞𝐧𝐚𝐢𝐤𝐤𝐢𝐫𝐞𝐧 🤧❣️** ",
    " **𝐔𝐧𝐧𝐚𝐢 𝐕𝐢𝐬𝐚𝐫𝐢𝐤𝐤𝐢𝐭𝐮 𝐊𝐚𝐝𝐚𝐢𝐤𝐤𝐮𝐦𝐚..?😏😏** ",
    " **𝐔𝐧𝐠𝐚𝐥 𝐍𝐞𝐧𝐚𝐢𝐕𝐚𝐥𝐚𝐧𝐝𝐡𝐮 𝐂𝐡𝐞𝐲𝐲𝐲𝐮😐** ",
    " **𝐒𝐚𝐩𝐩𝐭𝐮𝐭𝐞𝐧𝐠𝐚𝐥𝐚😒** ",
    " **𝐄𝐩𝐩𝐚𝐝𝐢 𝐈𝐫𝐮𝐤𝐤𝐮😮😮** ",
    " **𝐇𝐞𝐥𝐥𝐨👀** ",
    " **𝐍𝐚𝐦𝐦 𝐃𝐨𝐬𝐭 𝐁𝐞𝐬𝐭 𝐈𝐫𝐮𝐤𝐤𝐚𝐧𝐠𝐚 🙈** ",
    " **𝐒𝐨𝐫𝐫𝐲 𝐕𝐢𝐬𝐚𝐫𝐢𝐤𝐤𝐢𝐭𝐮 ☹️** ",
    " **𝐔𝐧𝐧𝐚𝐢 𝐕𝐢𝐬𝐚𝐫𝐢𝐤𝐤𝐢𝐭𝐮 𝐓𝐡𝐚𝐧𝐝𝐡𝐢𝐯𝐢𝐭𝐭𝐮 🥺🥺** ",
    " **𝐕𝐞𝐥𝐚𝐢 𝐒𝐞𝐢𝐲𝐲𝐫𝐚𝐢𝐫𝐮👀** ",
    " **𝐇𝐚𝐥 𝐂𝐡𝐚𝐥 𝐄𝐩𝐩𝐚𝐝𝐢..? 🙂** ",
    " **𝐎𝐧𝐠𝐚𝐥 𝐕𝐢𝐭𝐭𝐮𝐊𝐤𝐮 𝐄𝐧𝐧𝐚 𝐈𝐫𝐮𝐤𝐤𝐮..?🤔** ",
    " **𝐂𝐡𝐚𝐭𝐭𝐢𝐧𝐠𝐮 𝐒𝐞𝐲𝐲𝐲𝐮 🥺** ",
    " **𝐍𝐚𝐌𝐚𝐤𝐤𝐮 𝐏𝐞𝐬𝐮𝐧𝐠𝐚 𝐏𝐥𝐬🥺🥺** ",
    " **𝐍𝐚𝐦𝐚𝐥 𝐏𝐚𝐫𝐭𝐲 𝐂𝐡𝐞𝐲𝐲𝐲𝐮 🤭** ",
    " **𝐍𝐚𝐦𝐦𝐚 𝐊𝐚𝐦𝐛𝐢𝐭𝐚𝐭𝐡𝐮 🤭** ",
]

VC_TAG = [
    "**𝐎𝐧𝐠𝐚 𝐕𝐂 𝐕𝐚𝐧𝐠𝐨 𝐏𝐥𝐬🥲**",
    "**𝐒𝐞𝐤𝐢𝐫𝐚𝐦 𝐉𝐨𝐢𝐧 𝐏𝐚𝐧𝐧𝐮 𝐈𝐦𝐩𝐨𝐫𝐭𝐚𝐧𝐭😬**",
    "**𝐉𝐨𝐢𝐧 𝐕𝐂 𝐒𝐨𝐨𝐧🏓**",
    "**𝐎𝐧𝐠𝐚 𝐕𝐂 𝐕𝐚𝐧𝐠𝐨 𝐉𝐢🥰**",
    "**𝐎𝐧𝐠𝐚𝐥𝐮𝐤𝐤𝐮 𝐄𝐝𝐡𝐚𝐯𝐚𝐦 𝐏𝐚𝐧𝐧𝐚 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐫𝐢𝐲𝐮?🤨**",
    "**𝐕𝐂 𝐉𝐨𝐢𝐧 𝐏𝐚𝐧𝐧𝐢𝐭𝐭𝐮 🤣**",
    "**𝐕𝐂 𝐉𝐨𝐢𝐧 𝐏𝐚𝐧𝐧𝐚𝐥𝐚𝐦😁**",
    "**𝐕𝐂 𝐉𝐨𝐢𝐧 𝐏𝐚𝐧𝐧𝐢 𝐂𝐡𝐞𝐜𝐤𝐮⚽**",
    "**𝐒𝐞𝐤𝐢𝐫𝐚𝐦 𝐉𝐨𝐢𝐧 𝐒𝐨𝐥𝐮🥺**",
    "**𝐒𝐨𝐫𝐫𝐲 𝐏𝐥𝐬 𝐉𝐨𝐢𝐧 😥**",
    "**𝐕𝐂 𝐉𝐨𝐢𝐧 𝐏𝐚𝐧𝐧𝐢𝐭𝐭𝐮 🤔**",
]


@app.on_message(filters.command(["tagall"], prefixes=["/", "@", ".", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER,
        ):
            is_admin = True
    if not is_admin:
        return await message.reply(
            "𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬. "
        )

    if message.reply_to_message and message.text:
        return await message.reply(
            "/tagall 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐅𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠..."
        )
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply(
                "/tagall 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐅𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠..."
            )
    else:
        return await message.reply(
            "/tagall 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐅𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠..."
        )
    if chat_id in spam_chats:
        return await message.reply(
            "𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐁𝐲 /tagalloff , /stopvctag ..."
        )
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}\n\n|| ➥ ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ » /stoptagall ||"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except BaseException:
        pass


@app.on_message(filters.command(["vctag"], prefixes=["/", ".", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER,
        ):
            is_admin = True
    if not is_admin:
        return await message.reply(
            "𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬. "
        )
    if chat_id in spam_chats:
        return await message.reply(
            "𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐁𝐲 /tagalloff , /stopvctag ..."
        )
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}\n\n|| ➥ ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ » /stopvctag ||"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except BaseException:
        pass


@app.on_message(
    filters.command(
        [
            "stoptagall",
            "canceltagall",
            "offtagall",
            "tagallstop",
            "stopvctag",
            "tagalloff",
        ]
    )
)
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠 𝐁𝐚𝐛𝐲.")
    is_admin = False
    try:
        participant = await client.get_chat_member(
            message.chat.id, message.from_user.id
        )
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER,
        ):
            is_admin = True
    if not is_admin:
        return await message.reply(
            "𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬."
        )
    else:
        try:
            spam_chats.remove(message.chat.id)
        except BaseException:
            pass
        return await message.reply("♦ 𝐒𝐭𝐨𝐩𝐩𝐞𝐝..♦")


__MODULE__ = "Sɪɴɢʟᴇ Tᴀɢ"
__HELP__ = """
**Tᴀɢ A Usᴇʀs Oɴᴇ Bʏ Oɴᴇ**

Tʜɪs ᴍᴏᴅᴜᴇ ᴀᴏᴡs ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀs ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴀ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ ᴏʀ VC.

Cᴏᴍᴍᴀɴᴅs:
- /ᴛᴀɢᴀ: Mᴇɴᴛɪᴏɴ ᴀ ᴍᴇᴍʙᴇʀs ᴏɴᴇ ʙʏ ᴏɴᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.
- /ᴠᴄᴛᴀɢ: Mᴇɴᴛɪᴏɴ ᴀ ᴍᴇᴍʙᴇʀs ᴏɴᴇ ʙʏ ᴏɴᴇ ғᴏʀ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.

Tᴏ sᴛᴏᴘ ᴛᴀɢɢɪɴɢ:
- /sᴛᴏᴘᴛᴀɢᴀ: Sᴛᴏᴘ ᴍᴇɴᴛɪᴏɴɪɴɢ ᴀ ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.
- /sᴛᴏᴘᴠᴄᴛᴀɢ: Sᴛᴏᴘ ᴍᴇɴᴛɪᴏɴɪɴɢ ᴀ ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.

Nᴏᴛᴇ:
- Oɴʏ ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs.
- Usᴇ /sᴛᴏᴘᴛᴀɢᴀ ᴏʀ /sᴛᴏᴘᴠᴄᴛᴀɢ ᴛᴏ sᴛᴏᴘ ᴛᴀɢɢɪɴɢ.
"""
