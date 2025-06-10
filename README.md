# tgbot

This repository contains a simple Telegram bot example. It provides three buttons when you run the `/start` command:

- **ЕСЭД**
- **ГИСОГД АО**
- **РИС ЗАКУПКИ АО**

Pressing a button will reply with a short confirmation message.

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
