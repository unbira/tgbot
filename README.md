# tgbot

This repository contains a simple Telegram bot example. It provides three buttons when you run the `/start` command:

- **ЕСЭД**
- **ГИСОГД АО**
- **РИС ЗАКУПКИ АО**

Pressing a button will reply with a short confirmation message.
Selecting **\u0415\u0421\u042d\u0414** opens an additional menu with the options:

- \u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u043a \u0415\u0421\u042d\u0414
- \u0420\u0430\u0431\u043e\u0442\u0430 \u0432 \u0415\u0421\u042d\u0414
- \u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439 \u0415\u0421\u042d\u0414

## Setup

1. Install the dependencies (preferably in a virtual environment):

   ```bash
   pip install -r requirements.txt
   ```

2. Set your Telegram bot token. You can either export the `BOT_TOKEN` environment
   variable or create a `.env` file in the project root containing:

   ```
   BOT_TOKEN=<your token>
   ```

3. Run the bot:

   ```bash
   python bot.py
   ```

The bot will read the token from the environment. If `BOT_TOKEN` is missing an
informative error will be raised.

The bot uses polling to receive updates.
