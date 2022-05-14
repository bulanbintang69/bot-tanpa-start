# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url = f'https://t.me/RestAreaDewasa')
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴛᴜᴛᴏʀɪᴀʟ ᴘᴀᴋᴀɪ ʙᴏᴛ", url = f'https://t.me/+LRYn18fCDz4yYzcx'),
            ],
            [
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url = f'https://t.me/RestAreaDewasa')
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴛᴜᴛᴏʀɪᴀʟ ᴘᴀᴋᴀɪ ʙᴏᴛ", url = f'https://t.me/+LRYn18fCDz4yYzcx'),
            ],
            [
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url = f'https://t.me/RestAreaDewasa')
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴛᴜᴛᴏʀɪᴀʟ ᴘᴀᴋᴀɪ ʙᴏᴛ", url = f'https://t.me/+LRYn18fCDz4yYzcx'),
            ],
            [
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url = f'https://t.me/RestAreaDewasa')
            ],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ɢᴀʙᴜɴɢ ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="ᴛᴜᴛᴏʀɪᴀʟ ᴘᴀᴋᴀɪ ʙᴏᴛ", url = f'https://t.me/+LRYn18fCDz4yYzcx'),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴅᴀᴘᴀᴛᴋᴀɴ ꜰɪʟᴇ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="ᴛᴜᴛᴏʀɪᴀʟ ᴘᴀᴋᴀɪ ʙᴏᴛ", url = f'https://t.me/+LRYn18fCDz4yYzcx'),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴅᴀᴘᴀᴛᴋᴀɴ ꜰɪʟᴇ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ɢᴀʙᴜɴɢ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
                InlineKeyboardButton(text="ɢᴀʙᴜɴɢ ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="ᴛᴜᴛᴏʀɪᴀʟ ᴘᴀᴋᴀɪ ʙᴏᴛ", url = f'https://t.me/+LRYn18fCDz4yYzcx'),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴅᴀᴘᴀᴛᴋᴀɴ ꜰɪʟᴇ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
