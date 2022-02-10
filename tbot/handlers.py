from telegram import Update
from telegram.ext import CallbackContext


def echo_handler(update: Update, context: CallbackContext):
    text = "Эхо работает " + update.effective_message.text
    context.bot.sendMessage(chat_id=update.effective_chat.id,
                            text=text)
