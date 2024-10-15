
************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu              
*    Author: Radu Chiriac                                  
*    Day: 46 - Music Tracks Time Machine                   
*    Subject: BeautifulSoup, API token, spotipy, requests  
*    Date: 2024-09-11                                      
************************************************************


# Description
This is a project that scrapes the data from Billboard Hot 100 Songs for a given date (https://www.billboard.com/charts/hot-100/) and then creates a private playlist in your Spotify account with those songs.

# How to use
- create a free Spotify account, if you don't already have one
- go to the Developer Dashboard and create a new Spotify App: https://developer.spotify.com/dashboard/ 
- for the mandatory Redirect URIs enter a dummy but valid URL (https://www.examle.com or http://localhost:8080)
- update the same variable with the exact one that you have put in the Spotify app
- retrieve your Client Id and Client Secret and store them as environment variables (https://www.twilio.com/en-us/blog/how-to-set-environment-variables-html)
- run the program
- on first run or after each session where you deleted .cache, a browser window will open to authenticate to Spotify
- copy the full URL returned after successful authentication the console as instructed

# WARNING
The spotipy module creates a hidden file named .cache in the same folder as main.py, where it stores the Spotify session token after authentication. After you finish creating your playlists, DELETE that file for the safety and security of your Spotify account.