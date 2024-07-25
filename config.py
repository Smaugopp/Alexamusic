import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 24620300
API_HASH = "9a098f01aa56c836f2e34aee4b7ef963"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "6915408680:AAGcxq-eVClT3x8Kd2aNlrS0m0sCjnXjDgw"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://fidixi3663:w7rvlxmDd5lsX9ix@cluster0.0k1an50.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 2000))

# Chat id of a group for logging bot's activities
LOGGER_ID = -1002023182491

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = 6848223695

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/about-tosu/tosu",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/about_tosuu")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/nothing_bots_support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "6be9f0b34c384ad097cc71b1c1fc5e8b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "2607415f99944cc6b24fa98018fb8c09")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = "BQF3rQwACeq4VbYG8rcDxxmEJa5CYKD0Rwn6MhYQkbyr-ebhWyzDZACX0BbQ9nOAl_-jgLHZVldG4V2sXnwZkxl2vbACKXsag3i11c5Is1VCX_JMFzMJaXj_JJkSES7I94jeAh5dBgaCzxe5SJG9wb2cGt1DBfRf0Dp5FF78DpkPVIqKVFo1xrjKeGSNaBsBCcbHwUEk58MHPM6scBR1zkdpTgH1OHIczLJ_zAovhds9MjmxlkUlY9OgA0I0mZAHEcSZutejBppezpyhgj932RIszuTJzfDYb3WaN0hbGJVMsXU3oE-LZv5FvdhX8KQvWzGlQmQfYwg0wjIJE_vUI9Hx2mUQbwAAAAE1mGFGAA"
STRING2 = "BQF3rQwAHoNDkOSigDCKwLTkyCB-KJGa9imoFapd2Lf57oPjBzj02O9c1lZlXZbDTLgLy-sOKmfkSzyXv3saQLlGZKrG4gco8wPBZQoka-njc1sFslZZRTMtOtsg6JYypGmlZFr8TnEDj_uJv1dDIVJ-j2zJICU-ByQwpM5U0DcYssAZVU0WCNt6SVpGAYkFKDfvF3-0AF1jvY7qOr2ZqfpDGkLU3zGONs3MNtYSEsBcHYJBLkQ1fYA8SbIUKarD7Xjt4xs-zoFN_YCCcOK3mkRtMPO3WMXeTzQ96s4nhW_yCxjVAh41wSXDTmnpVmlBYXrF5RTTG1DVzu-0ejEKbXQkCEIC5AAAAAF6l3TOAA"
STRING3 = ""
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/322615e098b1592b8b0af.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/322615e098b1592b8b0af.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/322615e098b1592b8b0af.jpg"
STATS_IMG_URL = "https://graph.org/file/322615e098b1592b8b0af.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/322615e098b1592b8b0af.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/322615e098b1592b8b0af.jpg"
STREAM_IMG_URL = "https://graph.org/file/322615e098b1592b8b0af.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/322615e098b1592b8b0af.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/322615e098b1592b8b0af.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/322615e098b1592b8b0af.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/2829138cd6da27fcae483.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/2829138cd6da27fcae483.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
