import logging

# MongoDB settings
MONGODB_URI = "mongodb://sopromatsila:AloFGYYqJ5BRWiaO@<IP_ADDRESS>:27017/HiParcelDB?retryWrites=true&w=majority"
DATABASE_NAME = "HiParcelDB"

# Telegram Bot API Token
TOKEN = "7421368757:AAF1kcT1SSuvdqXOn-5uhGObCHho_HBrpTM"

# Logging settings
LOGGING_LEVEL = "DEBUG"
LOG_FILE_PATH = "bot.log"

logging.basicConfig(level=LOGGING_LEVEL, filename=LOG_FILE_PATH, filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')