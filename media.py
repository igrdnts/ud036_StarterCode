class Movie():
    """This class provides a way to store movie related information"""

    def __init__(self, title, storyline, poster_image, trailer, duration):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer
        self.duration = duration
