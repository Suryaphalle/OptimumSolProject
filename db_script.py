
import json
from movie.models import *
from datetime import datetime

mdate=datetime.strptime(movie_dict.get('date'), "%Y-%m-%dT%H:%M:%S.%fZ")
with open('movie.json','r') as file:
    movie_data = json.loads(file.read())

for movie_dict in movie_data:
    for movie in movie_dict.get('movies'):
        movie_geners = [] 
        for gen in movie.get('genre'):
            gen, created = Genre.objects.get_or_create(name=gen)
            movie_geners.append(gen)
        mov = Movies.objects.filter(title=movie.get('title')).last()
        if mov:
            print(mov, movie_geners)
            mov.genres.add(*movie_geners)
            mov.save() 
        # movie['genres'] = [m.id for m in movie_geners]
        del movie['genre']
        # movie_ratings = []
        # for rate in movie.get('Ratings'):
        #     rate, created = Rating.objects.get_or_create(source=rate.get('source'),value=rate.get('value'))
        #     movie_ratings.append(rate)
        # movie['ratings'] = [r.id for r in movie_ratings]
        del movie['Ratings']
        movie['released'] = datetime.strptime(movie.get('released'), "%d %b %Y").strftime("%Y-%m-%d")
        movie['dvd'] = datetime.strptime(movie.get('dvd'), "%d %b %Y").strftime("%Y-%m-%d") if movie.get('dvd') else None
        print(mov)