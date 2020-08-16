from django.shortcuts import render
from django.views import View
from .models import Cinema

# Create your views here.
class HomeCinemaListView(View):
    template_name = 'HomeCinemaList.html'
    queryset = Cinema.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)
