from typing import Union
import logging
import os
import random
import json
import yaml

from telegram import Bot, Update
from telegram.error import TelegramError
from telegram.ext import ContextTypes, CommandHandler


bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
logger = logging.getLogger('BOT')
BASE_DIR = os.getcwd()


with open(f'{BASE_DIR}/bot_core/utils/commands_msg_texts.yaml',
          mode='r') as phr_f:
    PHRASES: dict = yaml.safe_load(phr_f)


with open(f'{BASE_DIR}/bot_core/cache/gachi_stickers.json',
          mode='r') as f:
    STICKERS_CACHE: dict = json.load(f)


def __prepare_command_msg(
            command_name: str,
            localization: str = os.getenv("LOCALIZATION", 'en')
        ) -> Union[str, dict]:
    return PHRASES[command_name][localization]


async def async_ping(update: Update,
                     context: ContextTypes.DEFAULT_TYPE,
                     command_name: str = "ping") -> None:
    logger.info('PING COMMAND TRIGGERED')
    possible_phrases = random.choice(__prepare_command_msg(command_name))
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=possible_phrases
    )


async def async_gachi(update: Update,
                      context: ContextTypes.DEFAULT_TYPE,
                      command_name: str = "gachi") -> None:
    logger.info('GACHI COMMAND TRIGGERED')
    try:
        stickers = await bot.get_sticker_set('Gachi_Memes')
    except TelegramError:
        logger.warning('NO GACHI MEMES STICKER SET. USING CACHED')
        stickers = STICKERS_CACHE

    await context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker=random.choice(stickers['stickers'])['file_id'])

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="".join(__prepare_command_msg(command_name)))


def init_handlers() -> tuple[CommandHandler]:
    handlers = (
        CommandHandler('ping', async_ping),
        CommandHandler('gachi', async_gachi),
    )
    return handlers
