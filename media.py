import webbrowser
from videos import videos


class Movies(videos):
    """
    This is a Movies class that holds movie information
    """
    RATING = [1,2,3,4,5]
    
    def __init__(self, title, story, run_time, youtube_url, poster_image_url):
        videos.__init__(self, title, run_time)
        self.story = story
        self.youtube_url = youtube_url
        self.poster_image_url = poster_image_url

    def run_url_video(self):
        webbrowser.open(self.youtube_url)

wonder_woman = Movies('WONDER WOMAN','Amazonians come to save the world', 
                      '140', 'https://www.youtube.com/watch?v=VSB4wGIdDwo', 
                      'https://www.google.com/search?q=wonder+woman+poster&client=safari&rls=en&tbm=isch&imgil=7WPd6ro4HwmUuM%253A%253BP45jePEB_3RTgM%253Bhttp%25253A%25252F%25252Fwww.joblo.com%25252Fmovie-posters%25252F2017%25252Fwonder-woman&source=iu&pf=m&fir=7WPd6ro4HwmUuM%253A%252CP45jePEB_3RTgM%252C_&usg=__WK3OOzRVCmwCdUburdrz9aovf6c%3D')
print wonder_woman.title
wonder_woman.run_url_video()
