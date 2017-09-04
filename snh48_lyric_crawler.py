import urllib
import requests
import json
import re
from bs4 import BeautifulSoup

def song_id_crawler():
	
	play_list_url = "http://music.163.com/playlist?id=37936323"

	request = urllib.request.Request(play_list_url)

	response = urllib.request.urlopen(request)

	content = response.read().decode('utf-8')

	pattern = re.compile('<a href="/song\?id=(.*?)">')

	song_id = re.findall(pattern,content)

	print("Find all SNH48 GROUP song ids.\n")

	return song_id

def lyric_crawler(song_id):

	lyric_url = 'http://music.163.com/api/song/lyric?' + 'id=' + song_id +'&lv=1&kv=1&tv=-1'

	lyric = requests.get(lyric_url)

	json_obj = lyric.text

	j = json.loads(json_obj)

	try:

		lyric = j['lrc']['lyric']

		pattern = re.compile(r'\[.*\]')

		lyric = re.sub(pattern,"",lyric)

		lyric = lyric.strip()

	except KeyError as e:

		lyric = " "

	return lyric

def main():

	f = open("SNH48_lyric.txt","w")

	song_id = song_id_crawler()

	print("Start to find lyric")

	count = 1

	for id in song_id:

		if id != '${x.id}':

			print(count,id)

			lyric = lyric_crawler(id)

			f.write(lyric)

			count = count + 1

	f.close()

	print('Finish.')


if __name__ == '__main__':
	
	main()




