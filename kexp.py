import feedparser
import urllib2

FEED_URL = 'http://feeds.kexp.org/kexp/songoftheday'
DOWNLOAD_DIRECTORY = '/Users/imichaeldotorg/Music/DownloadedViaRSS'

def downloadFile(u,n):
	print "Downloading",u
	response = urllib2.urlopen(u)
	f = open(DOWNLOAD_DIRECTORY+'/'+n,'wb')
	f.write(response.read())
	f.close()
	print "done"


a = feedparser.parse(FEED_URL)

u = a['entries']
for e in u:
	theUrl = e['links'][1]['href']
	theFilename = theUrl.split('/')[-1]
	try:
		with open(DOWNLOAD_DIRECTORY + '/' + theFilename): pass
	except IOError:
		downloadFile(theUrl,theFilename)