#coding: utf-8
#解析成userid itemid rating timestamp行格式
import json
import sys

def is_null(s): 
	return len(s.split(","))>2

def parse_song_info(song_info):
	try:
		song_id, name, artist, popularity = song_info.split(":::")
		#return ",".join([song_id, name, artist, popularity])
		return ",".join([song_id,"1.0",'1300000'])
	except Exception:
		#print e
		#print song_info
		return ""

def parse_playlist_line(in_line):
	try:
		contents = in_line.strip().split("\t")
		name, tags, playlist_id, subscribed_count = contents[0].split("##")
		songs_info = map(lambda x:playlist_id+","+parse_song_info(x), contents[1:])
		songs_info = filter(is_null, songs_info)
		return "\n".join(songs_info)
	except Exception:
		print (e)
		return False
		

def parse_file(in_file, out_file):
	out = open(out_file, 'w',encoding='utf8')
	for line in open(in_file,encoding='utf8'):
		result = parse_playlist_line(line)
		if(result):
			out.write(result.strip()+"\n")
	out.close()