# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://graph.org/file/f86b71018196c5cfe7344.jpg",
    "https://graph.org/file/a3db9af88f25bb1b99325.jpg",
    "https://graph.org/file/5b344a55f3d5199b63fa5.jpg",
    "https://graph.org/file/84de4b440300297a8ecb3.jpg",
    "https://graph.org/file/84e84ff778b045879d24f.jpg",
    "https://graph.org/file/a4a8f0e5c0e6b18249ffc.jpg",
    "https://graph.org/file/ed92cada78099c9c3a4f7.jpg",
    "https://graph.org/file/d6360613d0fa7a9d2f90b.jpg",
]

HEY_IMG = "https://telegra.ph/file/a2e224ca5309a2c544393.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph//file/f9e2b9cdd9324fc39970a.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/c4c2759c5fc04cefd207a.mp4",
    "https://telegra.ph//file/b1fa6609b1c4807255927.mp4",
    "https://telegra.ph//file/f3c7147da6511fbe27c25.mp4",
    "https://telegra.ph//file/39071b73c02e3ff5945ca.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/6efdd8e28756bc2f6e53e.mp4",
]

BAN_GIFS = [
    "https://telegra.ph//file/85ac1ab12c833afa1a5dd.mp4",
]


KICK_GIFS = [
    "https://telegra.ph//file/79a6c527e6e6d530bcdc8.mp4",
]


MUTE_GIFS = [
    "https://telegra.ph//file/b4faf6e390d72d286abdf.mp4",
]

FIRST_PART_TEXT = "๏ *ʜᴇʏ* `{}`, ᴡᴇʟᴄᴏᴍᴇ !\n━━━━━━━━━━━━━━━━━━━━━━━━"

PM_START_TEXT = "๏ *ɪ ᴀᴍ ๛ᴡ ᴀ ᴀ ɴ ɪ ʏ ᴀ ⸙ ᴀɴᴅ ɪ ʜᴀᴠᴇ sᴘᴇᴄɪᴀʟ ғᴇᴀᴛᴜʀᴇs.\n\n๏ ɪ ᴀᴍ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟʟ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ + ᴍᴜsɪᴄ ʙᴏᴛ.*"


START_BTN = [
    [
        InlineKeyboardButton(
            text=" ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/roy_editx"),
        InlineKeyboardButton(text="ᴍᴜsɪᴄ", callback_data="git_source"),
    ],
    [
        InlineKeyboardButton(text="sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url=f"https://x-hd.video/video/-aubree-valentine-switch-roles-fta-reality-kings.html"),
    ],
    [
        InlineKeyboardButton(text="ᴇxᴛʀᴀ", callback_data="Miko_"),
        InlineKeyboardButton(text="ᴄʜᴀᴛ ᴀɪ", callback_data="ai_handler"),
    ],
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅ", callback_data="help_back"),
    ],
    
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text=" ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="ᴏᴡɴᴇʀ", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="ᴜᴘᴅᴀᴛᴇs", url="https://t.me/roy_editx"),
        ib(text="sᴜᴘᴘᴏʀᴛ", url="https://t.me/the_friendz"),
    ],
    [
        ib(
            text=" ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
๏ *ʜᴇʏ, ɪ ᴀᴍ ๛ᴡ ᴀ ᴀ ɴ ɪ ʏ ᴀ ⸙* 

๏ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ ➠ /
"""
