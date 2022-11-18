import datetime
import pytz
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram.ext.jobqueue import JobQueue

from sensitiveData import botToken, test_group_chat_id
from main import createMenusMessage
updater = Updater(botToken, use_context=True)


def start(update, context):
    print("Start called")
    # context.job_queue.run_daily(msg_spam,
    #                             datetime.time(hour=18, minute=28, tzinfo=pytz.timezone('Europe/Stockholm')),
    #                             days=(0, 1, 2, 3, 4, 5, 6))

    context.job_queue.run_repeating(msg_spam, interval=60)
    context.bot.send_message(chat_id=update.message.chat_id, text='Service started!')


def msg(context):
    context.bot.send_message(chat_id=context.job.context, text='text')


def msg_spam(context):
    print("msg_Spam called")
    msg = createMenusMessage()
    context.bot.send_message(chat_id=test_group_chat_id, text=msg)


def error(update, context):
    """Log Errors caused by Updates."""
    print("Update ", update, " caused error", context.error)


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


def main():
    updater = Updater(botToken, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start, pass_job_queue=True))
    dp.add_error_handler(error)

    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))  # Filters out unknown commands

    # Filters out unknown messages.
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
