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

2. Run the bot:

   ```bash
   python bot.py
   ```

The bot token is already defined in `bot.py`. If you need to use a different token, edit the value of `TOKEN` inside that file.

The bot uses polling to receive updates.
