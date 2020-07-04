#
# Flask server module
#
from main import predict
from flask import Flask, jsonify, request


app = Flask(__name__, static_folder="public", static_url_path="/")


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
  return jsonify(
    {
      "title": "Intro And Tarantelle",
      "artist": "ABC",
      "mood": 'regret',
      "url": "http://www.openmusicarchive.org/audio/Intro_And_Tarantelle.mp3",
    },
    {
      "title": "Dont Go Way Nobody",
      "artist": "EFG",
      "mood": 'alone',
      "url": "http://www.openmusicarchive.org/audio/Dont_Go_Way_Nobody.mp3"
    },
    {
      "title": "April Kisses",
      "artist": "HIJ",
      "mood": 'sad',
      "url": "http://www.openmusicarchive.org/audio/April_Kisses.mp3"
    },
    {
      "title": "Eddies Twister",
      "artist": "KLM",
      "mood": 'relaxed',
      "url": "http://www.openmusicarchive.org/audio/Eddies_Twister.mp3"
    },
    {
      "title": "Little Bits",
      "artist": "NOP",
      "mood": 'happy',
      "url": "http://www.openmusicarchive.org/audio/Little_Bits.mp3"
    }
  )


# Determine if "text" is relaxing or not.
@app.route("/relaxing")
def relaxing():
  return jsonify(
    relaxing=predict(request.args.get("text"))
  )
