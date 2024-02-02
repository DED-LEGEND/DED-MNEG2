# https://github.com/tinaarobot/YaeMiko
# https://github.com/tinaarobot 

# <============================================== IMPORTS =========================================================>
import asyncio
import contextlib
import importlib
import json
import re
import time
import traceback
from platform import python_version
from random import choice

import psutil
import pyrogram
import telegram
import telethon
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.error import (
    BadRequest,
    ChatMigrated,
    Forbidden,
    NetworkError,
    TelegramError,
    TimedOut,
)
from telegram.ext import (
    ApplicationHandlerStop,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from telegram.helpers import escape_markdown

import Database.sql.users_sql as sql
from Infamous.karma import *
from Mikobot import (
    BOT_NAME,
    LOGGER,
    OWNER_ID,
    SUPPORT_CHAT,
    TOKEN,
    StartTime,
    app,
    dispatcher,
    function,
    loop,
    tbot,
)
from Mikobot.plugins import ALL_MODULES
from Mikobot.plugins.helper_funcs.chat_status import is_user_admin
from Mikobot.plugins.helper_funcs.misc import paginate_modules

# <=======================================================================================================>

PYTHON_VERSION = python_version()
PTB_VERSION = telegram.__version__
PYROGRAM_VERSION = pyrogram.__version__
TELETHON_VERSION = telethon.__version__


# <============================================== FUNCTIONS =========================================================>
async def ai_handler_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query.data == "ai_handler":
        await query.answer()
        await query.message.edit_text(
            "💥 *ᴀʀᴛɪғɪᴄɪᴀʟ ɪɴᴛᴇʟʟɪɢᴇɴᴄᴇ ғᴜɴᴄᴛɪᴏɴs*\n\n"
            "✿ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ✿\n"
            "๏ /ask ➠ ᴀ ᴄʜᴀᴛʙᴏᴛ ᴜsɪɴɢ ɢᴘᴛ ғᴏʀ ʀᴇsᴘᴏɴᴅɪɴɢ ᴛᴏ ᴜsᴇʀ ǫᴜᴇʀɪᴇs.\n\n"
            "๏ /ai ➠ ᴘᴇʀғᴏʀᴍs ᴀ ᴘᴀʟᴍ sᴇᴀʀᴄʜ ᴜsɪɴɢ ᴀ ᴄʜᴀᴛʙᴏᴛ.\n\n"
            "๏ /upscale ➠ ᴜᴘsᴄᴀʟᴇs ʏᴏᴜʀ ɪᴍᴀɢᴇ ǫᴜᴀʟɪᴛʏ.",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "ɪᴍᴀɢᴇs ɢᴇɴ", callback_data="more_ai_handler"
                        ),
                        InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="Miko_back"),
                    ],
                ],
            ),
        )


