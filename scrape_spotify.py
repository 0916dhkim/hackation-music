from dotenv import load_dotenv
import asyncio
import httpx
from main import predict
from typing import List


# Load environment variables.
load_dotenv()

token = "BQB_8iAXJllM2lC3tXCwYX33bgBxnVFDDBIKRHNkwzE2WI-2yU5izmOcCtyVe7I6i2_uTJkkR7bhtih2FasbT7-82isR6OLVpN0GEHR4gyttZOq2SpYVZa0-ubn1-CEoDZ_o2K_IDMlUke4PD1x7PgYxsNo"


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
      "https://api.spotify.com/v1/browse/categories/toplists/playlists",
      headers={
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer " + token
      }
    )
    playlistIds = [i["id"] for i in res.json()["playlists"]["items"]]
  return playlistIds


# Get tracks in playlist.
async def playlistTracks(playlistId: str) -> List[str]:
  async with httpx.AsyncClient() as client:
    res = await client.get(
      f"https://api.spotify.com/v1/playlists/{playlistId}/tracks",
      headers={
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer " + token
      }
    )
    tracks = [i["track"] for i in res.json()["items"]]
  return [ Track(track["id"], track["preview_url"], track["name"], track["artists"][0]["name"]) for track in tracks ]

# Scrape tracks from Spotify
# and sort them into categories.
async def prepareTracks():
  playlistIds = await browseToplists()
  for playlist in playlistIds:
    tracks = await playlistTracks(playlist)
    for track in tracks:
      print(track)
      if predict(track.title) is "Relaxing":
        relaxingTracks.append(track)
      else:
        nonRelaxingTracks.append(track)

asyncio.run(prepareTracks())
