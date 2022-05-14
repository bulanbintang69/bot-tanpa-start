# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import CHANNEL, GROUP, OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"✥ ᴏᴡɴᴇᴛ ʙᴏᴛ : @wibusultan\n\n\nɪɴꜰᴏ ʟᴇʙɪʜ ʟᴀɴᴊᴜᴛ ꜱᴇᴘᴜᴛᴀʀ ʙᴏᴛ ꜱɪʟᴀʜᴋᴀɴ ʜᴜʙᴜɴɢɪ ᴀᴅᴍɪɴ/ᴏᴡɴᴇʀ.",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url = f'https://t.me/RestAreaDewasa')
                    ],
                    [
                        InlineKeyboardButton("ɢʀᴏᴜᴘ", url = f'https://t.me/RestAreaGroup')
                    ]
                ]
            ),
        )
