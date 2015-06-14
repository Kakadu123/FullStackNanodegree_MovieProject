# resource imported
import webbrowser


# Movie class defined
class Movie():

    def __init__(self, title_name, story_line_detail, poster_detail, trailer_detail):
        """
        Initialization method to set initial attributes
        """
        self.title = title_name
        self.storyline = story_line_detail
        self.poster_image_url = poster_detail
        self.trailer_youtube_url = trailer_detail

    def show_trailer(self):
        """
        method of Movie class to display youtube trailer
        """
        webbrowser.open(self.trailer_youtube_url)
