import logging
import os
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Load environment variables from .env if present
load_dotenv()

# Telegram bot token
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable not set")

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def main_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("\u0415\u0421\u042d\u0414", callback_data="esed"),
            InlineKeyboardButton("\u0413\u0418\u0421\u041e\u0413\u0414 \u0410\u041e", callback_data="gisogd"),
            InlineKeyboardButton("\u0420\u0418\u0421 \u0417\u0410\u041a\u0423\u041f\u041a\u0418 \u0410\u041e", callback_data="ris"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def esed_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u043a \u0415\u0421\u042d\u0414", callback_data="esed_connect")],
        [InlineKeyboardButton("\u0420\u0430\u0431\u043e\u0442\u0430 \u0432 \u0415\u0421\u042d\u0414", callback_data="esed_work")],
        [InlineKeyboardButton("\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439 \u0415\u0421\u042d\u0414", callback_data="esed_admin")],
        [InlineKeyboardButton("\u041d\u0430\u0437\u0430\u0434", callback_data="back_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def esed_connect_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f \u043a \u0415\u041c\u0422\u0421", callback_data="connect_emts")],
        [InlineKeyboardButton("\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f \u043a \u0415\u0421\u042d\u0414", callback_data="connect_esed")],
        [InlineKeyboardButton("\u041d\u0430\u0437\u0430\u0434", callback_data="back_esed")],
    ]
    return InlineKeyboardMarkup(keyboard)

def start(update: Update, context: CallbackContext) -> None:
    """Send the main menu when /start is issued."""
    update.message.reply_text(
        "Выберите сервис:",
        reply_markup=main_menu(),
    )



def button(update: Update, context: CallbackContext) -> None:
    """Handle button presses and support navigation."""
    query = update.callback_query
    query.answer()
    data = query.data

    if data in ("esed", "back_esed"):
        query.edit_message_text(
            text="\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u0430\u0437\u0434\u0435\u043b:",
            reply_markup=esed_menu(),
        )
        return

    if data == "back_main":
        query.edit_message_text(
            text="\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u0435\u0440\u0432\u0438\u0441:",
            reply_markup=main_menu(),
        )
        return

    if data == "esed_connect":
        text = (
            "\ud83d\udd0c \u0427\u0442\u043e\u0431\u044b \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u043e\u0441\u0442\u0443\u043f \u043a \u0415\u0421\u042d\u0414, \u0432\u0430\u0448\u0430 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f \u0434\u043e\u043b\u0436\u043d\u0430 \u0431\u044b\u0442\u044c \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0430 \u043a \u0435\u0434\u0438\u043d\u043e\u0439 \u043c\u0443\u043b\u044c\u0442\u0438\u0441\u0435\u0440\u0432\u0438\u0441\u043d\u043e\u0439 \u0442\u0435\u043b\u0435\u043a\u043e\u043c\u043c\u0443\u043d\u0438\u043a\u0430\u0446\u0438\u043e\u043d\u043d\u043e\u0439 \u0441\u0435\u0442\u0438 \u041f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u0430 \u0410\u0441\u0442\u0440\u0430\u0445\u0430\u043d\u0441\u043a\u043e\u0439 \u043e\u0431\u043b\u0430\u0441\u0442\u0438 (\u0415\u041c\u0422\u0421)."
        )
        query.edit_message_text(text=text, reply_markup=esed_connect_menu())
        return

    responses = {
        "esed_work": "\u0412\u044b \u0432\u044b\u0431\u0440\u0430\u043b\u0438 \u00ab\u0420\u0430\u0431\u043e\u0442\u0430 \u0432 \u0415\u0421\u042d\u0414\u00bb",
        "esed_admin": "\u0412\u044b \u0432\u044b\u0431\u0440\u0430\u043b\u0438 \u00ab\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439 \u0415\u0421\u042d\u0414\u00bb",
        "connect_emts": "\u0412\u044b \u0432\u044b\u0431\u0440\u0430\u043b\u0438 \u00ab\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f \u043a \u0415\u041c\u0422\u0421\u00bb",
        "connect_esed": "\u0412\u044b \u0432\u044b\u0431\u0440\u0430\u043b\u0438 \u00ab\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f \u043a \u0415\u0421\u042d\u0414\u00bb",
        "gisogd": "\u0412\u044b \u0432\u044b\u0431\u0440\u0430\u043b\u0438 \u0413\u0418\u0421\u041e\u0413\u0414 \u0410\u041e",
        "ris": "\u0412\u044b \u0432\u044b\u0431\u0440\u0430\u043b\u0438 \u0420\u0418\u0421 \u0417\u0410\u041a\u0423\u041f\u041a\u0418 \u0410\u041e",
    }

    text = responses.get(data, "\u041d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b\u0439 \u0432\u044b\u0431\u043e\u0440")
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