async def more_ai_handler_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query.data == "more_ai_handler":
        await query.answer()
        await query.message.edit_text(
            "*✿ ʜᴇʀᴇ's ᴍᴏʀᴇ ɪᴍᴀɢᴇ ɢᴇɴ ᴄᴏᴍᴍᴀɴᴅs ✿*\n\n"
            "☼︎ ᴄᴏᴍᴍᴀɴᴅ ➛ /meinamix\n"
            "  ๏ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ ➠ ɢᴇɴᴇʀᴀᴛᴇs ᴀɴ ɪᴍᴀɢᴇ ᴜsɪɴɢ ᴛʜᴇ ᴍᴇɪɴᴀᴍɪx ᴍᴏᴅᴇʟ.\n\n"
            "☼︎ ᴄᴏᴍᴍᴀɴᴅ ➛ /darksushi\n"
            "  ๏ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ ➠ ɢᴇɴᴇʀᴀᴛᴇs ᴀɴ ɪᴍᴀɢᴇ ᴜsɪɴɢ ᴛʜᴇ ᴅᴀʀᴋsᴜsʜɪ ᴍᴏᴅᴇʟ.\n\n"
            "☼︎ ᴄᴏᴍᴍᴀɴᴅ ➛ /meinahentai\n"
            "  ๏ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ ➠ ɢᴇɴᴇʀᴀᴛᴇs ᴀɴ ɪᴍᴀɢᴇ ᴜsɪɴɢ ᴛʜᴇ ᴍᴇɪɴᴀʜᴇɴᴛᴀɪ ᴍᴏᴅᴇʟ.\n\n"
            "☼︎ ᴄᴏᴍᴍᴀɴᴅ ➛ /darksushimix\n"
            "  ๏ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ ➠ ɢᴇɴᴇʀᴀᴛᴇs ᴀɴ ɪᴍᴀɢᴇ ᴜsɪɴɢ ᴛʜᴇ ᴅᴀʀᴋsᴜsʜɪᴍɪx ᴍᴏᴅᴇʟ.\n\n"
            "☼︎ ᴄᴏᴍᴍᴀɴᴅ ➛ /anylora\n"
            "  ๏ Description ➠ ɢᴇɴᴇʀᴀᴛᴇs ᴀɴ ɪᴍᴀɢᴇ ᴜsɪɴɢ ᴛʜᴇ ᴀɴʏʟᴏʀᴀ ᴍᴏᴅᴇʟ.\n\n"
            "☼︎ ᴄᴏᴍᴍᴀɴᴅ ➛ /cetsumix\n"
            "  ๏ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ ➠ ɢᴇɴᴇʀᴀᴛᴇs ᴀɴ ɪᴍᴀɢᴇ ᴜsɪɴɢ ᴛʜᴇ ᴄᴇᴛᴜs-ᴍɪx ᴍᴏᴅᴇʟ.\n\n"
            "☼︎ ᴄᴏᴍᴍᴀɴᴅ ➛ /darkv2\n"
            "  ๏ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ ➠ ɢᴇɴᴇʀᴀᴛᴇs ᴀɴ ɪᴍᴀɢᴇ ᴜsɪɴɢ ᴛʜᴇ ᴅᴀʀᴋᴠ2 ᴍᴏᴅᴇʟ.\n\n"
            "☼︎ ᴄᴏᴍᴍᴀɴᴅ ➛ /creative\n"
            "  ๏ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ ➠ ɢᴇɴᴇʀᴀᴛᴇs ᴀɴ ɪᴍᴀɢᴇ ᴜsɪɴɢ ᴛʜᴇ ᴄʀᴇᴀᴛɪᴠᴇ ᴍᴏᴅᴇʟ.",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="ai_handler"),
                        InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/roy_editx"),
                    ],
                ],
            ),
        )


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


