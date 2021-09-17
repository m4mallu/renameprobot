#-------------------------------------- https://github.com/m4mallu/renameprobot --------------------------------------#

import os

class Config(object):    
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")

    # Get these values from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID"))

    API_HASH = os.environ.get("API_HASH")

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    # Channels to forward the formatted video (Optional, Prefix: "-100", Bot should be an admin of the channels)
    CHANNEL1_ID = os.environ.get("CHANNEL1_ID")

    CHANNEL1_NAME = os.environ.get("CHANNEL1_NAME")

    CHANNEL2_ID = os.environ.get("CHANNEL2_ID")

    CHANNEL2_NAME = os.environ.get("CHANNEL2_NAME")

    CHANNEL3_ID = os.environ.get("CHANNEL3_ID")

    CHANNEL3_NAME = os.environ.get("CHANNEL3_NAME")

    CHANNEL4_ID = os.environ.get("CHANNEL4_ID")

    CHANNEL4_NAME = os.environ.get("CHANNEL4_NAME")

    CHANNEL5_ID = os.environ.get("CHANNEL5_ID")

    CHANNEL5_NAME = os.environ.get("CHANNEL5_NAME")
