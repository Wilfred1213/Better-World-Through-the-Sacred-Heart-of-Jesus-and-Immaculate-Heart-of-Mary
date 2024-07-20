from django.shortcuts import render
from homeApp.models import Category, FocolarePassword
from blog.models import My_blog, Prayers, Novena, StationsImages, Dailyprayer
from django.core.paginator import Paginator,  EmptyPage, PageNotAnInteger
from blog.search import blogsearch
# Create your views here.
def index(request):
    
    all_blogs = My_blog.objects.all().order_by('-post_date')[:3]
    last_blog = My_blog.objects.all().order_by('post_date')[:3]
    first_blog = all_blogs.first()
    dailyprayer = Dailyprayer.objects.first()

    focolare = FocolarePassword.objects.all().order_by('-posted_date')[:4]
    prayer = Prayers.objects.all().order_by('date_posted')[:4]
    novena =Novena.objects.all()[:6]
    stations1 = StationsImages.objects.first()
    stations2 = StationsImages.objects.last()
    stations3 = StationsImages.objects.all()[3:5]

    search_blog = blogsearch(request)

    context = {
        'dailys':dailyprayer,
        'blogs':all_blogs,
        'first':first_blog,
        'last':last_blog,
        'prayers':prayer,
        'focolares':focolare,
        'novenas':novena,
        'stations':stations1,
        'stations2':stations2,
        'stations3':stations3,
        'searches':search_blog,
        
    }

    return render(request, 'homeApp/index.html', context)

def focolare(request):
    password = FocolarePassword.objects.all()
    blog_post = My_blog.objects.all().order_by('-post_date')[:4]

    # pagination
    paginator = Paginator(password, 3)
    page_number = request.GET.get('page')
    try:

        page_obj =paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj =paginator.page(1)
    except EmptyPage:
        page_obj =paginator.page(paginator.num_pages)
    # end of pagination


    context = {
        'passwords':page_obj,
        'blogs':blog_post
    }
    return render(request, 'homeApp/password.html', context)

def focolare_detail(request, foco_id):
    password = FocolarePassword.objects.get(id = foco_id)
    blog_post = My_blog.objects.all().order_by('-post_date')[:4]

    context = {
        'passwords':password,
        'blogs':blog_post
    }
    return render(request, 'homeApp/foco_single.html', context)

def all_blogs(request):
    password = FocolarePassword.objects.all().order_by('-posted_date')[:4]
    # blog_post = My_blog.objects.all().order_by('post_date')[:4]
    blog = My_blog.objects.all()

    # pagination
    paginator = Paginator(blog, 3)
    page_number = request.GET.get('page')
    try:

        page_obj =paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj =paginator.page(1)
    except EmptyPage:
        page_obj =paginator.page(paginator.num_pages)
    # end of pagination

    search_blog = blogsearch(request)


    context = {
        'page_obj':page_obj,
        'passwords':password,
        'searches':search_blog,
    }
    return render(request, 'homeApp/blogs.html', context)

