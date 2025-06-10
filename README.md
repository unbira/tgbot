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

2. Provide your bot's API token in the `BOT_TOKEN` environment variable. For example:

   ```bash
   export BOT_TOKEN="YOUR_TOKEN_HERE"
   ```

   Alternatively, you can create a `.env` file with `BOT_TOKEN=YOUR_TOKEN_HERE` and use a tool like `python-dotenv` to load it.

3. Run the bot:

   ```bash
   python bot.py
   ```

The bot uses polling to receive updates.
