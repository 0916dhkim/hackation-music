import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CSV_FIELDS = ['index','songName','artist','moodID','spotifyID','danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo']
RANGE_LOWER = 0
RANGE_UPPER = 100
INFILE = 'trainNumbered.csv'
OUTFILE = 'output.csv'
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())



with open(INFILE, newline='') as csvfile:
	reader = csv.reader(csvfile)
	data = list(reader)

#print(data)


# collect spotify ID's for all song searches
for i in range(RANGE_LOWER, RANGE_UPPER): #iterating through rows of the CSV data
	searchTerm = data[i][2] + " " + data[i][1]

	results = sp.search(q=searchTerm, type='track', limit=1)

	spotifyID = "null"
	for track in results['tracks']['items']:
	    #print(x, track['id'], track['name'],",",track['artists'][0]['name'])
	    spotifyID = track['id']
	    print("spotifyID", spotifyID)

	#add spotifyID
	if spotifyID is not None:
		data[i].append(spotifyID)
		# collect features for song id
		features = sp.audio_features(spotifyID)
		#print("featurelist=",features)
		if features is not None:
			for n in features:
				if n is not None:
					data[i].append(n['danceability'])
					data[i].append(n['energy'])
					data[i].append(n['key'])
					data[i].append(n['loudness'])
					data[i].append(n['mode'])
					data[i].append(n['speechiness'])
					data[i].append(n['acousticness'])
					data[i].append(n['instrumentalness'])
					data[i].append(n['liveness'])
					data[i].append(n['valence'])
					data[i].append(n['tempo'])



# writing to csv file  
with open(OUTFILE, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(CSV_FIELDS)  
        
    # writing the data rows  
    csvwriter.writerows(data) 






