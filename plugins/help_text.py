#-------------------------------------- https://github.com/m4mallu/renameprobot --------------------------------------#

import logging
from pyrogram import Client, filters, StopPropagation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translation import Translation

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

@Client.on_message(filters.private & filters.command(['start', 'help']), group=0)
async def start(bot, update):
    me = await bot.get_me()
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.first_name, me.first_name),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("⚙️ Settings", callback_data="settings")]
            ])
    )
    await update.delete()
    raise StopPropagation()


async def bot_settings(bot, update):
    await bot.delete_messages(chat_id=update.message.chat.id, message_ids=update.message.message_id)
    await bot.send_message(
        chat_id=update.message.chat.id,
        text=Translation.SETTINGS_TEXT,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message.message_id,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("View Thumb", callback_data="view_thumb"),
                 InlineKeyboardButton("Del Thumb", callback_data="conf_thumb")],
                [InlineKeyboardButton("Help", callback_data="start_help"),
                 InlineKeyboardButton("Close", callback_data="close")]
            ])
    )


async def start_bot(bot, update):
    await bot.delete_messages(chat_id=update.message.chat.id, message_ids=update.message.message_id)
    me = await bot.get_me()
    await bot.send_message(
        chat_id=update.message.chat.id,
        text=Translation.START_TEXT.format(update.from_user.first_name, me.first_name),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("⚙️ Settings", callback_data="settings")]
            ])
    )
