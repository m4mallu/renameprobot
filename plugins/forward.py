#-------------------------------------- https://github.com/m4mallu/renameprobot --------------------------------------#

import os
import time
import logging

from translation import Translation
from pyrogram import Client, filters
from int import channel, channel_name

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config

# ******************************** CONFIGURING DEFAULT SENDING CHANNEL USING COMMANDS *********************************#
@Client.on_message(filters.private & filters.command(["channel1"]))
async def channel1(bot, update):
    if update.from_user.id not in Config.AUTH_USERS:
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a = await update.reply_text(text=Translation.NOT_AUTH_TXT)
        time.sleep(5)
        await a.delete()
        return
    channel_id = Config.CHANNEL1_ID
    channel_string = Config.CHANNEL1_NAME
    if not channel_id:
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a = await bot.send_message(chat_id=update.chat.id, text=Translation.INVALID_CHANNEL)
        time.sleep(10)
        await a.delete()
    else:
        channel[id] = int(channel_id)
        channel_name[id] = str(channel_string)
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a = await bot.send_message(chat_id=update.chat.id,
                                   text=Translation.CHANNEL_CONFIRM.format(Config.CHANNEL1_NAME))
        time.sleep(5)
        await a.delete()


# ---------------------------------------------------------------------------------------------------------------------#
@Client.on_message(filters.private & filters.command(["channel2"]))
async def channel2(bot, update):
    if update.from_user.id not in Config.AUTH_USERS:
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a = await update.reply_text(text=Translation.NOT_AUTH_TXT)
        time.sleep(5)
        await a.delete()
        return
    channel_id = Config.CHANNEL2_ID
    channel_string = Config.CHANNEL2_NAME
    if not channel_id:
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a = await bot.send_message(chat_id=update.chat.id, text=Translation.INVALID_CHANNEL)
        time.sleep(10)
        await a.delete()
    else:
        channel[id] = int(channel_id)
        channel_name[id] = str(channel_string)
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a = await bot.send_message(chat_id=update.chat.id,
                                   text=Translation.CHANNEL_CONFIRM.format(Config.CHANNEL2_NAME))
        time.sleep(5)
        await a.delete()


# ---------------------------------------------------------------------------------------------------------------------#
@Client.on_message(filters.private & filters.command(["channel3"]))
async def channel3(bot, update):
    if update.from_user.id not in Config.AUTH_USERS:
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a = await update.reply_text(text=Translation.NOT_AUTH_TXT)
        time.sleep(5)
        await a.delete()
        return
    channel_id = Config.CHANNEL3_ID
    channel_string = Config.CHANNEL3_NAME
    if not channel_id:
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a = await bot.send_message(chat_id=update.chat.id, text=Translation.INVALID_CHANNEL)
        time.sleep(10)
        await a.delete()
    else:
        channel[id] = int(channel_id)
        channel_name[id] = str(channel_string)
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a = await bot.send_message(chat_id=update.chat.id,
                                   text=Translation.CHANNEL_CONFIRM.format(Config.CHANNEL3_NAME))
        time.sleep(5)
        await a.delete()


# ---------------------------------------------------------------------------------------------------------------------#
@Client.on_message(filters.private & filters.command(["channel4"]))
async def channel4(bot, update):
    if update.from_user.id not in Config.AUTH_USERS:
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a = await update.reply_text(text=Translation.NOT_AUTH_TXT)
        time.sleep(5)
        await a.delete()
        return
    channel_id = Config.CHANNEL4_ID
    channel_string = Config.CHANNEL4_NAME
    if not channel_id:
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a = await bot.send_message(chat_id=update.chat.id, text=Translation.INVALID_CHANNEL)
        time.sleep(10)
        await a.delete()
    else:
        channel[id] = int(channel_id)
        channel_name[id] = str(channel_string)
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a = await bot.send_message(chat_id=update.chat.id,
                                   text=Translation.CHANNEL_CONFIRM.format(Config.CHANNEL4_NAME))
        time.sleep(5)
        await a.delete()


