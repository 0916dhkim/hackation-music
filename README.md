# hackation-music
Music Service

## Getting Started
First, create a virtual environment.
```bash
python -m venv venv
```
Then, activate virtual environment.
```bash
# Windows
./venv/Scripts/activate

# MacOS and Linux
source venv/bin/activate
```
Install dependencies.
```bash
pip install -r requirements.txt
```
You need 2 environment variables for this app.
Create `.env` file at the project root, and add the
following environment variables.
- SPOTIFY_CLIENT_ID
- SPOTIFY_CLIENT_SECRET

You can get these values from <https://developer.spotify.com/dashboard/>

## Start Flask Server
```bash
python -m flask run
```

## API Specs

Method | Path | Example | Description
--- | --- | --- | ---
GET | /music | http://localhost:5000/music | Get an array of music URL
GET | /relaxing | http://localhost:5000/relaxing?text=Amazing%20Grace | Check if `text` is relaxing or not
GET | / | http://localhost:5000/ | Index Page
