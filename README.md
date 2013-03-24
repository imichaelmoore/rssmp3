rssmp3
======

KEXP's [song of the day](http://feeds.kexp.org/kexp/songoftheday) RSS feed is awesome.  So is MPR's [The Current](http://www.thecurrent.org/collection/song-of-the-day/rss) feed.  I'd like to download these each day and add them to my iTunes library, and have them automatically pushed to my iPhone via iTunes Match.

Here's a simple script to fetch the RSS feed and save the files into a directory on your Mac.  I then use [Hazel](http://www.noodlesoft.com/hazel.php) to automatically add them to a specific playlist in my iTunes library.

Requirements
============

You will need the excellent feedparser Python library.  I use it in a virtualenv.