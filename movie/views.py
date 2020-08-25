from django.shortcuts import render
from django.shortcuts import render
from django.views import View
from cinema.models import Cinema
from .models import Show, ShowHall, Preview
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