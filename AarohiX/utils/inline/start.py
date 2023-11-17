from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AarohiX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ [👑ᴘᴀʀᴛʜ👑‍] 🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❣️ʜᴇʟᴩ❣️",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="❤‍🔥sᴇᴛᴛɪɴɢs❤‍🔥", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💖 ғᴇᴇʟɪɴɢs 💖", url=f"https://t.me/Diloo_Ki_Dhadkan"),
            InlineKeyboardButton(
                text="🥰 ᴍʏ ʟɪғᴇʟɪɴᴇ[❣️] 🥰", url=f"https://t.me/ishqfeelings"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💝ᴍᴀɪɴᴛᴀɪɴᴇʀ[ᴘᴀʀᴛʜ]💝", user_id=OWNER),
            InlineKeyboardButton(
                text="🥰sᴜᴩᴩᴏʀᴛ[ᴘᴀʀᴛʜ]🥰", url=config.SUPPORT_GROUP
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ [💞ᴘᴀʀᴛʜ💞]🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥺ʜᴇʟᴩ🥺", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💖 ғᴇᴇʟɪɴɢs 💖", url=f"https://t.me/ishqfeelings"),
            InlineKeyboardButton(
                text="🥰 ᴍʏ ʟɪғᴇʟɪɴᴇ[❣️] 🥰", url=f"https://t.me/Diloo_Ki_Dhadkan"
            ),
        ],
        [
            InlineKeyboardButton(text="💝ᴍᴀɪɴᴛᴀɪɴᴇʀ[ᴘᴀʀᴛʜ]💝", user_id=OWNER),
            InlineKeyboardButton(
                text="🥰sᴜᴩᴩᴏʀᴛ[ᴘᴀʀᴛʜ]🥰", url=config.SUPPORT_GROUP
            ),
        ],
        [
            InlineKeyboardButton(
                    text="🥺 ᴏᴡɴᴇʀ 🥺", url=f"https://THE_KING_PARTH"
                )
        ],
     ]
    return buttons
