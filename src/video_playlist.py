"""A video playlist class."""

from .video_library import VideoLibrary

class Playlist:
    """A class used to represent a Playlist."""
    
    def __init__(self, playlistname):
        
        self._playlist_name = playlistname
        self._videos = list()
        
        
    def get_name(self):
        """Returns name of the playlist"""
        return self._playlist_name

    def get_videos(self):
        """Returns the list of the videos within the playlist"""
        return self._videos
    
    def add_videos(self, video_id):
        """ Checks to see if video already exists in the playlist,
        otherwise it adds the requested video"""
        
        #new_vid = 