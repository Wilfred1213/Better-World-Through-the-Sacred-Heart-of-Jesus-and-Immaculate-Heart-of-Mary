# from http.client import HTTPResponse

# from django.contrib.auth import login
from django.shortcuts import redirect, render
 
from .forms import novenaForm, novenaDaysForm, NewsLetterForm, PostForm, CommentForm, NovenaCommentForm, dailyPrayersForm
from . models import *

from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator,  EmptyPage, PageNotAnInteger
from . like import new_likes, authmessage
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from blog.search import *

@login_required(login_url ='authentications:loggin')
def create_novena(request):
    slider = Slider.objects.all()
    if request.method == 'POST':
        form = novenaForm(request.POST, request.FILES)
        if form.is_valid():
            title  = form.cleaned_data['title']
            post_body = form.cleaned_data['post_body']
            image = form.cleaned_data['image']
            
            Novena.objects.create(title = title, post_body=post_body, image=image)
            messages.info(request, 'novena saved')
            return redirect('create_days_of_novena')
        messages.error('Error saving novena')
    form = novenaForm()
    context = {
        'sliders':slider,
        'form':form,
    }
    return render(request, 'blog/create_novena.html', context)

@login_required(login_url ='authentications:loggin')
def create_days_of_novena(request):
    
    if request.method == 'POST':
          
        form = novenaDaysForm(request.POST, request.FILES)
        if form.is_valid():
            novena = form.cleaned_data['novena']
            save_novena = form.save(commit=False)
            save_novena.novena = novena
            save_novena.save()
            messages.info(request, 'Novena Save!')
            return redirect('create_days_of_novena')
        
    form = novenaDaysForm()
    context = {
        'form':form
    }
    return render(request, 'blog/create_days_of_novena.html', context)

# sending news letter
# @login_required(login_url ='authentications:loggin')        
def newsletter(request):
    slider = Slider.objects.all()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST, request.FILES)
        if form.is_valid(): 
            title = form.cleaned_data['title']
            letter = form.cleaned_data['letter']
            image = form.cleaned_data['image']
            
            NewsLetter.objects.create(title=title, letter=letter, news_img=image)
            messages.info(request, 'Letter sent successfully!')
            return redirect('newsletter')
        else:
            messages.error(request, 'Failed to send')
    else:
        form = NewsLetterForm()
    
    context = {
        'form': form,
        'sliders':slider
    }
    return render(request, 'blog/newsletter.html', context)

# stations of the cross
# @login_required(login_url ='authentications:loggin')
def opening_prayer(request):
    slider = Slider.objects.all()
    opening = Station_open_closing_prayer.objects.order_by('-date').first()
    context = {
        'opening':opening,
        'sliders':slider,
    }
    return render(request, 'blog/opening_prayers.html', context)

# @login_required(login_url ='authentications:loggin')
def closing_prayer(request):
    intro =PrayerIntro.objects.all().order_by('-post_date')
    slider = Slider.objects.all()
    stations = Stationofcross.objects.all()
    closing = Station_open_closing_prayer.objects.order_by('-date').first()
    context = {
        'closing':closing,
        'sliders':slider,
        'intro':intro,
        'stations':stations
    }
    return render(request, 'blog/closing_prayer.html', context)

# @login_required(login_url ='authentications:loggin')
def all_stations_cross(request):
    slider = Slider.objects.all()
    stationintro = Station_open_closing_prayer.objects.order_by('-date').first()
    stations = Stationofcross.objects.all()
  
    rondom_nov = Stationofcross.objects.order_by('?').first()
    # search
    search_station = stationsearch(request) 
    # end   
    context = {
        'searches':search_station,
        'random':rondom_nov,
        'sliders':slider,
        'stations':stations,
        'stationintro':stationintro,       
       
    }
    return render(request, 'blog/stations_of_the_cross.html', context)

# @login_required(login_url ='authentications:loggin')
def station_details(request, station_id):
    my_blog =My_blog.objects.all()
    slider = Slider.objects.all()
    prayers = Prayers.objects.all()
    stations_detail =Stationofcross.objects.get(title=station_id)
    stations = Stationofcross.objects.all()
    previous_station = Stationofcross.objects.filter(number_of_stations=stations_detail.number_of_stations - 1).first()
    next_station = Stationofcross.objects.filter(number_of_stations=stations_detail.number_of_stations + 1).first()
    # next_station = Stationofcross.objects.filter(date__gt=stations_detail.date).order_by('date').first()
    

    # search
    search_station = stationsearch(request) 
    # end

    
    context = {
        'searches':search_station,
        'my_blog':my_blog,
        'sliders':slider,
        'prayers':prayers,
        'stations_detail':stations_detail,
        'stations':stations,
        'next_station':next_station,
        'previous_station':previous_station,
        
        
    }
    
    return render(request, 'blog/stations_detail.html', context)

