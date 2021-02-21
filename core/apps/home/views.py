from django.shortcuts import render,redirect
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from advert.models import Advert
from authentication.models import User
from utils import get_by_pk_or_pass

def home(request):
    context = {
        'title':'Home',
        "saleadverts":Advert.objects.public().filter(category="S"),
        "fullrentadverts":Advert.objects.public().filter(category="R"),
        "rentadverts":Advert.objects.public().filter(category="A"),
        "buyadverts":Advert.objects.public().filter(category="B"),
    }
    return render(request,"Home/work/home.html",context)

def Adverts(request,page=1):
    page_number = page
    advertlist = Advert.objects.public()
    try:
        paginator = Paginator(advertlist, 6)
        adverts = paginator.get_page(page_number)
    except :
        adverts = ''
    context = {
        "title":"Advert's",
        "adverts":adverts
    }
    return render(request,"Home/work/Adverts.html",context)

def SearchAdvert(request,*args,**kwargs):
    search = request.GET.get('Category')
    if search == '':
        return redirect("home:advert")
    adverts = Advert.objects.public().filter(category=search)
    context = {
        "title":"search",
        'adverts': adverts,
    }
    return render(request, "Home/work/Adverts.html", context)

def DetailAdvert(request,Uid):
    context = {
        "title":"یافت نشد",
        "advert":None
    }
    advert = Advert.objects.get_object_or_pass(Uid=Uid)
    if advert:
        context['title'] = advert.title
        context['advert'] = advert
    return render(request,"Home/work/DetailAdvert.html",context)

def Agents(request,page=1):
    page_number = page
    agentlist = User.objects.get_by_role(role_name='agent')
    try:
        paginator = Paginator(agentlist, 6)
        agents = paginator.get_page(page_number)
    except :
        agents = ''
    context = {
        "title":"Agent's",
        "agents":agents,
    }
    return render(request,"Home/work/Agents.html",context)

def DetailAgent(request,pk):
    agent = get_by_pk_or_pass(User,pk=pk)
    context = {
        "title":"Agent",
        "agent":agent,
    }
    return render(request,"",context)

def AboutUs(request):
    context = {
        "title":"About Us",
        "aboutus":None
    }
    return render(request,"",context)
