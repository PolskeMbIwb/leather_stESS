import logging
import os

from telegram.ext import ApplicationBuilder, CommandHandler

from commands import (async_gachi,
                      async_ping)


if bool(os.getenv('DEBUG') in ('True', '1')):
    logging.basicConfig(level=logging.INFO)
elif bool(os.getenv('DEBUG') in ('False', '0')):
    logging.basicConfig(level=logging.WARNING)
else:
    raise Exception('INVALID DEBUG MODE PASSED')


def init_handlers() -> tuple[CommandHandler]:
    handlers = (
        CommandHandler('ping', async_ping),
        CommandHandler('gachi', async_gachi),
    )
    return handlers


if __name__ == '__main__':
    application = ApplicationBuilder().token(
        os.getenv('TELEGRAM_TOKEN')
    ).build()
    application.add_handlers(init_handlers())
    application.run_polling()
