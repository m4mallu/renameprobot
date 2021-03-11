#-------------------------------------- https://github.com/m4mallu/renameprobot --------------------------------------#

import os
import time
import shutil
import logging
from pyrogram.errors import FloodWait

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from translation import Translation
from helper.display_progress import progress_for_pyrogram

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

async def convert_to_doc_copy(bot, update):
    await bot.delete_messages(chat_id=update.message.chat.id, message_ids=update.message.message_id)
    saved_file_path = os.getcwd() + "/" + "downloads" + "/" + str(update.from_user.id) + "/"
    thumb_image_path = os.getcwd() + "/" + "thumbnails" + "/" + str(update.from_user.id) + ".jpg"
    description = Translation.CUSTOM_CAPTION_DOC
    if not os.path.exists(thumb_image_path):
        thumb_image_path = None
    for file in os.listdir(saved_file_path):
        dir_content = (os.path.join(saved_file_path, file))
        if dir_content is not None:
            a = await bot.send_message(
                chat_id=update.message.chat.id,
                text=Translation.UPLOAD_START,
                reply_to_message_id=update.message.message_id
            )
            c_time = time.time()
            try:
                await bot.send_document(
                    chat_id=update.message.chat.id,
                    document=dir_content,
                    thumb=thumb_image_path,
                    caption=description,
                    progress=progress_for_pyrogram,
                    progress_args=(
                        Translation.UPLOAD_START,
                        a,
                        c_time
                    )
                )
                await a.delete()
            except FloodWait as e:
                time.sleep(e.x)
            try:
                shutil.rmtree(saved_file_path)
            except Exception:
                pass


async def convert_to_video_copy(bot, update):
    await bot.delete_messages(chat_id=update.message.chat.id, message_ids=update.message.message_id)
    saved_file_path = os.getcwd() + "/" + "downloads" + "/" + str(update.from_user.id) + "/"
    thumb_image_path = os.getcwd() + "/" + "thumbnails" + "/" + str(update.from_user.id) + ".jpg"
    description = Translation.CUSTOM_CAPTION_VIDEO
    if not os.path.exists(thumb_image_path):
        thumb_image_path = None
    for file in os.listdir(saved_file_path):
        dir_content = (os.path.join(saved_file_path, file))
        if dir_content is not None:
            metadata = extractMetadata(createParser(dir_content))
            if metadata.has("duration"):
                duration = metadata.get('duration').seconds
                b = await bot.send_message(
                    chat_id=update.message.chat.id,
                    text=Translation.UPLOAD_START,
                    reply_to_message_id=update.message.message_id
                )
                c_time = time.time()
                try:
                    await bot.send_video(
                        chat_id=update.message.chat.id,
                        video=dir_content,
                        duration=duration,
                        caption=description,
                        thumb=thumb_image_path,
                        supports_streaming=True,
                        progress=progress_for_pyrogram,
                        progress_args=(
                            Translation.UPLOAD_START,
                            b,
                            c_time
                        )
                    )
                    await b.delete()
                except FloodWait as e:
                    time.sleep(e.x)
                try:
                    shutil.rmtree(saved_file_path)
                except Exception:
                    pass


async def clear_media(bot, update):
    await bot.delete_messages(chat_id=update.message.chat.id, message_ids=update.message.message_id)
    saved_file_path = os.getcwd() + "/" + "downloads" + "/" + str(update.from_user.id) + "/"
    try:
        shutil.rmtree(saved_file_path)
    except Exception:
        pass