IMPORTED = {}
MIGRATEABLE = []
HELPABLE = {}
STATS = []
USER_INFO = []
DATA_IMPORT = []
DATA_EXPORT = []
CHAT_SETTINGS = {}
USER_SETTINGS = {}

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("Mikobot.plugins." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__

    if imported_module.__mod_name__.lower() not in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    else:
        raise Exception("ᴄᴀɴ'ᴛ ʜᴀᴠᴇ ᴛᴡᴏ ᴍᴏᴅᴜʟᴇs ᴡɪᴛʜ ᴛʜᴇ sᴀᴍᴇ ɴᴀᴍᴇ! ᴘʟᴇᴀsᴇ ᴄʜᴀɴɢᴇ ᴏɴᴇ")

    if hasattr(imported_module, "__help__") and imported_module.__help__:
        HELPABLE[imported_module.__mod_name__.lower()] = imported_module

    # Chats to migrate on chat_migrated events
    if hasattr(imported_module, "__migrate__"):
        MIGRATEABLE.append(imported_module)

    if hasattr(imported_module, "__stats__"):
        STATS.append(imported_module)

    if hasattr(imported_module, "__user_info__"):
        USER_INFO.append(imported_module)

    if hasattr(imported_module, "__import_data__"):
        DATA_IMPORT.append(imported_module)

    if hasattr(imported_module, "__export_data__"):
        DATA_EXPORT.append(imported_module)

    if hasattr(imported_module, "__chat_settings__"):
        CHAT_SETTINGS[imported_module.__mod_name__.lower()] = imported_module

    if hasattr(imported_module, "__user_settings__"):
        USER_SETTINGS[imported_module.__mod_name__.lower()] = imported_module


# do not async
async def send_help(chat_id, text, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    await dispatcher.bot.send_message(
        chat_id=chat_id,
        text=text,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=keyboard,
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    message = update.effective_message
    uptime = get_readable_time((time.time() - StartTime))
    if update.effective_chat.type == "private":
        if len(args) >= 1:
            if args[0].lower() == "help":
                await send_help(update.effective_chat.id, HELP_STRINGS)
            elif args[0].lower().startswith("ghelp_"):
                mod = args[0].lower().split("_", 1)[1]
                if not HELPABLE.get(mod, False):
                    return
                await send_help(
                    update.effective_chat.id,
                    HELPABLE[mod].__help__,
                    InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help_back")]]
                    ),
                )

            elif args[0].lower() == "markdownhelp":
                IMPORTED["exᴛʀᴀs"].markdown_help_sender(update)
            elif args[0].lower().startswith("stngs_"):
                match = re.match("stngs_(.*)", args[0].lower())
                chat = dispatcher.bot.getChat(match.group(1))

                if is_user_admin(chat, update.effective_user.id):
                    send_settings(match.group(1), update.effective_user.id, False)
                else:
                    send_settings(match.group(1), update.effective_user.id, True)

            elif args[0][1:].isdigit() and "rules" in IMPORTED:
                await IMPORTED["rules"].send_rules(update, args[0], from_pm=True)

        else:
            first_name = update.effective_user.first_name
            lol = await message.reply_photo(
                photo=str(choice(START_IMG)),
                caption=FIRST_PART_TEXT.format(escape_markdown(first_name)),
                parse_mode=ParseMode.MARKDOWN,
            )
            await asyncio.sleep(0.2)
            guu = await update.effective_message.reply_text("💌")
            await asyncio.sleep(1.8)
            await guu.delete()  # Await this line
            await update.effective_message.reply_text(
                PM_START_TEXT,
                reply_markup=InlineKeyboardMarkup(START_BTN),
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=False,
            )
    else:
        await message.reply_photo(
            photo=str(choice(START_IMG)),
            reply_markup=InlineKeyboardMarkup(GROUP_START_BTN),
            caption="<b>๏ ɪ ᴀᴍ ᴀʟɪᴠᴇ!</b>\n\n<b>๏ sɪɴᴄᴇ ➠ </b> <code>{}</code>".format(
                uptime
            ),
            parse_mode=ParseMode.HTML,
        )


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """๏ ʟᴏɢ ᴛʜᴇ ᴇʀʀᴏʀ ᴀɴᴅ sᴇɴᴅ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇssᴀɢᴇ ᴛᴏ ɴᴏᴛɪғʏ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ."""
    # Log the error before we do anything else, so we can see it even if something breaks.
    LOGGER.error(msg="๏ ᴇxᴄᴇᴘᴛɪᴏɴ ᴡʜɪʟᴇ ʜᴀɴᴅʟɪɴɢ ᴀɴ ᴜᴘᴅᴀᴛᴇ", exc_info=context.error)

    # traceback.format_exception returns the usual python message about an exception, but as a
    # list of strings rather than a single string, so we have to join them together.
    tb_list = traceback.format_exception(
        None, context.error, context.error.__traceback__
    )
    tb = "".join(tb_list)

    # Build the message with some markup and additional information about what happened.
    message = (
        "๏ ᴀɴ ᴇxᴄᴇᴘᴛɪᴏɴ ᴡᴀs ʀᴀɪsᴇᴅ ᴡʜɪʟᴇ ʜᴀɴᴅʟɪɴɢ ᴀɴ ᴜᴘᴅᴀᴛᴇ\n"
        "๏ <pre>ᴜᴘᴅᴀᴛᴇ = {}</pre>\n\n"
        "๏ <pre>{}</pre>"
    ).format(
        html.escape(json.dumps(update.to_dict(), indent=2, ensure_ascii=False)),
        html.escape(tb),
    )

    if len(message) >= 4096:
        message = message[:4096]
    # Finally, send the message
    await context.bot.send_message(
        chat_id=OWNER_ID, text=message, parse_mode=ParseMode.HTML
    )


# for test purposes
async def error_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    error = context.error
    try:
        raise error
    except Forbidden:
        print("no nono1")
        print(error)
        # remove update.message.chat_id from conversation list
    except BadRequest:
        print("no nono2")
        print("BadRequest caught")
        print(error)

        # handle malformed requests - read more below!
    except TimedOut:
        print("no nono3")
        # handle slow connection problems
    except NetworkError:
        print("no nono4")
        # handle other connection problems
    except ChatMigrated as err:
        print("no nono5")
        print(err)
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        print(error)
        # handle all other telegram related errors


async def help_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)

    print(query.message.chat.id)

    try:
        if mod_match:
            module = mod_match.group(1)
            text = (
                "᪥ *ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ ᴏғ* *{}* ᪥ \n".format(HELPABLE[module].__mod_name__)
                + HELPABLE[module].__help__
            )
            await query.message.edit_text(
                text=text,
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help_back")]]
                ),
            )

        elif prev_match:
            curr_page = int(prev_match.group(1))
            await query.message.edit_text(
                text=HELP_STRINGS,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(curr_page - 1, HELPABLE, "help")
                ),
            )

        elif next_match:
            next_page = int(next_match.group(1))
            await query.message.edit_text(
                text=HELP_STRINGS,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(next_page + 1, HELPABLE, "help")
                ),
            )

        elif back_match:
            await query.message.edit_text(
                text=HELP_STRINGS,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, HELPABLE, "help")
                ),
            )

        await context.bot.answer_callback_query(query.id)

    except BadRequest:
        pass


