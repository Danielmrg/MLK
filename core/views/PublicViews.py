from django.shortcuts import (render, HttpResponse,get_object_or_404)
from core.filters import *
from core.models import *



def Home(request):
   adverts_list = Advert.objects.filter(user=request.user)
   adverts = AdvertFilter(request.GET, queryset=adverts_list)
   context = {
      'adverts':adverts
   }
   return render(request, 'work/public_advert.html', context)

def Detail(request,slug):
   qs = get_object_or_404(Advert,slug=slug)
   context = {
      'advert': qs
   }
   return render(request,'work/Detail.html',context)

def My_page(request):
   if request.GET.get('qs'):
         adverts_list = Advert.objects.search_all(query=request.GET.get('qs')).filter(user=request.user)
   else:
         adverts_list = Advert.objects.filter(user=request.user)
   context = {
      'adverts': adverts_list
   }
   return render(request,'work/My_page.html',context)

def Group_page(request):
   users = request.user.group.get_all_users()
   context = {
      'users': users
   }
   return render(request, 'work/All_users.html', context)

def Group_adverts(request):
   all_adverts = request.user.group.get_all_adverts()
   context = {
      'adverts': all_adverts,
   }
   return render(request,'work/My_page.html',context)