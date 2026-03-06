# Day 46 - Authenticated Web Requests and Playlist Automation

Yesterday, we learned how to pull data from any website. Today, we're doing something much more powerful: we're taking that scraped data and pushing it into a major platform—Spotify.

We're building a "Musical Time Machine." You enter a date (like your graduation day or your 10th birthday), we scrape the Billboard Top 100 for that exact week, and then we automatically build a private Spotify playlist with all those songs.

## The Problem: Moving from Scraping to Automation

Scraping a website like Billboard is the easy part. The difficult piece of the puzzle is talking to Spotify. Unlike a public website, you can't just "scrape" your way into a private user account. You need **Authentication**.

### Step 1: Managing Secrets

To talk to Spotify, you need a Client ID and a Client Secret. These are like your username and password for the API. **Never** hardcode these directly in your script. If you push your code to GitHub, anyone can steal them.

Instead, we use environment variables:

```python
import os

SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
```

### Step 2: OAuth 2.0 (The "Dance")

Spotify uses OAuth 2.0. This is the protocol that allows you to "Log in with Google" or "Log in with Facebook" on other sites. In our script, we use the `spotipy` library to handle the heavy lifting:

```python
import spotipy
from spotipy.oauth2 import SpotifyOAuth

auth_scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri="https://www.example.com/",
    scope=auth_scope
))
```

The `scope` is crucial. It's us telling Spotify exactly what we want to do. We don't want to delete your account; we only want to `playlist-modify-private`. When you first run this, your browser will open, asking you to grant permission. Once you agree, Spotify sends a code back to your redirect URI, which `spotipy` captures to get your access token.

## The Process: Search, Map, and Create

Once we have the list of 100 song names from Billboard, we can't just give the names to Spotify. We need their unique **Spotify URIs**.

### Searching for Tracks

We loop through our scraped song names and perform a search for each one:

```python
for song in song_names:
    result = sp.search(q=f"track:{song}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
```

**Watch out—** Not every song from 1950 is on Spotify! We use a `try/except` block to catch `IndexError` if the search results for a song are empty. Without this, one missing song would crash your entire program.

### Creating the Playlist

Finally, once we have a list of URIs, we create the playlist and add the tracks in one go:

```python
user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(
    user=user_id,
    public=False,
    name=f"{date} - BillBoard Top 100"
)

sp.user_playlist_add_tracks(playlist_id=playlist['id'], tracks=song_uris)
```

## Running the Playlist Script

1. Set your environment variables in your terminal:
   ```bash
   export SPOTIFY_CLIENT_ID='your_id'
   export SPOTIFY_CLIENT_SECRET='your_secret'
   ```
2. Run the script:
   ```bash
   python "main.py"
   ```
3. Enter a date like `2000-08-12`.
4. Approve the request in your browser.
5. Check your Spotify app—you'll have a brand new "2000-08-12 - BillBoard Top 100" playlist waiting for you!

## Summary

Today we leaped from just "reading" the web to "interacting" with it. You learned how to handle OAuth authentication, manage sensitive API keys, and bridge the gap between two completely different systems (Billboard and Spotify) using Python as the glue.
