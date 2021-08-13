"""A video player class."""

from .video_library import VideoLibrary
import random 
from .video_playlist import Playlist

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._video_play = None
        self._is_paused = False
        self._playlists = list()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:\n")
        videos = self._video_library.get_all_videos()
        for vid in sorted(videos, key=lambda v: v.title[0]):
            
            tgs = "[" 
            for i in range(len(vid.tags)):

                tgs = tgs + vid.tags[i].strip() + " "
             
            tgs = tgs.rstrip() + "]"
            
            print(vid.title, " (", vid.video_id, ") ", tgs if vid.tags else [])
        

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        new_vid = self._video_library.get_video(video_id)
        
        if new_vid is None:
            print("Cannot play video: Video does not exist")
            return
            
        if self._video_play is not None:
            self.stop_video()
        
        print("Playing video:", new_vid.title)   
        self._video_play = new_vid
        self._is_paused = False
    

    def stop_video(self):
        """Stops the current video."""
        
        if self._video_play is None:
            print("Cannot stop video: No video is currently playing")
#            return            #(get rid of 'else')
        else:
            print("Stopping video:", self._video_play.title)
            self._video_play = None
        
        self._is_paused = False

    def play_random_video(self):
        """Plays a random video from the video library."""
        
        videos = self._video_library.get_all_videos()
        rand_vid = random.choice(videos)
        
        if len(videos) == 0:
            print("No videos available")
            return
        
        self.play_video(rand_vid.video_id)

    def pause_video(self):
        """Pauses the current video."""
        
        if self._is_paused == True:
            print("Video already paused:", self._video_play.title)
            return
        if self._video_play is None:
            print("Cannot pause video: No video is currently playing")
            return
        
        print("Pausing video:", self._video_play.title)
        self._is_paused = True

    def continue_video(self):
        """Resumes playing the current video."""
        
        if self._is_paused == False:
            print("Cannot continue video: Video is not paused")
            return
        if self._video_play is None:
            print("Cannot continue video: No video is currently playing")

        print("Continuing video:", self._video_play.title)
        self._is_paused = False

    def show_playing(self):
        """Displays video currently playing."""
        
        if self._video_play is None:
            print("No video is currently playing")
            return
        
        tgs = "[" 
        for i in range(len(self._video_play.tags)):
            tgs = tgs + self._video_play.tags[i].strip() + " "
        tgs = tgs.rstrip() + "]"
        
        if self._is_paused == False:
            print("Currently playing:", self._video_play.title, " (", self._video_play.video_id, ") ", tgs if self._video_play.tags else [])
            
        else:
            print("Currently playing:", self._video_play.title, " (", self._video_play.video_id, ") ", tgs if self._video_play.tags else [], "- PAUSED")


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if self.playlist_exist(playlist_name) == True:
            print("Cannot create playlist: A playlist with the same name already exists")
            return
        
        new_playlist = Playlist(playlist_name)
        self._playlists.append(new_playlist)
        print("Successfully created new playlist:", playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")

    # Supplementary function to help    
    def playlist_exist(self, playlist_name):
        """ Checks if a playlist already exists.
        
        Args: playlist_name: the name of the new playlist
        Returns: whether or not the playlist exists """
        
        for playlist in self._playlists:
            
            if playlist_name.lower() == playlist.get_name().lower():
                return True
                