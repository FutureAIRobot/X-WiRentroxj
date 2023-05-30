# 0AIB | 
from pyrogram import Client, __version__, enums

# from pyrogram.types import ParseMode

from Rentrox.config import Config, LOGGER

from Rentrox.user import User

class Bot(Client):

    USER: User = None

    USER_ID: int = None

    def __init__(self):

        super().__init__(

            session_name="rentrox",

            api_hash=Config.API_HASH,

            api_id=Config.API_ID,

            plugins={"root": "Rentrox/plugins"},

            workers=200,

            bot_token=Config.BOT_TOKEN

        )

        self.LOGGER = LOGGER

    async def start(self):

        await super().start()

        bot_details = await self.get_me()

        self.set_parse_mode(enums.ParseMode.HTML)

        self.LOGGER(__name__).info(

            f"@{bot_details.username} started! (Pyrogram {__version__})"

        )

        self.USER, self.USER_ID = await User().start()

    async def stop(self, *args):

        await super().stop()

        self.LOGGER(__name__).info("Bot stopped. Bye.")


