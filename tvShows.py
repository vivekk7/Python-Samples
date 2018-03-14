from videos import videos

class tvShows(videos):
    """
    This is a Movies class that holds movie information
    """
    RATING = [1,2,3,4,5]
    
    def __init__(self, title, run_time, episode, number_of_seasons):
        videos.__init__(self, title, run_time)
        self.episode = episode
        self.number_of_seasons = number_of_seasons

    def get_local_listing(self):
        pass

friends = tvShows('Friends','20','4','10')
print friends.number_of_seasons