async def stats_back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query.data == "insider_":
        uptime = get_readable_time((time.time() - StartTime))
        cpu = psutil.cpu_percent(interval=0.5)
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent
        text = f"""
✽ sʏsᴛᴇᴍ sᴛᴀᴛᴇs ✽
⊰᯽⊱┈──╌❊╌──┈⊰᯽⊱

๏ ᴜᴘᴛɪᴍᴇ ➠ {uptime}
๏ ᴄᴘᴜ ➠ {cpu}%
๏ ʀᴀᴍ ➠ {mem}%
๏ ᴅɪsᴋ ➠ {disk}%
๏ ᴘʏᴛʜᴏɴ ➠ {PYTHON_VERSION}
๏ ᴘᴛʙ ➠ {PTB_VERSION}

๏ ᴛᴇʟᴇᴛʜᴏɴ ➠ {TELETHON_VERSION}
๏ ᴘʏʀᴏɢʀᴀᴍ ➠ {PYROGRAM_VERSION}
"""
        await query.answer(text=text, show_alert=True)


async def gitsource_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "git_source":
        source_link = "https://x-hd.video/video/-aubree-valentine-switch-roles-fta-reality-kings.html"
        message_text = (
            f"*✦ ᴍᴜsɪᴄ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs sᴇᴄᴛɪᴏɴ ✦* \n\n ๏ /play ➛ ᴘʟᴀʏ ᴀɴʏ sᴏɴɢ ᴏɴ ɢʀᴏᴜᴘ ᴠᴄ. \n ๏ /vplay ➛ ᴘʟᴀʏ ᴀɴʏ ᴠɪᴅᴇᴏ sᴏɴɢ ᴏɴ ɢʀᴏᴜᴘ ᴠᴄ. \n ๏ /cplay ➛ ᴘʟᴀʏ ᴀɴʏ sᴏɴɢ ɪɴ ᴄʜᴀɴɴᴇʟ ᴠᴄ\n ๏ /playlist ➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴀᴠᴇᴅ ᴘʟᴀʏʟɪsᴛ ᴏɴ sᴇʀᴠᴇʀ. \n ๏ /pause ➛ ᴩᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ. \n ๏ /resume ➛ ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴩᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ. \n ๏ /skip ➛ sᴋɪᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴀɴᴅ sᴛᴀʀᴛ sᴛʀᴇᴀᴍɪɴɢ ᴛʜᴇ ɴᴇxᴛ ᴛʀᴀᴄᴋ ɪɴ ǫᴜᴇᴜᴇ. \n ๏ /end  ➛ ᴄʟᴇᴀʀs ᴛʜᴇ ǫᴜᴇᴜᴇ ᴀɴᴅ ᴇɴᴅ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ. \n ๏ /player ➛ ɢᴇᴛ ᴀ ɪɴᴛᴇʀᴀᴄᴛɪᴠᴇ ᴩʟᴀʏᴇʀ ᴩᴀɴᴇʟ. \n ๏ /queue ➛ sʜᴏᴡs ᴛʜᴇ ǫᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋs ʟɪsᴛ."
        )

        # Adding the inline button
        keyboard = [[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="Miko_back")]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            message_text,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=False,
            reply_markup=reply_markup,
        )


async def repo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    source_link = "https://x-hd.video/video/-aubree-valentine-switch-roles-fta-reality-kings.html"
    message_text = f"*๏ ʜᴇʀᴇ ɪs ᴛʜᴇ ʟɪɴᴋ ғᴏʀ ᴛʜᴇ ғʀᴇᴇ ᴘᴏʀɴ sɪᴛᴇ*\n\n{source_link}"

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message_text,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=False,
    )


