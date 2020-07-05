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
  return jsonify([
    {
      "title": track.title,
      "artist": track.artist,
      "url": track.preview
    } for track in relaxingTracks
  ])


# Determine if "text" is relaxing or not.
@app.route("/relaxing")
def relaxing():
  return jsonify(
    relaxing=predict(request.args.get("text"))
  )
