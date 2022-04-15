
from telegram.ext import  *
import api_key as key
import botResponse as rp

print ("Bot starts")

def start (update,context) :
    update.message.reply_text("ne var ?")
def  handle (update,context):
    text =str(update.message.text).lower()
    rsp =rp.salt_responses(text)
    update.message.reply_text(rsp)


def main ():
    updater = Updater(key.API_KEY,use_context=True)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(MessageHandler(Filters.text, handle))
    updater.start_polling(5)
    updater.idle()


main()