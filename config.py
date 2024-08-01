import os
import sys

import loguru
import pretty_errors
from aiogram import Bot
from aiogram.dispatcher.dispatcher import Dispatcher

TOKEN = os.getenv("FTB_TOKEN")
log_file = "logs/FTB.log"

bot = Bot(TOKEN)
dp = Dispatcher()

whitelist = ["1660218648"]

monthes = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

logger = loguru.logger

logger.level("DEBUG", color="<green>")
logger.level("INFO", color="<cyan>")
logger.level("WARNING", color="<yellow>")
logger.level("CRITICAL", color="<red>")

logger.add(
    log_file,
    level="DEBUG",
    rotation="1000 MB",
    retention="31 days",
    backtrace=True,
    diagnose=True,
)

