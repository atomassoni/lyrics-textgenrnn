#!/usr/bin/python3

from textgenrnn import textgenrnn
import urllib.parse
import requests
import json
import os.path
import sys

textgen = textgenrnn()
artist_search = ' '.join(sys.argv[1:]).lower()
api_key = #musixmatch api key here
base_url = 'http://api.musixmatch.com/ws/1.1/'
get_track = 'matcher.track.get'
get_lyric = 'track.lyrics.get'
get_all_tracks = 'track.search'
before_time = '20190501'
track_list = []
lyrics_directory = 'lyrics/'
output_directory = 'output/'
lyrics_file = lyrics_directory + '_'.join(sys.argv[1:]).lower() + '.txt'
output_file = output_directory + '_'.join(sys.argv[1:]).lower() + '.txt'

def get_lyrics_content(track_id):
  f = {'track_id': track_id, 'apikey' : api_key }
  request = base_url + get_lyric + '?' + urllib.parse.urlencode(f)
  response = requests.get(request)
  jx = response.json()
  # print(jx)
  s1 = jx['message']['body']['lyrics']['lyrics_body']
  s2 = s1.replace("...\n\n******* This Lyrics is NOT for Commercial use *******", '')
  s3 = s2.replace("\n\n", "\n")
  f = open(lyrics_file, 'a')
  f.write(s3)
  f.close()

def get_all_tracks_by_artist():
  f = {'f_track_release_group_first_release_date_max' : before_time, 'page_size' : '50', 'page': '1', 's_track_rating' : 'desc', 'apikey' : api_key, 'q_artist' : artist_search }
  request = base_url + get_all_tracks + '?' + urllib.parse.urlencode(f)
  response = requests.get(request)
  jx = response.json()
  tracks = jx['message']['body']['track_list']
  for track in tracks:
    if track['track']['has_lyrics'] > 0:
      get_lyrics_content(track['track']['track_id'])

try:
  result = os.path.exists(lyrics_file)
except Exception as path_err:
  print("error parsing stream")
else:
  if result:
    print("already a file for {}".format(artist_search))
  else:
    print("no lyrics for {} yet, generating".format(artist_search))
    get_all_tracks_by_artist()

textgen.train_from_file(lyrics_file, num_epochs=1)
textgen.generate_to_file(output_file, n=16)