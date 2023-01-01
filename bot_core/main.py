import logging
import os
import sys

from telegram.ext import ApplicationBuilder

from utils.commands import init_handlers


LOGGER_FORMAT = '[%(asctime)s][%()s] -- %(message)s'
DEBUG_MODE = os.getenv('DEBUG', 'True')

if DEBUG_MODE in ('True', '1'):
    logging.basicConfig(
        level=logging.INFO,
        # format=LOGGER_FORMAT,
    )

elif DEBUG_MODE in ('False', '0'):
    logging.basicConfig(
        level=logging.WARNING,
        # format=LOGGER_FORMAT,
    )

else:
    logging.error(f'INVALID DEBUG MODE PASSED. PASSED: {DEBUG_MODE}')
    sys.exit(1)


if __name__ == '__main__':
    try:
        token = os.environ.get('TELEGRAM_TOKEN')
    except Exception:
        logging.error("NO TOKEN DATA PASSED")
        sys.exit(1)

    application = ApplicationBuilder().token(token).build()
    application.add_handlers(init_handlers())
    application.run_polling()
