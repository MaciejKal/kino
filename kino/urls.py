"""kino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from kino import settings


from cinema.views import HomeCinemaListView, CinemaMovieList
from movie.views import ShowView, PreviewListCinemaView, PreviewListView, ChoosePlaceView

urlpatterns = [
    path('admin/', admin.site.urls),
    path( '', HomeCinemaListView.as_view(), name='home-page'),
    path( 'kino/<int:idC>', CinemaMovieList.as_view(), name='cinema-movies'),
    path( 'kino/<int:idC>/film/<int:idM>', ShowView.as_view(), name='cinema-movies'),
    path('zapowiedzi/<int:id>', PreviewListCinemaView.as_view(), name='preview-cinema-movies'),
    path('zapowiedzi/', PreviewListView.as_view(), name='preview-movies'),
    path('seans/<int:id>', ChoosePlaceView.as_view(), name='choose-place')
] +static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)