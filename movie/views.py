from django.shortcuts import render
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from cinema.models import Cinema, Place
from .models import Show, ShowHall, Preview, Reservation
import datetime
# Create your views here.
class ShowView(View):
    template_name = 'ShowDetailts.html'
    def get_objects(self):
        queryset = []
        idC = self.kwargs.get('idC')
        idM = self.kwargs.get('idM')
        dateSelect = self.request.GET.get('date', datetime.date.today())


        shows = Show.objects.all().filter(cinema_id = idC).filter(movie_id=idM)
        for show in shows:
            showHall = ShowHall.objects.all().filter(show_id = show.id).filter(dateTime__date = dateSelect).order_by('pricing_id','dateTime')
            queryset.append([show, showHall])

        return queryset

    def get_preview(self):
        idC = self.kwargs.get('idC')
        idM = self.kwargs.get('idM')
        return Preview.objects.all().filter(cinema_id = idC).filter(movie_id=idM)

    def get(self, request, *args, **kwargs):
        context = {
            'object_list': self.get_objects(),
            'preview': self.get_preview(),

        }
        return render(request, self.template_name, context)

class PreviewListView(View):
    template_name = 'PreviewList.html'
    def get_previews(self):

        return Preview.objects.all().filter(premiere__gt = datetime.date.today()).order_by('movie_id')

    def get(self, request, *args, **kwargs):
        context = {
            'preview_List': self.get_previews(),

        }
        return render(request, self.template_name, context)

class PreviewListCinemaView(View):
    template_name = 'PreviewList.html'
    def get_previews(self):
        idC = self.kwargs.get('id')
        return Preview.objects.all().filter(cinema_id = idC).filter(premiere__gt = datetime.date.today()).order_by('movie_id')

    def get(self, request, *args, **kwargs):
        context = {
            'preview_List': self.get_previews(),

        }
        return render(request, self.template_name, context)

class ChoosePlaceView(View):
    template_name = 'ChoosePlace.html'
    def get_showHall(self):
        idS = self.kwargs.get('id')
        return ShowHall.objects.get(id=idS)

    def get_seats(self):
        idS = self.kwargs.get('id')
        ret = []
        places = Place.objects.all().filter(hall_id=ShowHall.objects.get(id=idS).hall.id).order_by('row','number')
        for iter in places:
            try:
                go = Reservation.objects.get(place_id=iter.id)
            except ObjectDoesNotExist:
                go = None
            if go == None:
                ret.append([iter, 0])
            else:
                ret.append([iter, 1])
        return ret



    def get(self, request, *args, **kwargs):
        context = {
            'object_list': self.get_seats(),
            'showHall': self.get_showHall(),
        }
        return render(request, self.template_name, context)
