import asyncio, os, random
from business_logic import parse_weather
from telegram import Bot, Update, Chat, StickerSet
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = Bot(token=TELEGRAM_TOKEN)


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update['message']['text'])
    possible_phrases = ["Да-да, я жив", 'А?...Что?', "Чо по репману"]
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text=random.choice(possible_phrases))

async def gachi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    stickers = await bot.get_sticker_set('Gachi_Memes')
    await context.bot.send_sticker(chat_id=update.effective_chat.id, 
                                   sticker=random.choice(stickers['stickers'])['file_id'])
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text='Куда ебать?')

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    metro = update['message']['text'].split()[1]
    await context.bot.send_message(chat_id=update.effective_chat.id,text=parse_weather(metro=metro.lower()))

def init_handlers():    
    handlers = (
        CommandHandler('ping', ping),
        CommandHandler('gachi', gachi),
        CommandHandler('weather',weather),
    )
    return handlers

if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    application.add_handlers(init_handlers())
    application.run_polling()
