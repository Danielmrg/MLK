from django.shortcuts import render,get_object_or_404
from advert.models import Advert
from authentication.models import User
from django.contrib.auth.decorators import login_required
from authentication.decorators import IsAllowRole

# @login_required(login_url="home:home")
@IsAllowRole
def Home(request):
    adverts = Advert.objects.filter(user=request.user)
    # adverts = AdvertFilter(request.GET, queryset=adverts_list)
    context = {
          'adverts':adverts
    }
    return render(request, 'dashboard/work/public_advert.html', context)

@IsAllowRole
def Detail(request,slug):
    qs = get_object_or_404(Advert,slug=slug)
    context = {
          'advert': qs
    }
    return render(request,'dashboard/work/Detail.html',context)

@IsAllowRole
def My_page(request):
    if request.GET.get('qs'):
            adverts_list = Advert.objects.search_all(query=request.GET.get('qs')).filter(user=request.user)
    else:
            adverts_list = Advert.objects.filter(user=request.user)
    context = {
          'adverts': adverts_list
    }
    return render(request,'dashboard/work/My_page.html',context)

@IsAllowRole
def Group_page(request):
    users = User.objects.all()
    context = {
       'users': users
    }
    return render(request, 'dashboard/work/All_users.html', context)

@IsAllowRole
def Group_adverts(request):
    all_adverts = Advert.objects.public()
    context = {
          'adverts': all_adverts,
    }
    return render(request,'dashboard/work/My_page.html',context)