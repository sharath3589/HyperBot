from telegram import Update, Bot
from telegram.ext import run_async

from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot import dispatcher

from requests import get


@run_async
def ud(bot: Bot, update: Update):
    message = update.effective_message
    text = message.text[len("/ud ") :]
    results = get(f"http://api.urbandictionary.com/v0/define?term={text}").json()
    reply_text = f'Word: {text}\nDefinition: {results["list"][0]["definition"]}'
    message.reply_text(reply_text)


__help__ = """
 - /ud:{word} Type the word or expression you want to search use, like /ud telegram
"""

__mod_name__ = "Urban dictionary"

ud_handle = DisableAbleCommandHandler("ud", ud)

dispatcher.add_handler(ud_handle)
