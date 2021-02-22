from django.urls import path
from . import views

app_name='dashboard'

urlpatterns = [
    path('',views.Home,name='home'),
    path('Detail/<slug>/',views.Detail,name='detail'),
    path('MyPage/',views.My_page,name='my-adverts'),
    path('Group/',views.Group_page,name='users'),
    path('group-adverts/',views.Group_adverts,name='group-adverts'),
    path('AddAdvert/',views.Add_advert,name="add-advert"),
]