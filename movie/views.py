from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from cinema.models import Cinema, Place, Pricing
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
                go = Reservation.objects.get(showHall_id = idS,place_id=iter.id)
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

class ReservateView(View):
    template_name = 'Reservate.html'

    def get(self, request, *args, **kwargs):
        idS = self.kwargs.get('id')
        pricing = Pricing.objects.get(id = ShowHall.objects.get(id = idS).pricing.id)

        context = {

            'pricing':pricing,
            'idShow':idS
        }
        return render(request, self.template_name, context)

@method_decorator(csrf_exempt, name='dispatch')
class FinalizeView(View):
    template_name = 'Finalize.html'

    def get(self, request, *args, **kwargs):

        context = {


        }
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        mail = request.POST.get('mail')
        showH = request.POST.get('showH')
        places = request.POST.get('places')
        norm = int(request.POST.get('norm'))
        sch = int(request.POST.get('sch'))
        stud = int(request.POST.get('stud'))
        child = int(request.POST.get('child'))

        text = "Rezarwacja powiodła się<br/>Zarezerwowano " + str(norm + sch + stud + child) + " miejsc:<br/>" + str(norm) + ": normalnych<br/>" + str(sch) + ": szkolnych<br/>" + str(stud) + ": studenckich<br/>"+ str(child) + ": dla dzieci<br/>"

        tab = places.split(',')
        showHallObject = ShowHall.objects.get(id=showH)
        picing = Pricing.objects.get(id=showHallObject.pricing.id)
        sum = int(norm) * picing.priceNor + int(sch) * picing.priceSch + int(stud) * picing.priceStud + int(child) * picing.priceChild
        text = text + "Za kwotę: " + str(sum)  +"zł"
        for item in tab:
            p = item.split('.')
            try:
                go = Reservation.objects.get(showHall_id=showH, place_id = Place.objects.get(hall_id=showHallObject.hall.id, row=p[0], number=p[1]).id)
            except ObjectDoesNotExist:
                go = None
            if go != None:
                return render(request, 'Confirmation.html', { 'text': "Błąd rezerwacji" })

        for item in tab:
            p = item.split('.')
            if norm > 0:
                Reservation.objects.create(showHall = showHallObject, place = Place.objects.get(hall_id=showHallObject.hall.id, row =p[0], number=p[1]), price = picing.priceNor, mail=mail, payed=False, ukey=False)
                norm = norm - 1
            elif sch > 0:
                Reservation.objects.create(showHall = showHallObject, place = Place.objects.get(hall_id=showHallObject.hall.id, row =p[0], number=p[1]), price = picing.priceSch, mail=mail, payed=False, ukey=False)
                sch = sch - 1
            elif stud > 0:
                Reservation.objects.create(showHall = showHallObject, place = Place.objects.get(hall_id=showHallObject.hall.id, row =p[0], number=p[1]), price = picing.priceStud, mail=mail, payed=False, ukey=False)
                stud = stud - 1
            elif child > 0:
                Reservation.objects.create(showHall = showHallObject, place = Place.objects.get(hall_id=showHallObject.hall.id, row =p[0], number=p[1]), price = picing.priceChild, mail=mail, payed=False, ukey=False)
                child = child - 1

        print(self.request.POST)
        context = { 'text': text}

        return render(request, 'Confirmation.html', context)
