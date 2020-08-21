from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
import asyncio
import httpx
from main import predict
from typing import List
import os


# Load environment variables.
load_dotenv()

# Use spotipy package for maanaging access tokens.
if os.getenv("SPOTIFY_CLIENT_ID") is None:
  raise Exception("Environment variable SPOTIFY_CLIENT_ID is required.")
if os.getenv("SPOTIFY_CLIENT_SECRET") is None:
  raise Exception("Environment variable SPOTIFY_CLIENT_SECRET is required.")
spotify = SpotifyClientCredentials(
  client_id=os.getenv("SPOTIFY_CLIENT_ID"),
  client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
)


class Track:
  def __init__(self, id, preview, title, artist):
    self.id = id
    self.preview = preview
    self.title = title
    self.artist = artist

  def __str__(self):
    return f"<[{self.id}] {self.title} ; {self.artist}>"


# List of relaxing tracks.
relaxingTracks: List[Track] = []
# List of non-relaxing tracks.
nonRelaxingTracks: List[Track] = []

# Get playlists from toplists category.
async def browseToplists() -> List[str]:
  async with httpx.AsyncClient() as client:
    res = await client.get(
      "https://api.spotify.com/v1/browse/categories/toplists/playlists?limit=50",
      headers={
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer " + spotify.get_access_token(as_dict=False)
      }
    )
    playlistIds = [i["id"] for i in res.json()["playlists"]["items"]]
  return playlistIds


# Get tracks in playlist.
async def playlistTracks(playlistId: str) -> List[Track]:
  async with httpx.AsyncClient() as client:
    res = await client.get(
      f"https://api.spotify.com/v1/playlists/{playlistId}/tracks",
      headers={
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer " + spotify.get_access_token(as_dict=False)
      }
    )
    tracks = [i["track"] for i in res.json()["items"]]
    tracks = filter(
        lambda track: track is not None,
        tracks
    )
  return [ Track(track["id"], track["preview_url"], track["name"], track["artists"][0]["name"]) for track in tracks ]

# Scrape tracks from Spotify
# and sort them into categories.
async def prepareTracks():
  playlistIds = await browseToplists()
  for playlist in playlistIds:
    tracks = await playlistTracks(playlist)
    for track in tracks:
      # Omit null preview url.
      if track.preview is None:
        print(track, "missing preview")
        continue
      print(track)
      if predict(track.title) is "Relaxing":
        relaxingTracks.append(track)
      else:
        nonRelaxingTracks.append(track)

asyncio.run(prepareTracks())
