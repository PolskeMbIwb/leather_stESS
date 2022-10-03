import logging
import os
import random

from telegram import Bot, Update
from telegram.error import TelegramError
from telegram.ext import ContextTypes

bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
logger = logging.getLogger('BOT')


async def async_ping(update: Update,
                     context: ContextTypes.DEFAULT_TYPE):
    logger.info('PING COMMAND TRIGGERED')
    possible_phrases = ["Да-да, я жив", 'А?...Что?', "Чо по репману"]
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=random.choice(
                                        possible_phrases
                                   ))


async def async_gachi(update: Update,
                      context: ContextTypes.DEFAULT_TYPE):
    logger.info('GACHI COMMAND TRIGGERED')
    try:
        stickers = await bot.get_sticker_set('Gachi_Memes')
    except TelegramError:
        logger.warning('NO GACHI MEMES STICKER SET. USING CACHED')
        stickers = []
    await context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker=random.choice(stickers['stickers'])['file_id'])
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Куда любить?')
