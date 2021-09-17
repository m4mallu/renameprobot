
# [RenameProBot](https://github.com/m4mallu/renameprobot) 🤖

An Open Source ALL-In-One Telegram RoBot, that can do a lot of things.


## 💠 About :
An advanced telegram bot which performs the following functions differently.

### 1. File Formatting Functions 😍:

😍**Just give a required file name with supported extensions as a Reply to any telegram media will give the following
results in Bot.  
These functions can be done in a single download** 😍

- Custom Thumbnail Support
- File renaming.
- Converting to video.
- Extracting screenshots.
- Making duplicates of downloaded media in a Doc / Video formats.  
- Trimming streams from the downloaded media.

### 2. Copying medias to 5 different Chats 😍:
- **For this, bot must be an admin of the required chats(Channels / Groups with privileges)**  
- **Configuration Variables should be entered properly (Channel Names & IDs)**  
- **Don't forget to enter a prefix of '-100' to the channel / group IDs**

<br />

- Configure the var with required information
- Command ```/channel1``` to ```/channel5``` will set the default channel to copy medias to them.
- ```channel1``` is mandatory while the others are optionals.
- Command ```/view``` will give the default channel name.
- Command ```/list``` will give the list of current channels configured to the bot.
- Command ```/send``` will copy the replied media to the default channel.

## 💠 Advantage
- Doesn't need any repeated uploads & downloads for different operations 😉
- Can send the formatted media directly to 5 chats (configured in var) through ```/send``` command.
- **Finally:** If you are a movie channel admin, the bot is all yours 🥳

## 💠 Easy Way :

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/m4mallu/renameprobot)

## 💠 In linux Servers Or VPS:

### Create **config.py** with variables as given below

**An example `config.py` file could be:**

```
class Development(Config):
  APP_ID = "5531485"
  API_HASH = "eb064548abfb49dc3eeb1aeb98ae0f581e"
  TG_BOT_TOKEN = "6244445444:nhs6sgvhh6776gfnhsb4asas1aNbb"
  AUTH_USERS = [245588455, 246456588, 3452256266]
  CHANNEL1_ID = "-10013547554452"                            
  CHANNEL1_NAME = "My Channel"
  CHANNEL2_ID = "-1001554222221"
  CHANNEL2_NAME = "My Second Channel"
  CHANNEL3_ID = ""
  CHANNEL3_NAME = ""
  CHANNEL4_ID = ""
  CHANNEL4_NAME = ""
  CHANNEL5_ID = ""
  CHANNEL5_NAME = ""
```
```Channel_2``` ```Channel_3``` ```Channel_4``` ```Channel_5``` Parameters are Optionals, While the others are Mandatory. 

After creating the config file, open a terminal in the bot directory and run the following commands (Don' run as root !)

```
virtualenv -p python3 venv
. ./venv/bin/activate
pip3 install -r requirements.txt
python3 bot.py
```
## 💠 [@BotFather](https://telegram.dog/BotFather) Commands

```
start - Check if the Bot is Online
send  - send media to the defaul channel
view  - view the default channel name
list  - List the channels configured to the bot
channel1- set channel1 as default channel
channel2- set channel2 as default channel               (Optional)
channel3- set channel3 as default channel               (Optional)
channel4- set channel4 as default channel               (Optional)
channel5- set channel5 as default channel               (Optional)

```

## 💠 [LICENSE](https://choosealicense.com/licenses/gpl-3.0/)
- GPLv3

## 💠 Credits :
[SpEcHiDe](https://github.com/SpEcHiDe) for his [AnyDLBot](https://github.com/SpEcHiDe/AnyDLBot)

[DAN](https://t.me/haskell) for his [Pyrogram](https://github.com/pyrogram/pyrogram) Library

## 💠 Creator :

[Mallu Boy](https://t.me/m4mallu) In Telegram [AS](https://t.me/space4renjith)