# @login_required(login_url ='authentications:loggin')
def all_prayers(request):
    dailyprayer = Dailyprayer.objects.order_by('-date_posted').first()
    all_prayers = Prayers.objects.order_by('?').first()
    
    slider = Slider.objects.all()
    prayers = Prayers.objects.all()
    # search
    search_station = prayersearch(request) 
    # end
    context ={
        'searches':search_station,
        'all_prayers':all_prayers,
        'prayers':prayers,
        'sliders':slider,
        'dailyprayer':dailyprayer,
        
    }
    return render(request, 'blog/all_prayers.html', context)

def unsubscrib(request):
    user = request.user
    subscribed = SubscribedUser.objects.filter(unsubscribe__in = request.user)
    if subscribed:
        subscribed.delete()
        return redirect('home')

    return redirect('home')

    
# @login_required(login_url ='authentications:loggin')        
def dailyprayer(request):
    slider = Slider.objects.all()
    if request.method == 'POST':
        form = dailyPrayersForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            prayer = form.cleaned_data['prayer']
            Dailyprayer.objects.create(title=title, prayer=prayer)
            # messages.error(request, 'Daily prayer posted!!')
            return redirect('dailyprayer')
    else:
        form = dailyPrayersForm()

    context = {
        'form': form,
        'sliders':slider,
    }

    return render(request, 'blog/dailyprayer.html', context)


# @login_required(login_url ='authentications:loggin')
def deleteBlog(request, id):
    myBlog =My_blog.objects.get(id=id)
    myBlog.delete()
    return redirect('home')

# @login_required(login_url ='authentications:loggin')
def deleteComent(request, blog_id):
    
    comment =Comment.objects.get(id=blog_id)
    if comment.user ==request.user:
        comment.delete()
    
    # return redirect(request.META.get('HTTP_REFERER'))
    return redirect(reverse('blog_details', kwargs={'id': comment.blog.id}))

# delete nove_na
# @login_required(login_url ='authentications:loggin')
def deleteNovenaComent(request, novena_id):
    
    comment =NovenaComment.objects.get(id=novena_id)
    if comment.user ==request.user:
        comment.delete()
    
    # return redirect(request.META.get('HTTP_REFERER'))
    return redirect(reverse('novena_details', kwargs={'id': comment.novenas.id}))

# @login_required(login_url ='authentications:loggin')
def dashbord(request):
    slider = Slider.objects.all()
    context = {
        
        'sliders':slider,
        
    }
    return render(request, 'blog/dashbord.html', context)

# @login_required(login_url ='authentications:loggin')
def home(request):
    dailyprayer = Dailyprayer.objects.order_by('-date_posted').first()
    my_blog =My_blog.objects.all().order_by('-post_date')
    intro =PrayerIntro.objects.all().order_by('-post_date')
    slider = Slider.objects.all()
    prayers = Prayers.objects.all()[0:20]
    # pagination
    paginator = Paginator(my_blog, 3)
    page_number = request.GET.get('page')
    try:

        page_obj =paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj =paginator.page(1)
    except EmptyPage:
        page_obj =paginator.page(paginator.num_pages)
    # end of pagination
    comment_count =Comment.objects.filter()
    comment_no=comment_count.count()
      
    
    novena =Novena.objects.all()[0:6]

    # search
    search_blog = blogsearch(request) 
    # end
    context = {
        'searches':search_blog,
        'dailyprayer':dailyprayer,
        'my_blog':my_blog,
        'sliders':slider,
        'prayers':prayers,
        'page_obj':page_obj,
        'novena':novena,
        'intro':intro,
        'comment_count':comment_no
    }
    return render(request, 'blog/home.html', context)



# @login_required(login_url ='authentications:loggin')
def galary(request):
    slider = Slider.objects.all()
    prayers = Prayers.objects.all()
    
    
    galary = My_blog.objects.all()
    # pagination
    paginator = Paginator(galary, 50)
    page_number = request.GET.get('page')
    try:

        page_obj =paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj =paginator.page(1)
    except EmptyPage:
        page_obj =paginator.page(paginator.num_pages)
    # end of pagination

    context ={
        'page_obj':page_obj,
        'prayers':prayers,
        'sliders':slider,
        
    }
    return render(request, 'blog/galary.html', context)

