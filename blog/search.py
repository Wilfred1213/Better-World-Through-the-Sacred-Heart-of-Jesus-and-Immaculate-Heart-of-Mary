from blog.models import *
from homeApp.models import Sacramental, SaintOfTheDay

def stationsearch(request):
    if request.method =='GET':
        search = request.GET.get('search')
        
        search_station = Stationofcross.objects.filter(title__icontains =search) if search else None
        return search_station    

def prayersearch(request):
    if request.method =='GET':
        search = request.GET.get('search')
        
        search_prayer = Prayers.objects.filter(title__icontains =search) if search else None
        return search_prayer    

def novenasearch(request):
    if request.method =='GET':
        search = request.GET.get('search')
        
        search_novena = Novena.objects.filter(title__icontains =search) if search else None
        return search_novena

def blogsearch(request):
    if request.method =='GET':
        search = request.GET.get('search')
        
        search_blog = My_blog.objects.filter(title__icontains =search) if search else None
        return search_blog
    
def saintsearch(request):
    if request.method =='GET':
        search = request.GET.get('search')
        
        search_prayer = SaintOfTheDay.objects.filter(name__icontains =search) if search else None
        return search_prayer 
    

def sacramentalsearch(request):
    if request.method =='GET':
        search = request.GET.get('search')
        
        search_prayer = Sacramental.objects.filter(name__icontains =search) if search else None
        return search_prayer 