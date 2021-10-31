import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "teamDlt_update")
BG_IMAGE = getenv("BG_IMAGE", "https://te.legra.ph/file/3f2d83ab6aaa71af4baae.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Somyajeet_Mishra")
OWNER_NAME = getenv("OWNER_NAME", "Somyajeet_Mishra")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "teamDlt")
PROJECT_NAME = getenv("PROJECT_NAME", "Pokimane-Music")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/somyajeet1/Pokimane-Music")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1976274592").split()))
