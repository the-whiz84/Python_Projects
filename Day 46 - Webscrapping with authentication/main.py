from bs4 import BeautifulSoup
import requests, os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = "https://www.example.com/"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Retrieve the Top 100 song names for the given period
print(f"Getting Billboard Top 100 songs for the week of {date}........")

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")
response.raise_for_status()
top100_html = response.text

soup = BeautifulSoup(top100_html, "html.parser")
print("Retrieving song names from the Top 100 chart......")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# Authenticate to Spotify
print("Authenticating to Spotify and retrieving token.......")

auth_scope = "user-library-read playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=auth_scope))

# Retrieve user id and tracks uri
user_id = sp.current_user()["id"]
song_uris = []

print("Retrieving Spotify track URIs for each song name.......")

for song in song_names:
    result = sp.search(q=f"track:{song}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Create Spotify private playlist
PLAYLIST_ID = sp.user_playlist_create(user=user_id,public=False,name=f"{date} - BillBoard Top 100")['id']

print(f"Creating Spotify playlist with id: {PLAYLIST_ID}")
print("Adding tracks to playlist .....")

sp.user_playlist_add_tracks(playlist_id=PLAYLIST_ID,tracks=song_uris,user=user_id)
print("DONE")
