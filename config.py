import os

API_ID = API_ID = 23031620

API_HASH = os.environ.get("API_HASH", "31cb00c1cbe580394778b43105864bca")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7083457174:AAGexgaWlR-eB8Rz1QHPzlogzy7hvELkr_s")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 502980590))

LOG = -1002080964342

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "502980590").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