async def Miko_about_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query.data == "Miko_":
        uptime = get_readable_time((time.time() - StartTime))
        message_text = (
            f"๏ <b>ɪ ᴀᴍ ๛ᴡ ᴀ ᴀ ɴ ɪ ʏ ᴀ ⸙, ᴀɴᴅ ʜᴇʀᴇ ɪs ᴍʏ ᴀʟʟ ғᴇᴀᴛᴜʀᴇᴅ.</b>"
            f"\n\n๏ <b>ᴀɪ ɪɴᴛᴇɢʀᴀᴛɪᴏɴ.</b>"
            f"\n๏ <b>ᴀᴅᴠᴀɴᴄᴇ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ᴄᴀᴘᴀʙɪʟɪᴛʏ.</b>"
            f"\n๏ <b>ᴀɴɪᴍᴇ ʙᴏᴛ ғᴜɴᴄᴛɪᴏɴᴀʟɪᴛʏ.</b>"
            f"\n\n๏ <b>ᴜsᴇʀs</b> ➛ {sql.num_users()}"
            f"\n๏ <b>ᴄʜᴀᴛs</b> ➛ {sql.num_chats()}"
            f"\n\n๏ <b>ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʜᴇʟᴘ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ</b> {BOT_NAME}."
        )
        await query.message.edit_text(
            text=message_text,
            disable_web_page_preview=True,
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="sʏsᴛᴇᴍ sᴛᴀᴛs", callback_data="insider_"),
                    ],
                    [
                        InlineKeyboardButton(
                            text="sᴘᴀᴍ ʀᴀɪᴅ", callback_data="Miko_support"
                        ),
                        InlineKeyboardButton(text="ᴄᴏᴍᴍᴀɴᴅ", callback_data="help_back"),
                    ],
                    [
                        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="Miko_back"),
                    ],
                ]
            ),
        )
    elif query.data == "Miko_support":
        message_text = (
            "*✦ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs ᴏғ sᴘᴀᴍ, ʀᴀɪᴅ sᴇᴄᴛɪᴏɴ ✦ \n\n๏ ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ ๏\n\n֍ 𝗦𝗽𝗮𝗺 ➠ ๏ ꜱᴘᴀᴍꜱ ᴀ ᴍᴇꜱꜱᴀɢᴇ. ๏\n  ๛ /spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)\n  ๛ /spam <count> <replying any message>\n\n֍ 𝗣𝗼𝗿𝗻𝗦𝗽𝗮𝗺 ➠ ๏ ᴘᴏʀᴍᴏɢʀᴀᴘʜʏ ꜱᴘᴀᴍ. ๏\n  ๛ /pspam <count>\n\n֍ 𝗛𝗮𝗻𝗴 ➠ ๏ ꜱᴘᴀᴍꜱ ʜᴀɴɢɪɴɢ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ. ๏\n  ๛ /hang <counter>\n\n๏ ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ ๏\n\n֍ 𝗥𝗮𝗶𝗱 ➠ ๏ ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜꜱᴇʀ ꜰᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ. ๏\n  ๛ /raid <count> <username>\n  ๛ /raid <count> <reply to user>\n\n֍ 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱 ➠ ๏ ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ. ๏\n  ๛ /rraid <replying to user>\n  ๛ /rraid <username>\n\n֍ 𝗗𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱 ➠ ๏ ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ. ๏\n  ๛ /drraid <replying to user>\n  ๛ /drraid <username>\n\n֍ 𝐌𝐑𝐚𝐢𝐝 ➠ ๏ ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ. ๏\n  ๛ /mraid <count> <username>\n  ๛ /mraid <count> <reply to user>\n\n֍ 𝐒𝐑𝐚𝐢𝐝 ➠ ๏ ꜱʜᴀʏᴀʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ. ๏\n  ๛ /sraid <count> <username>\n  ๛ /sraid <count> <reply to user>\n\n֍ 𝐂𝐑𝐚𝐢𝐝 ➠ ๏ ᴀʙᴄᴅ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ. ๏\n  ๛ /craid <count> <username>\n  ๛ /craid <count> <reply to user>\n\n๏ ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ ๏\n\n֍ 𝗨𝘀𝗲𝗿𝗕𝗼𝘁 ➠ ๏ ᴜꜱᴇʀʙᴏᴛ ᴄᴍᴅꜱ ๏\n  ๛ /ping \n  ๛ /reboot\n  ๛ /sudo <reply to user>  ➛ Owner Cmd\n  ๛ /logs ➛ Owner Cmd\n\n֍ 𝗘𝗰𝗵𝗼 ➠ ๏ ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜꜱᴇʀ ๏\n  ๛ /echo <reply to user>\n  ๛ /rmecho <reply to user>\n\n֍ 𝗟𝗲𝗮𝘃𝗲 ➠ ๏ ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ๏\n  ๛ /leave <group/chat id>\n  ๛ /leave ➛ Type in the Group bot will auto leave that group*"
        )
        await query.message.edit_text(
            text=message_text,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"
                        ),
                        InlineKeyboardButton(
                            text="ᴏᴡɴᴇʀ", url=f"tg://user?id={OWNER_ID}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="Miko_"),
                    ],
                ]
            ),
        )
    elif query.data == "Miko_back":
        first_name = update.effective_user.first_name
        await query.message.edit_text(
            PM_START_TEXT.format(escape_markdown(first_name), BOT_NAME),
            reply_markup=InlineKeyboardMarkup(START_BTN),
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
        )


