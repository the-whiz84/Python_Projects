# Day 46 - Authenticated Web Requests and Playlist Automation

Day 46 turns scraping into cross-platform automation. The script scrapes the Billboard Hot 100 for a chosen date, authenticates with Spotify, searches for matching tracks, and builds a private playlist. The key lesson is that scraping public data is only half the story. Once you need to write into a user account, authentication and API permissions become part of the workflow.

## 1. Scraping the Source List from Billboard

The script starts by pulling the Billboard chart for a specific date:

```python
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")
response.raise_for_status()
```

Then it parses the song names:

```python
soup = BeautifulSoup(top100_html, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
```

This reuses the BeautifulSoup ideas from Day 45, but now the scraped output is not the final artifact. It becomes input for another system.

## 2. Authenticating with Spotify Through OAuth

Spotify access is handled with `SpotifyOAuth`:

```python
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=auth_scope
))
```

This is the major step forward from simple API keys. The script is not only identifying an application. It is obtaining permission to act on behalf of a user.

That is why the scope matters. `playlist-modify-private` gives only the access needed for this task and nothing more.

## 3. Translating Song Names into Spotify URIs

Spotify playlist APIs do not accept raw song titles as the final identifier. The script has to search for each song and extract a URI:

```python
for song in song_names:
    result = sp.search(q=f"track:{song}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
```

This is the important mapping step in the whole project. Billboard names are one representation of a song, but Spotify needs its own internal identifiers.

The `try` / `except` block also matters because not every scraped song will have a matching track entry.

## 4. Creating the Playlist from the Mapped Track IDs

Once the URIs are ready, the script creates a new private playlist:

```python
user_id = sp.current_user()["id"]
PLAYLIST_ID = sp.user_playlist_create(
    user=user_id,
    public=False,
    name=f"{date} - BillBoard Top 100"
)['id']
```

Then it adds all the tracks:

```python
sp.user_playlist_add_tracks(playlist_id=PLAYLIST_ID, tracks=song_uris, user=user_id)
```

At this point the automation has crossed three systems:

- user input for the date
- Billboard for source chart data
- Spotify for authenticated playlist creation

That end-to-end handoff is what makes the project feel substantial.

## How to Run the Project

1. Open a terminal in this folder.
2. Set the required environment variables:

```bash
export SPOTIFY_CLIENT_ID='your_id'
export SPOTIFY_CLIENT_SECRET='your_secret'
```

3. Run:

```bash
python main.py
```

4. Enter a date like `2000-08-12`, approve the Spotify OAuth flow in your browser, and confirm that a private playlist is created in your account.

## Summary

Day 46 connects scraping to authenticated API automation. The script scrapes Billboard for historical chart data, authenticates with Spotify through OAuth, maps scraped song names to Spotify URIs, and creates a private playlist from those tracks. The main lesson is how public web data becomes useful once it is translated into the identifiers and permissions required by another platform.
