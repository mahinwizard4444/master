import os
import time

import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]
# To save user details (userfull for getting user info & total user count)
# May reduce filter capacity
# Give Yes or No
SAVE_USER = os.environ.get("SAVE_USER", "no").lower()

# To check dyno status
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")

# Optional - To set alternative Bot Commands.
ADD_FILTER_CMD = os.environ.get("ADD_FILTER_CMD", "add")
DELETE_FILTER_CMD = os.environ.get("DELETE_FILTER_CMDD", "del")
DELETE_ALL_CMD = os.environ.get("DELETE_ALL_CMDD", "delall")
CONNECT_COMMAND = os.environ.get("CONNECT_COMMANDD", "connect")
DISCONNECT_COMMAND = os.environ.get("DISCONNECT_COMMANDD", "disconnect")


# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# To record the start Time of the Bot.
BOT_START_TIME = time.time()

# Messages
default_start_msg = """
**Hi {}, I'm Media Search Bot or ypu can call me as Auto-Filter Bot**
Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