async def get_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat  # type: Optional[Chat]
    args = update.effective_message.text.split(None, 1)

    # ONLY send help in PM
    if chat.type != chat.PRIVATE:
        if len(args) >= 2 and any(args[1].lower() == x for x in HELPABLE):
            module = args[1].lower()
            await update.effective_message.reply_text(
                f"๏ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ɪɴ ᴘᴍ ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ ᴏғ {module.capitalize()}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="ʜᴇʟᴘ",
                                url="https://t.me/{}?start=ghelp_{}".format(
                                    context.bot.username, module
                                ),
                            )
                        ]
                    ]
                ),
            )
            return
        await update.effective_message.reply_text(
            "๏ ᴄʜᴏᴏsᴇ ᴀɴ ᴏᴘᴛɪᴏɴ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʜᴇʟᴘ.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ᴏᴘᴇɴ ɪɴ ᴘʀɪᴠᴀᴛᴇ",
                            url="https://t.me/{}?start=help".format(
                                context.bot.username
                            ),
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            text="ᴏᴘᴇɴ ʜᴇʀᴇ",
                            callback_data="help_back",
                        )
                    ],
                ]
            ),
        )
        return

    elif len(args) >= 2 and any(args[1].lower() == x for x in HELPABLE):
        module = args[1].lower()
        text = (
            "๏ ʜᴇʀᴇ ɪs ᴛʜᴇ ᴀᴠᴀɪʟᴀʙʟᴇ ʜᴇʟᴘ ғᴏʀ ᴛʜᴇ *{}* ᴍᴏᴅᴜʟᴇ\n".format(
                HELPABLE[module].__mod_name__
            )
            + HELPABLE[module].__help__
        )
        await send_help(
            chat.id,
            text,
            InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help_back")]]
            ),
        )

    else:
        await send_help(chat.id, HELP_STRINGS)


async def send_settings(chat_id, user_id, user=False):
    if user:
        if USER_SETTINGS:
            settings = "\n\n".join(
                "*{}*:\n{}".format(mod.__mod_name__, mod.__user_settings__(user_id))
                for mod in USER_SETTINGS.values()
            )
            await dispatcher.bot.send_message(
                user_id,
                "ᴛʜᴇsᴇ ᴀʀᴇ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ sᴇᴛᴛɪɴɢs:" + "\n\n" + settings,
                parse_mode=ParseMode.MARKDOWN,
            )

        else:
            await dispatcher.bot.send_message(
                user_id,
                "๏ sᴇᴇᴍs ʟɪᴋᴇ ᴛʜᴇʀᴇ ᴀʀᴇɴ'ᴛ ᴀɴʏ ᴜsᴇʀ sᴘᴇᴄɪғɪᴄ sᴇᴛᴛɪɴɢs ᴀᴠᴀɪʟᴀʙʟᴇ :'(",
                parse_mode=ParseMode.MARKDOWN,
            )
    else:
        if CHAT_SETTINGS:
            chat_name = dispatcher.bot.getChat(chat_id).title
            await dispatcher.bot.send_message(
                user_id,
                text="๏ ᴡʜɪᴄʜ ᴍᴏᴅᴜʟᴇ ᴡᴏᴜʟᴅ ʏᴏᴜ ʟɪᴋᴇ ᴛᴏ ᴄʜᴇᴄᴋ {}'s sᴇᴛᴛɪɴɢs ғᴏʀ?".format(
                    chat_name
                ),
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, CHAT_SETTINGS, "stngs", chat=chat_id)
                ),
            )
        else:
            await dispatcher.bot.send_message(
                user_id,
                "๏ sᴇᴇᴍs ʟɪᴋᴇ ᴛʜᴇʀᴇ ᴀʀᴇɴ'ᴛ ᴀɴʏ ᴄʜᴀᴛ sᴇᴛᴛɪɴɢs ᴀᴠᴀɪʟᴀʙʟᴇ :'(\n sᴇɴᴅ ᴛʜɪs "
                "๏ ɪɴ ᴀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ʏᴏᴜ'ʀᴇ ᴀᴅᴍɪɴ ɪɴ ᴛᴏ ғɪɴᴅ ɪᴛs ᴄᴜʀʀᴇɴᴛ sᴇᴛᴛɪɴɢs!",
                parse_mode=ParseMode.MARKDOWN,
            )


