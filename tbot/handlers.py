from telegram import Update
from telegram.ext import CallbackContext


def echo_handler(update: Update, context: CallbackContext):
    context.bot.sendMessage(chat_id=update.effective_chat.id,
                            text=update.effective_message.text)
