import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

with open("config.json") as f:
    config = json.load(f)

# Set up Spotify client with OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=config["spotify_client_id"],
    client_secret=config["spotify_client_secret"],
    redirect_uri=config["spotify_redirect_uri"],
    scope="user-read-currently-playing" # Needed to see what's currently playing

# Fetch the current track's album art URL
def get_current_album_art_url():
    current = sp.current_user_playing_track()
    if current and current["item"]:
        return current["item"]["album"]["images"][0]["url"] # Return the first image URL
    return None # Nothing playing
