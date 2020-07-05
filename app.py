#
# Flask server module
#
from scrape_spotify import relaxingTracks, nonRelaxingTracks
from flask import Flask, jsonify, request
from flask_cors import CORS

# Random module
import random


app = Flask(__name__, static_folder="public", static_url_path="/")
CORS(app)


@app.route("/")
def index():
  return app.send_static_file("index.html")


# Test API endpoint
@app.route("/hello")
def hello_world():
  return "Hello, World!"


# Return an array of music URL
@app.route("/music")
def music():
  mood = request.args.get('mood') #get mood from query string

  if mood is None: # if no mood specified play relaxing songs only
    return jsonify([
    {
      "title": track.title,
      "artist": track.artist,
      "url": track.preview,
      "relaxing": True
    } for track in relaxingTracks
  ])

  # number of non relaxing songs as per given mood
  sadNo = {
  'love': 0,
  'lonely': 2,
  'sad': 1,
  'happy': 0,
  'anxious': 3,
  'relaxed': 0 ,
  }

  setSize = sadNo[mood] # size of sad sons array

  nonRel = [
    {
      "title": track.title,
      "artist": track.artist,
      "url": track.preview,
      "relaxing": False
    } for track in random.sample(nonRelaxingTracks, setSize) # create a random set of non relaxing songs of size setSize
  ]  

  Rel = [
    {
      "title": track.title,
      "artist": track.artist,
      "url": track.preview,
      "relaxing": True
    } for track in relaxingTracks
  ]

  res = nonRel+Rel # join nonrelaxing and relaxing tracks in response

  return jsonify(res)


# Determine if "text" is relaxing or not.
@app.route("/relaxing")
def relaxing():
  return jsonify(
    relaxing=predict(request.args.get("text"))
  )
