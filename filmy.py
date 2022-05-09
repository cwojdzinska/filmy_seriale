
import random
import numbers


class Watchable():
    def __init__(self, title="", year="", genre="",count=0):
        self.title=title
        self.year=year
        self.genre=genre
        self.count=count

    def play(self):
        self.count+=1
        

class Movie(Watchable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __str__(self):
        return f'{self.title} ({self.year}) | play count: {self.count}'


class Series(Watchable):
    def __init__(self, season="", episode="", *args, **kwargs):        
        super().__init__(*args, **kwargs)
        self.episode=episode
        self.season=season
    
    def __str__(self):
        return f'{self.title} S{self.season:02d}E{self.episode:02d} | play count: {self.count}'


if __name__=="__main__":
    
    watchables = [
        Movie(title="Pulp Fiction", genre="drama", year=1994),
        Movie(title="Kill Bill", genre="drama", year=2003),
        Series(title="Friends", genre="comedy", year=1993, season=1, episode=1),
        Series(title="Friends", genre="comedy", year=1993, season=1, episode=2),
        Series(title="Friends", genre="comedy", year=1993, season=1, episode=3),
        Series(title="Friends", genre="comedy", year=1993, season=1, episode=4),
        Series(title="Friends", genre="comedy", year=1993, season=1, episode=5),
    ]
    
    for i in range(0,10):
        random.choice(watchables).play()

    for w in watchables:
        print (w)