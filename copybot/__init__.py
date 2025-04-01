import logging
import logging.config
import os
import re

from dotenv import load_dotenv

load_dotenv(override=True)

pattern = re.compile(r"^.\d+$")

# vars
APP_ID = int(os.environ.get("APP_ID", "24010108"))
API_HASH = os.environ.get("API_HASH", "8d89700b2fc09a3aa6c906cbed65b040")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5580813031:AAHbEdD_g1MwYozWxEJdi3EIl5YwkMa1pvY")
OWNER_ID = int(os.environ.get("OWNER_ID", "6936727037"))
SESSION = os.environ.get("SESSION", "")
ADMINS = [
    int(user) if pattern.search(user) else user
    for user in os.environ.get("ADMINS", "").split()
] + [OWNER_ID]


# logging Conf
logging.config.fileConfig(fname="config.ini", disable_existing_loggers=False)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
