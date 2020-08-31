from django.shortcuts import render
from django.views import View
from .models import Cinema
from movie.models import Show, ShowHall
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

class CinemaMovieList(View):
    template_name = 'CinemaMovisList.html'
    def get_objects(self):
        queryset = []
        idC = self.kwargs.get('idC')
        dateSelect = self.request.GET.get('date', datetime.date.today())

        shows = Show.objects.all().filter(cinema_id = idC)
        for show in shows:
            showHall = ShowHall.objects.all().filter(show_id = show.id).filter(dateTime__date = dateSelect).order_by('pricing_id','dateTime')
            queryset.append([show, showHall])

        return queryset

    def get(self, request, *args, **kwargs):
        context = {
            'object_list': self.get_objects(),           
            'cinema_id': self.kwargs.get('idC')
        }
        return render(request, self.template_name, context)
        
