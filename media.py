import webbrowser

class Movie():    
    def __init__(self, title_name, story_line_detail, poster_detail, trailer_detail):
        self.title = title_name
        self.storyline = story_line_detail
        self.poster_image_url = poster_detail
        self.trailer_youtube_url = trailer_detail

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)