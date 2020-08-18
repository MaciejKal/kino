from django.shortcuts import render
from django.views import View
from .models import Cinema
from movie.models import Show, Movie
import datetime

# Create your views here.
class HomeCinemaListView(View):
    template_name = 'HomeCinemaList.html'
    queryset = Cinema.objects.all()
    shows = Show.objects.all()
    movies = []
    for show in shows:
        if(show.dateFrom <= datetime.date.today() or show.dateTo >= datetime.date.today()):
            movie = show.movie
            if movie not in movies:
                movies.append(movie)




    def get_queryset(self):
        return self.queryset

    def get_querysetMovies(self):
        return self.movies

    def get_querysetShow(self):
        return self.shows

    def get(self, request, *args, **kwargs):
        context = {
            'object_list': self.get_queryset(),
            'object_list_movies': self.get_querysetMovies(),
            'object_list_shows': self.get_querysetShow()
        }
        return render(request, self.template_name, context)
