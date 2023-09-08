#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        # Process user_input using your Python function
        processed_result = process_input(user_input)
        return render_template('index.html', result=processed_result)
    return render_template('index.html', result=None)

def song_recommender(df1, df2):
    song = input("Please enter the name of a song: ")
    # Check if the input contains at least one alphabetical character and/or alphanumeric character
    if not (any(c.isalpha() for c in song) and any(c.isalnum() for c in song)):
        print("Invalid input. Please enter a song name containing letters and/or numbers.")
        return
    print(f"You entered a valid song name: {song}")
    # Load Spotify secrets
    secrets_file = open("secrets.txt", "r")
    string = secrets_file.read()
    secrets_dict = {}
    for line in string.split('\n'):
        if len(line) > 0:
            secrets_dict[line.split(':')[0]] = line.split(':')[1].strip()
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=secrets_dict['clientid'],
                                                               client_secret=secrets_dict['clientsecret']))
    results = sp.search(q='track:' + song, type='track')
    track = pd.json_normalize(results["tracks"]["items"])
    if not track.empty:
        song_id = track.iloc[0]['id']
        song_url = track.iloc[0]['external_urls.spotify']
    else:
        print("Song not found in Spotify.")
        return
    audio_features_list = sp.audio_features(song_id)
    audio_features_df = pd.json_normalize(audio_features_list)
    audio_features_df = audio_features_df[['duration_ms', 'danceability',
                                           'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
                                           'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']]
    # Load scaler and transform data
    with open('scaler.pkl', 'rb') as f:
        loaded_scaler = pickle.load(f)
        X = loaded_scaler.transform(audio_features_df)
    # Load KMeans model and predict cluster
    with open('kmeans.pkl', 'rb') as f:
        loaded_kmeans = pickle.load(f)
        clusters = loaded_kmeans.predict(X)
    matching_song = df1[(df1['title'].str.lower() == song.lower())]
    if not matching_song.empty:
        print(f"The song '{matching_song['title'].values[0]}' by {matching_song['artist'].values[0]} matches your input.")
        recommended_song = df1[df1['title'].str.lower() != song].sample(1)
        print(f"Here's a recommended song: '{recommended_song['title'].values[0]}' by {recommended_song['artist'].values[0]}")
        results2 = sp.search(q='track:' + recommended_song['Title'].values[0], type='track')
        track2 = pd.json_normalize(results2["tracks"]["items"])
        song_url = track2.iloc[0]['external_urls.spotify']
        print(f"Here's a url of the song: {song_url}")
    else:
        cluster_df = df2[df2['clusters'] == clusters[0]]
        recommended_song2 = cluster_df[cluster_df['track_name'].str.lower() != song].sample(1)
        print(f"Here's a recommended song: '{recommended_song2['track_name'].values[0]}' by {recommended_song2['artists'].values[0]}")
        results3 = sp.search(q='track:' + recommended_song2['track_name'].values[0], type='track')
        track3 = pd.json_normalize(results3["tracks"]["items"])
        song_url = track3.iloc[0]['external_urls.spotify']
        print(f"Here's a url of the song: {song_url}")

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




