import asyncio, os, random
from telegram import Bot, Update, Chat, StickerSet
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = Bot(token=TELEGRAM_TOKEN)


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    possible_phrases = ["Да-да, я жив", 'А?...Что?', "Чо по репману"]
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text=random.choice(possible_phrases))

async def gachi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    stickers = await bot.get_sticker_set('Gachi_Memes')
    await context.bot.send_sticker(chat_id=update.effective_chat.id, 
                                   sticker=random.choice(stickers['stickers'])['file_id'])
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text='Куда ебать?')


def init_handlers() -> tuple[CommandHandler]:
    handlers = (
        CommandHandler('ping', ping),
        CommandHandler('gachi', gachi),
    )
    return handlers

if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    application.add_handlers(init_handlers())
    application.run_polling()
