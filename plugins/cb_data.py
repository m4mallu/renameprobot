#-------------------------------------- https://github.com/m4mallu/renameprobot --------------------------------------#

from plugins.help_text import start_bot, bot_settings
from plugins.sub_functions import view_thumbnail, delete_thumbnail, del_thumb_confirm, close_button
from plugins.multimedia import rename_file, convert_to_video
from plugins.make_another_copy import convert_to_doc_copy, convert_to_video_copy, clear_media
from pyrogram import Client


@Client.on_callback_query()
async def catch_youtube_fmtid(bot, update):
    cb_data = update.data
    if "close" in cb_data:
        await close_button(bot, update)
    elif "view_thumb" in cb_data:
        await view_thumbnail(bot, update)
    elif "del_thumb" in cb_data:
        await delete_thumbnail(bot, update)
    elif "conf_thumb" in cb_data:
        await del_thumb_confirm(bot, update)
    elif "start_help" in cb_data:
        await start_bot(bot, update)
    elif "settings" in cb_data:
        await bot_settings(bot, update)
    elif "rename_doc" in cb_data:
        await rename_file(bot, update)
    elif "convert_video" in cb_data:
        await convert_to_video(bot, update)
    elif "d_copy" in cb_data:
        await convert_to_doc_copy(bot, update)
    elif "v_copy" in cb_data:
        await convert_to_video_copy(bot, update)
    elif "clear_med" in cb_data:
        await clear_media(bot, update)
