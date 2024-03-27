# Spotify Telegram Bot

## Overview
The Spotify Telegram Bot is a Telegram bot that allows users to search for tracks, browse new releases, and perform various other actions related to Spotify directly from their Telegram chat.

## Features
- Search for tracks by name or artist
- Get random tracks
- Browse new releases
- Connect with your Spotify account

## Getting Started
Follow these instructions to set up and run the Spotify Telegram Bot locally.

### Prerequisites
- Python 3.6 or higher
- Spotify developer account
- Telegram bot token

### Installation
1. Clone this repository to your local machine.
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

### Usage
1. Set the required environment variables:
   - `BOT_TOKEN`: Your Telegram bot token.
   - `CLIENT_ID`: Your Spotify Client ID.
   - `CLIENT_SECRET`: Your Spotify Client Secret.
   
   Example:
   ```
   export BOT_TOKEN=<Your Telegram Bot Token>
   export CLIENT_ID=<Your Spotify Client ID>
   export CLIENT_SECRET=<Your Spotify Client Secret>
   ```

2. Run the bot using the following command:
   ```
   python bot.py
   ```

Once the bot is running, you can interact with it via your Telegram chat.

## Contributing
Contributions are welcome! Please follow the standard GitHub flow:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Create a new Pull Request

## Acknowledgments
- The Spotify API
- The Telegram Bot API
- Spotipy - A Python library for the Spotify Web API