# ---------------------------------------------------------------------------------------------------------------------#
@Client.on_message(filters.private & filters.command(["channel5"]))
async def channel5(bot, update):
    if update.from_user.id not in Config.AUTH_USERS:
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a = await update.reply_text(text=Translation.NOT_AUTH_TXT)
        time.sleep(5)
        await a.delete()
        return
    channel_id = Config.CHANNEL5_ID
    channel_string = Config.CHANNEL5_NAME
    if not channel_id:
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a = await bot.send_message(chat_id=update.chat.id, text=Translation.INVALID_CHANNEL)
        time.sleep(10)
        await a.delete()
    else:
        channel[id] = int(channel_id)
        channel_name[id] = str(channel_string)
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a = await bot.send_message(chat_id=update.chat.id,
                                   text=Translation.CHANNEL_CONFIRM.format(Config.CHANNEL5_NAME))
        time.sleep(5)
        await a.delete()


# *********************************** TO VIEW THE DEFAULT SENDING CHANNEL *********************************************#
@Client.on_message(filters.private & filters.command(["view"]))
async def view(bot, update):
    if update.from_user.id not in Config.AUTH_USERS:
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a = await update.reply_text(text=Translation.NOT_AUTH_TXT)
        time.sleep(5)
        await a.delete()
        return
    if (channel_name.keys()) and ("view" in update.text):
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a = await update.reply_text(Translation.INFO_CHANNEL.format(channel_name[id]))
        time.sleep(5)
        await a.delete()
    else:
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a = await update.reply_text(Translation.NO_DEFAULT_SET)
        time.sleep(5)
        await a.delete()

# ************************************** List All the channels attached to bot ****************************************#
@Client.on_message(filters.private & filters.command(["list"]))
async def list_channels(bot, update):
    if update.from_user.id not in Config.AUTH_USERS:
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a = await update.reply_text(text=Translation.NOT_AUTH_TXT)
        time.sleep(5)
        await a.delete()
        return
    else:
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a = await update.reply_text(text=Translation.LIST_CHANNELS.format(
            Config.CHANNEL1_ID, Config.CHANNEL1_NAME, Config.CHANNEL2_ID, Config.CHANNEL2_NAME, Config.CHANNEL3_ID,
            Config.CHANNEL3_NAME, Config.CHANNEL4_ID, Config.CHANNEL4_NAME, Config.CHANNEL5_ID, Config.CHANNEL5_NAME)
        )
        time.sleep(20)
        await a.delete()
# ************************************** SEND A FILE TO THE CONFIGURED CHANNEL ****************************************#
@Client.on_message(filters.private & filters.command(["send"]))
async def forward(bot, update):
    if update.from_user.id not in Config.AUTH_USERS:
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a = await update.reply_text(text=Translation.NOT_AUTH_TXT)
        time.sleep(5)
        await a.delete()
        return
    if update.reply_to_message is not None:
        if channel.keys():
            try:
                await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
                await bot.copy_message(chat_id=channel[id], from_chat_id=update.chat.id,
                                       message_id=update.reply_to_message.message_id)
                a = await update.reply_text(text=Translation.SUCCESSFUL_SEND.format(channel_name[id]),
                                            parse_mode='html', quote=True)
                time.sleep(5)
                await a.delete()
            except Exception:
                await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
                a = await update.reply_text(text=Translation.FORWARD_ERROR, parse_mode='html', quote=True)
                time.sleep(5)
                await a.delete()
        else:
            await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
            a = await update.reply_text(text=Translation.INVALID_CHANNEL)
            time.sleep(15)
            await a.delete()
    else:
        await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
        a = await update.reply_text(text=Translation.NOT_REPLIED_TO_MESSAGE)
        time.sleep(5)
        await a.delete()