async def settings_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = update.effective_user
    bot = context.bot
    mod_match = re.match(r"stngs_module\((.+?),(.+?)\)", query.data)
    prev_match = re.match(r"stngs_prev\((.+?),(.+?)\)", query.data)
    next_match = re.match(r"stngs_next\((.+?),(.+?)\)", query.data)
    back_match = re.match(r"stngs_back\((.+?)\)", query.data)
    try:
        if mod_match:
            chat_id = mod_match.group(1)
            module = mod_match.group(2)
            chat = bot.get_chat(chat_id)
            text = "*{}* ʜᴀs ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ sᴇᴛᴛɪɴɢs ғᴏʀ ᴛʜᴇ *{}* ᴍᴏᴅᴜʟᴇ\n\n".format(
                escape_markdown(chat.title), CHAT_SETTINGS[module].__mod_name__
            ) + CHAT_SETTINGS[module].__chat_settings__(chat_id, user.id)
            await query.message.reply_text(
                text=text,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="ʙᴀᴄᴋ",
                                callback_data="stngs_back({})".format(chat_id),
                            )
                        ]
                    ]
                ),
            )

        elif prev_match:
            chat_id = prev_match.group(1)
            curr_page = int(prev_match.group(2))
            chat = bot.get_chat(chat_id)
            await query.message.reply_text(
                "๏ ʜᴇʏ ᴛʜᴇʀᴇ ! ᴛʜᴇʀᴇ ᴀʀᴇ ǫᴜɪᴛᴇ ᴀ ғᴇᴡ sᴇᴛᴛɪɴɢs ғᴏʀ {} - ɢᴏ ᴀʜᴇᴀᴅ ᴀɴᴅ ᴘɪᴄᴋ ᴡʜᴀᴛ "
                "๏ ʏᴏᴜ'ʀᴇ ɪɴᴛᴇʀᴇsᴛᴇᴅ ɪɴ.".format(chat.title),
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(
                        curr_page - 1, CHAT_SETTINGS, "stngs", chat=chat_id
                    )
                ),
            )

        elif next_match:
            chat_id = next_match.group(1)
            next_page = int(next_match.group(2))
            chat = bot.get_chat(chat_id)
            await query.message.reply_text(
                "๏ ʜᴇʏ ᴛʜᴇʀᴇ ! ᴛʜᴇʀᴇ ᴀʀᴇ ǫᴜɪᴛᴇ ᴀ ғᴇᴡ sᴇᴛᴛɪɴɢs ғᴏʀ {} - ɢᴏ ᴀʜᴇᴀᴅ ᴀɴᴅ ᴘɪᴄᴋ ᴡʜᴀᴛ "
                "๏ ʏᴏᴜ'ʀᴇ ɪɴᴛᴇʀᴇsᴛᴇᴅ ɪɴ.".format(chat.title),
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(
                        next_page + 1, CHAT_SETTINGS, "stngs", chat=chat_id
                    )
                ),
            )

        elif back_match:
            chat_id = back_match.group(1)
            chat = bot.get_chat(chat_id)
            await query.message.reply_text(
                text="๏ ʜᴇʏ ᴛʜᴇʀᴇ ! ᴛʜᴇʀᴇ ᴀʀᴇ ǫᴜɪᴛᴇ ᴀ ғᴇᴡ sᴇᴛᴛɪɴɢs ғᴏʀ {} - ɢᴏ ᴀʜᴇᴀᴅ ᴀɴᴅ ᴘɪᴄᴋ ᴡʜᴀᴛ "
                "๏ ʏᴏᴜ'ʀᴇ ɪɴᴛᴇʀᴇsᴛᴇᴅ ɪɴ".format(escape_markdown(chat.title)),
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, CHAT_SETTINGS, "stngs", chat=chat_id)
                ),
            )

        # ensure no spinny white circle
        bot.answer_callback_query(query.id)
        await query.message.delete()
    except BadRequest as excp:
        if excp.message not in [
            "๏ ᴍᴇssᴀɢᴇ ɪs ɴᴏᴛ ᴍᴏᴅɪғɪᴇᴅ",
            "Query_id_invalid",
            "๏ ᴍᴇssᴀɢᴇ ᴄᴀɴ'ᴛ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ",
        ]:
            LOGGER.exception("๏ ᴇxᴄᴇᴘᴛɪᴏɴ ɪɴ sᴇᴛᴛɪɴɢs ʙᴜᴛᴛᴏɴs. %s", str(query.data))


