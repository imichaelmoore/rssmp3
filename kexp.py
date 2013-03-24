import feedparser
import urllib2
import json

FEED_URL = 'http://feeds.kexp.org/kexp/songoftheday'
DOWNLOAD_DIRECTORY = '/Users/imichaeldotorg/Music/DownloadedViaRSS'
FEED_NAME = 'kexp'

def downloadFile(u,n):
	print "Downloading",u
	response = urllib2.urlopen(u)
	f = open(DOWNLOAD_DIRECTORY+'/'+n,'wb')
	f.write(response.read())
	f.close()
	print "done"


a = feedparser.parse(FEED_URL)

#Open log of already downloaded files -- This file needs to be created before first run.  Should fix this.
f = open(DOWNLOAD_DIRECTORY + '/' + FEED_NAME + '_downloaded.json','r')
d = f.read()
f.close()
downloads = json.loads(d)

u = a['entries']
l = len(u)
i = 0
for e in u:
	i = i + 1
	theUrl = e['links'][1]['href']
	print "Downloading File",i,"of",l
	theFilename = theUrl.split('/')[-1]
	if theUrl not in downloads:
		downloadFile(theUrl,theFilename)
		downloads.append(theUrl)
	
		#Save log of already downloaded files.
		f = open(DOWNLOAD_DIRECTORY + '/' + FEED_NAME+ '_downloaded.json','w')
		f.write(json.dumps(downloads))
		f.close()
	else:
		print "Already downloaded",theUrl

