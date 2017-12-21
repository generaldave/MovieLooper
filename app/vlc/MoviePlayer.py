'''
David Fuller

MoviePlayer class: Setsup and plays movies in a loop

12-20-2017
'''

import os
import tkinter as tk
from tkinter import filedialog
from random import shuffle

from .vlc import *

supported_movie_extensions = ['mkv', 'mp4', 'avi', 'm4v']

class MoviePlayer(object):
    '''
    Sets up a movie player class.
    '''
    
    def __init__(self, app_directory):
        '''
        MoviePlayer's init method.

        Sets up a movie player object.

        Args:
            app_directory (str): Representation of application directory.
        '''
        
        self.app_directory = app_directory
        self.movies = []

        path = self.setup_path()
        self.setup_movies(path)
        self.setup_player()
        
        self.index = 0 
        
    def setup_path(self):
        '''
        Sets up path to stored movies.

        Returns:
            path (str): Path to stored movies.
        '''
        
        root = tk.Tk()
        root.withdraw()

        settings_path = self.app_directory + '/files/settings'
        with open(settings_path, 'r') as settings_file:
            path = settings_file.readline()
            path = path.lstrip('path=')
            path = path.rstrip()

        if path == '':
            path = filedialog.askdirectory()
            with open(settings_path, 'w') as settings_file:
                settings_file.write('path=' + path)

        return path

    def setup_movies(self, path):
        '''
        Sets up movies array.

        Args:
            path (str): Path to stored movies.
        '''
        
        for root, dirs, files in os.walk(path):
            for name in files:
                for extension in supported_movie_extensions:
                    if name.endswith(extension):
                        self.movies.append(root + '/' + name)

        shuffle(self.movies)

    def setup_player(self):
        '''
        Sets up movie player object.
        '''
        
        self.vlc_instance = Instance('--fullscreen')
        self.vlc_player = self.vlc_instance.media_player_new()
        self.vlc_player.set_fullscreen(True)

    def play_movie(self):
        '''
        Plays next movie.
        '''
        
        movie = self.movies[self.index]
        print(movie)
        vlc_media = self.vlc_instance.media_new_path(movie)
        self.vlc_player.set_media(vlc_media)
        self.vlc_player.play()

    def loop_movies(self):
        '''
        Loops through movies repeatedly.
        '''
        
        self.play_movie()
        
        playing = True
        while playing:
            if self.vlc_player.get_state() == State.Ended:
                self.vlc_player.stop()
                self.index = self.index + 1
                try:
                    movie = self.movies[self.index]
                except:
                    self.index = 0
                self.play_movie()
