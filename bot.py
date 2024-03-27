import os
import requests
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler,Filters,CallbackQueryHandler
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,Update

load_dotenv()

bot_token = os.getenv('BOT_TOKEN')
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

spotify_client_id = os.getenv('Client_ID')
spotify_client_secret = os.getenv('Client_Secret')
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_client_secret))

BROWSE_OPTIONS = {
    'New Releases': 'new-releases',
}

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
            text="""
    Welcome to the Spotify Telegram Bot!

    Here are the available commands:
    /search - Perform a search
    /random - Get a random song
    /browse - Discover music
    """)

def download_audio(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None

def random_track(update, context):
    random_offset = random.randint(0, 10)  # Adjust the range based on your preference
    results = sp.search(q='track:', type='track', limit=1, offset=random_offset)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        track_name = track['name']
        track_artists = ', '.join(artist['name'] for artist in track['artists'])
        track_url = track['external_urls']['spotify']
        track_preview_url = track['preview_url']
        audio_file = download_audio(track_preview_url)
        context.bot.send_audio(chat_id=update.effective_chat.id, audio=audio_file, title=track_name, performer=track_artists)
        update.message.reply_text(f"Random track: {track_name} by {track_artists}\nListen on Spotify: {track_url}")

    else:
        update.message.reply_text("Sorry, no tracks found.")

def browse(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton(option, callback_data=data)] for option, data in BROWSE_OPTIONS.items()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Choose a browse option:', reply_markup=reply_markup)

def browse_option_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    option = query.data

    if option == 'new-releases':
        results = sp.new_releases(limit=15)
        handle_browse_results(query, results, "Here are the new releases:")

def handle_browse_results(query, results, message_prefix):
    if 'albums' in results:
        message = message_prefix
        for album in results['albums']['items']:
            album_name = album['name']
            artist_names = ', '.join(artist['name'] for artist in album['artists'])
            album_url = album['external_urls']['spotify']
            message += f"\n- {album_name} by {artist_names}\n  Listen on Spotify: {album_url}"
        query.edit_message_text(text=message)
    else:
        query.edit_message_text(text="Failed to retrieve browse results.")

def search(update: Update, context: CallbackContext):
    update.message.reply_text("Please enter the song you want to search:")

def process_search_query(update: Update, context: CallbackContext):
    search_query = update.message.text

    results = sp.search(q=search_query, limit=5) 

    formatted_results = []
    for track in results['tracks']['items']:
        track_name = track['name']
        artist_name = track['artists'][0]['name'] 
        track_url = track['external_urls']['spotify']
        formatted_result = f"Track: {track_name}\nArtist: {artist_name}\nURL: {track_url}"
        formatted_results.append(formatted_result)

    update.message.reply_text("\n\n".join(formatted_results))

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("search", search))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, process_search_query))
dispatcher.add_handler(CommandHandler("random", random_track))
dispatcher.add_handler(CommandHandler("browse", browse))
dispatcher.add_handler(CallbackQueryHandler(browse_option_callback))

updater.start_polling()