async def get_settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat  # type: Optional[Chat]
    user = update.effective_user  # type: Optional[User]
    msg = update.effective_message  # type: Optional[Message]

    # ONLY send settings in PM
    if chat.type != chat.PRIVATE:
        if is_user_admin(chat, user.id):
            text = "๏ ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ɢᴇᴛ ᴛʜɪs ᴄʜᴀᴛ sᴇᴛᴛɪɴɢs, ᴀs ᴡᴇʟʟ ᴀs ʏᴏᴜʀs."
            await msg.reply_text(
                text,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="sᴇᴛᴛɪɴɢs",
                                url="t.me/{}?start=stngs_{}".format(
                                    context.bot.username, chat.id
                                ),
                            )
                        ]
                    ]
                ),
            )
        else:
            text = "๏ ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴇᴛᴛɪɴɢs."

    else:
        await send_settings(chat.id, user.id, True)


async def migrate_chats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message  # type: Optional[Message]
    if msg.migrate_to_chat_id:
        old_chat = update.effective_chat.id
        new_chat = msg.migrate_to_chat_id
    elif msg.migrate_from_chat_id:
        old_chat = msg.migrate_from_chat_id
        new_chat = update.effective_chat.id
    else:
        return

    LOGGER.info("๏ ᴍɪɢʀᴀᴛɪɴɢ ғʀᴏᴍ %s, ᴛᴏ %s", str(old_chat), str(new_chat))
    for mod in MIGRATEABLE:
        with contextlib.suppress(KeyError, AttributeError):
            mod.__migrate__(old_chat, new_chat)

    LOGGER.info("๏ sᴜᴄᴄᴇssғᴜʟʟʏ ᴍɪɢʀᴀᴛᴇᴅ!")
    raise ApplicationHandlerStop


# <=======================================================================================================>


# <=================================================== MAIN ====================================================>
def main():
    function(CommandHandler("start", start))

    function(CommandHandler("help", get_help))
    function(CallbackQueryHandler(help_button, pattern=r"help_.*"))

    function(CommandHandler("settings", get_settings))
    function(CallbackQueryHandler(settings_button, pattern=r"stngs_"))
    function(CommandHandler("repo", repo))

    function(CallbackQueryHandler(Miko_about_callback, pattern=r"Miko_"))
    function(CallbackQueryHandler(gitsource_callback, pattern=r"git_source"))
    function(CallbackQueryHandler(stats_back, pattern=r"insider_"))
    function(CallbackQueryHandler(ai_handler_callback, pattern=r"ai_handler"))
    function(CallbackQueryHandler(more_ai_handler_callback, pattern=r"more_ai_handler"))
    function(MessageHandler(filters.StatusUpdate.MIGRATE, migrate_chats))

    dispatcher.add_error_handler(error_callback)

    LOGGER.info("๏ ɴʏᴋᴀᴀ ɪs sᴛᴀʀᴛɪɴɢ >> ᴜsɪɴɢ ʟᴏɴɢ ᴘᴏʟʟɪɴɢ.")
    dispatcher.run_polling(timeout=15, drop_pending_updates=True)


if __name__ == "__main__":
    try:
        LOGGER.info("๏ sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴏᴀᴅᴇᴅ ᴍᴏᴅᴜʟᴇs: " + str(ALL_MODULES))
        tbot.start(bot_token=TOKEN)
        app.start()
        main()
    except KeyboardInterrupt:
        pass
    except Exception:
        err = traceback.format_exc()
        LOGGER.info(err)
    finally:
        try:
            if loop.is_running():
                loop.stop()
        finally:
            loop.close()
        LOGGER.info(
            "------------------------ sᴛᴏᴘᴘᴇᴅ sᴇʀᴠɪᴄᴇs ------------------------"
        )
# <==================================================== END ===================================================>
