from django.urls import path
from . import views
app_name='home'

urlpatterns = [
    path("",views.home,name='home'),
    path("Adverts/",views.Adverts,name="advert"),
    path("Adverts/<page>/",views.Adverts,name="advert"),
    path("Adverts/search/",views.SearchAdvert,name="search-advert"),
    path("Adverts/Detail/<Uid>/",views.DetailAdvert,name="detail-advert"),
    path("Agents/",views.Agents,name="agent"),
    path("Agents/<page>/",views.Agents,name="agent"),
]