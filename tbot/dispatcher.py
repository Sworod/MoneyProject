from telegram.ext import Updater, MessageHandler, Filters

from MoneyProj.settings import TELEGRAM_TOKEN
from telegram import Bot, Update, BotCommand
import logging

from tbot.handlers import echo_handler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def setup_dispatcher(dispatcher):
    "Adding handlers"
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo_handler))


def run_pooling():
    """ Run bot in pooling mode """
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    dp = updater.dispatcher
    dp = setup_dispatcher(dp)

    bot_info = Bot(TELEGRAM_TOKEN).get_me()
    bot_link = f"https://t.me/" + bot_info["username"]

    logging.info(f"Pooling of '{bot_link}' started")
    # it is really useful to send '👋' emoji to developer
    # when you run local test
    # bot.send_message(text='👋', chat_id=<YOUR TELEGRAM ID>)

    updater.start_polling()
    updater.idle()
