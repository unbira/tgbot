import logging
import os
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Load environment variables from .env if present
load_dotenv()

# Telegram bot token
TOKEN = "8191580486:AAF3ZukswhUIpp1BeWLQiJ_Z9Q6Nd18O6s4"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    """Send a message with three buttons when the command /start is issued."""
    keyboard = [
        [
            InlineKeyboardButton("\u0415\u0421\u042d\u0414", callback_data="esed"),
            InlineKeyboardButton("\u0413\u0418\u0421\u041e\u0413\u0414 \u0410\u041e", callback_data="gisogd"),
            InlineKeyboardButton("\u0420\u0418\u0421 \u0417\u0410\u041a\u0423\u041f\u041a\u0418 \u0410\u041e", callback_data="ris")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u0435\u0440\u0432\u0438\u0441:", reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    """Handle button presses."""
    query = update.callback_query
    query.answer()
    responses = {
        "esed": "\u0412\u044b \u0432\u044b\u0431\u0440\u0430\u043b\u0438 \u0415\u0421\u042d\u0414",
        "gisogd": "\u0412\u044b \u0432\u044b\u0431\u0440\u0430\u043b\u0438 \u0413\u0418\u0421\u041e\u0413\u0414 \u0410\u041e",
        "ris": "\u0412\u044b \u0432\u044b\u0431\u0440\u0430\u043b\u0438 \u0420\u0418\u0421 \u0417\u0410\u041a\u0423\u041f\u041a\u0418 \u0410\u041e",
    }
    text = responses.get(query.data, "\u041d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b\u0439 \u0432\u044b\u0431\u043e\u0440")
    query.edit_message_text(text=text)


def main() -> None:
    """Start the bot."""
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
