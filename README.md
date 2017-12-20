Movie Looper

Written in Python 3.5.2

This requires VLC Media Player to be installed - https://www.videolan.org/vlc/index.html

It also uses vlc.py found here - https://github.com/oaubert/python-vlc/blob/master/generated/2.2/vlc.py

The app stores a movie directory, if set by user. If none is set, it will ask you to set one. It will then scrape all of the movies, with the given extensions (), store and shuffle them. Once movies are stored, the app will begin playing the movies 1 by 1 in that order. Movies are re-shuffled every time the app is started. To close, you can use ALT+F4 and then restart the shell in IDLE.