# @login_required(login_url ='authentications:loggin')
def message(request, id):
    blog = My_blog.objects.get(id=id)
    comment =Comment.objects.filter(blog =blog)
    comment_count =comment.count()

    return render(request, 'blog/home.html', {'comment_count':comment_count})


# @login_required(login_url ='authentications:loggin')
def prayer_details(request, id):
    detail = Prayers.objects.get(id =id)
    novena =Novena.objects.all()[0:4]
    slider = Slider.objects.all()
    my_blog =My_blog.objects.all()
    
    #search 
    search_prayer = prayersearch(request)
    context ={
        'searches':search_prayer,
        'details':detail,
        'sliders':slider,
        'novena':novena,
        'blog':my_blog,
        'searches':search_prayer,
    }
    return render(request, 'blog/prayer_detail.html', context)

# @login_required(login_url ='authentications:loggin')
def blog_details(request, id):
    users = request.user
     
    my_blog =My_blog.objects.get(id=id)
    slider = Slider.objects.all()
    
    prayers = Prayers.objects.all()
    novena =Novena.objects.all()[0:4]
    comment_no =Comment.objects.filter(blog=my_blog).count()
    comment = Comment.objects.filter(blog = my_blog).order_by('-post_date')
    # search
    search_blog =blogsearch(request)       
    # end

    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comments =Comment(post_body =form.cleaned_data['post_body'],
                blog = my_blog, user=users)
            comments.save()
            return redirect(f'/blog_details{id}')
            
    
    else:
        form =CommentForm()
    context ={
        'searches':search_blog,
        'blog':my_blog,
        'sliders':slider,
        'prayers':prayers,
        'novena':novena,
        'form':form,
        'comment_no':comment_no,
        'comments':comment,

    }
    return render(request, 'blog/blog_detail.html', context)

# @login_required(login_url ='authentications:loggin')
def all_novena(request):
    slider = Slider.objects.all()
    prayers = Prayers.objects.all()
    novena = Novena.objects.all()
    rondom_nov = Novena.objects.order_by('?').first()
    # search
    search_novena =novenasearch(request)       
    # end
    context = {
        'searches':search_novena,
        'random':rondom_nov,
        'sliders':slider,
        'prayers':prayers,
        'novena':novena,
        
       
    }
    return render(request, 'blog/all_novena.html', context)

# @login_required(login_url ='authentications:loggin')    
def novena_details(request, id):
    users = request.user
    my_blog =My_blog.objects.all()
    # my_novena =Novena.objects.all()
    slider = Slider.objects.all()
    prayers = Prayers.objects.all()
    novena =Novena.objects.get(id=id)
    comment = NovenaComment.objects.filter(novenas = novena).order_by('-post_date')

    day_of_nov = Days.objects.filter(novena = novena)
    # search
    search_novena =novenasearch(request)       
    # end
    
    if request.method =='POST':
        form = NovenaCommentForm(request.POST)
        if form.is_valid():
            comments = NovenaComment(post_body = form.cleaned_data['post_body'], novenas = novena, user=users)
            comments.save()
            return redirect(f'/novena_details{id}')

    else:
        form =CommentForm()


    context = {
        'searches':search_novena,
        'my_blog':my_blog,
        'sliders':slider,
        'prayers':prayers,
        'novenas':novena,
        'form':form,
        'comments':comment,
        'days':day_of_nov,
    }
    return render(request, 'blog/novena_detail.html', context)


# @login_required(login_url ='authentications:loggin') 
def blog_post(request):
    slider = Slider.objects.all()
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
               
    else:
        form =PostForm()
        return render(request, 'blog/post_page.html', {'form':form, 'sliders':slider})

@login_required(login_url ='authentications:loggin')
def liked_post(request, id):
    new_likes(request)
    return HttpResponseRedirect(reverse('blog_details', args =[str(id)]))

@login_required(login_url ='authentications:loggin')
def liked_main_blog(request):
    new_likes(request)
    return redirect('home')


def aboutview(request):
    about = About_us.objects.all()
    slider = Slider.objects.all()

    context={
        'about':about,
        'sliders':slider
    }
    return render(request, 'blog/about.html', context)

class deleteComentsView(DeleteView):
    model = Comment
    success_url =reverse_lazy('blog_details', args =[str(id)])

class novenaView(DetailView):
    model = Novena
    template_name = 'blog/novena_detail.html'


