#-------------------------------------- https://github.com/m4mallu/renameprobot --------------------------------------#

import os
import time
from pyrogram import Client, filters, StopPropagation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

from translation import Translation
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from helper.display_progress import progress_for_pyrogram
from plugins.help_text import bot_settings
from int import message1, input_file_name, replied_message


if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config

#-------------- Receives a Text message including filename with Extension replied to a Telegram Media ----------------#
@Client.on_message(filters.private & filters.text, group=1)
async def download_media(bot, update):
    if update.from_user.id not in Config.AUTH_USERS:
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a0 = await update.reply_text(text=Translation.NOT_AUTH_TXT)
        time.sleep(5)
        await a0.delete()
        await bot_settings(bot, update)
        raise StopPropagation()
    else:
        file_name = update.text
        extensions = Translation.EXTENSIONS
        if file_name.endswith(tuple(extensions)):
            if update.reply_to_message is not None:
                input_file_name[id] = file_name
                replied_message[id] = update.reply_to_message
                # ------------------ Asking for File Type Select Doc/Video ------------------#
                a = await bot.send_message(
                    text=Translation.FILE_TYPE_SELECT.format(file_name),
                    chat_id=update.chat.id,
                    reply_to_message_id=update.message_id,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton(text="📚Document", callback_data="rename_doc"),
                             InlineKeyboardButton("🎞Video", callback_data="convert_video")]
                        ])
                )
                message1[id] = a.message_id

#-------------------------------------- Renaming with Updated Text as Document ---------------------------------------#
async def rename_file(bot, update):
    await bot.delete_messages(chat_id=update.message.chat.id, message_ids=message1[id])
    description = Translation.CUSTOM_CAPTION_DOC
    thumb_image_path = os.getcwd() + "/" + "thumbnails" + "/" + str(update.from_user.id) + ".jpg"
    if not os.path.exists(thumb_image_path):
        thumb_image_path = None
    download_location = os.path.join(os.getcwd(), "downloads", str(update.message.chat.id))
    if not os.path.isdir(download_location):
        os.makedirs(download_location)
    dl_folder = [f for f in os.listdir(download_location)]
    for f in dl_folder:
        try:
            os.remove(os.path.join(download_location, f))
        except IndexError:
            pass
    saved_file_path = download_location + "/" + input_file_name[id].replace("_", " ")
    a = await bot.send_message(chat_id=update.message.chat.id, text=Translation.DOWNLOAD_START)
    c_time = time.time()
    try:
        await bot.download_media(
            message=replied_message[id],
            file_name=saved_file_path,
            progress=progress_for_pyrogram,
            progress_args=(
                Translation.DOWNLOAD_START,
                a,
                c_time
            )
        )
    except FloodWait as e:
        time.sleep(e.x)
    if saved_file_path is not None:
        await bot.edit_message_text(
            text=Translation.SAVED_RECVD_DOC_FILE,
            chat_id=update.message.chat.id,
            message_id=a.message_id
        )
        time.sleep(3)
        await bot.edit_message_text(
            chat_id=update.message.chat.id,
            text=Translation.UPLOAD_START,
            message_id=a.message_id
        )
        c_time = time.time()
        try:
            await bot.send_document(
                chat_id=update.message.chat.id,
                document=saved_file_path,
                thumb=thumb_image_path,
                caption=description,
                progress=progress_for_pyrogram,
                progress_args=(
                    Translation.UPLOAD_START,
                    a,
                    c_time
                )
            )
        except FloodWait as e:
            time.sleep(e.x)
        await a.delete()
        await bot.send_message(
            chat_id=update.message.chat.id,
            text=Translation.MAKE_A_COPY_TEXT,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("📘 Document", callback_data="d_copy"),
                     InlineKeyboardButton("🎞 Video", callback_data="v_copy")],
                    [InlineKeyboardButton(" Close", callback_data="clear_med")]
                ])
        )


#--------------------------------------- Renaming with Updated Text as Video -----------------------------------------#
async def convert_to_video(bot, update):
    await bot.delete_messages(chat_id=update.message.chat.id, message_ids=message1[id])
    thumb_image_path = os.getcwd() + "/" + "thumbnails" + "/" + str(update.from_user.id) + ".jpg"
    if not os.path.exists(thumb_image_path):
        thumb_image_path = None
    description = Translation.CUSTOM_CAPTION_VIDEO
    download_location = os.path.join(os.getcwd(), "downloads", str(update.message.chat.id))
    if not os.path.isdir(download_location):
        os.makedirs(download_location)
    dl_folder = [f for f in os.listdir(download_location)]
    for f in dl_folder:
        try:
            os.remove(os.path.join(download_location, f))
        except IndexError:
            pass
    saved_file_path = download_location + "/" + input_file_name[id].replace("_", " ")
    a = await bot.send_message(
        chat_id=update.message.chat.id,
        text=Translation.DOWNLOAD_START,
    )
    c_time = time.time()
    try:
        await bot.download_media(
            message=replied_message[id],
            file_name=saved_file_path,
            progress=progress_for_pyrogram,
            progress_args=(
                Translation.DOWNLOAD_START,
                a,
                c_time
            )
        )
    except FloodWait as e:
        time.sleep(e.x)
    if saved_file_path is not None:
        metadata = extractMetadata(createParser(saved_file_path))
        if metadata.has("duration"):
            duration = metadata.get('duration').seconds
            await bot.edit_message_text(
                text=Translation.SAVED_RECVD_DOC_FILE,
                chat_id=update.message.chat.id,
                message_id=a.message_id
            )
            time.sleep(5)
            await bot.edit_message_text(
                chat_id=update.message.chat.id,
                text=Translation.UPLOAD_START,
                message_id=a.message_id
            )
            c_time = time.time()
            try:
                await bot.send_video(
                    chat_id=update.message.chat.id,
                    video=saved_file_path,
                    duration=duration,
                    caption=description,
                    thumb=thumb_image_path,
                    supports_streaming=True,
                    progress=progress_for_pyrogram,
                    progress_args=(
                        Translation.UPLOAD_START,
                        a,
                        c_time
                    )
                )
            except FloodWait as e:
                time.sleep(e.x)
            await a.delete()
            await bot.send_message(
                chat_id=update.message.chat.id,
                text=Translation.MAKE_A_COPY_TEXT,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("📘 Document", callback_data="d_copy"),
                         InlineKeyboardButton("🎞 Video", callback_data="v_copy")],
                        [InlineKeyboardButton(" Close", callback_data="clear_med")]
                    ])
            )
