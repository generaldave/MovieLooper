'''
David Fuller

App class: Initializes application

10-22-2017
'''

from .vlc import MoviePlayer

class App(object):
    '''
    Sets up and runs a Pygame application.
    '''
    
    def __init__(self, app_directory):
        '''
        App's init method.

        Stores application directory. Runs the applicaiton.

        Args:
            app_directory (str): Representation of application directory.
        '''
        
        player = MoviePlayer(app_directory)
        player.loop_movies()
