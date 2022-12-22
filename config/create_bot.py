from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import exceptions
from loguru import logger
import configparser

try:
    config = configparser.ConfigParser()
    config.read("config.ini")
except FileNotFoundError:
    logger.critical("Не найден конфиг file")
    raise FileNotFoundError


try:
    storage = MemoryStorage()
    bot = Bot(token=config["aiogram"]["api_key"])
    app = Dispatcher(bot, storage=storage)
except exceptions.ValidationError:
    logger.error("Ivalid token")
    raise exceptions.ValidationError