from django.shortcuts import render, redirect
from homeApp.models import Category, FocolarePassword, Contact, SaintOfTheDay, Sacramental
from blog.models import My_blog, Slider, Prayers, Novena, StationsImages, Dailyprayer
from django.core.paginator import Paginator,  EmptyPage, PageNotAnInteger
from blog.search import blogsearch
from django.contrib import messages
from django.db.models import Count
from blog.like import count

# Create your views here.
def index(request):
    
    all_blogs = My_blog.objects.all().order_by('-post_date')[:3]
    last_blog = My_blog.objects.all().order_by('post_date')[:3]
    first_blog = all_blogs.first()
    dailyprayer = Dailyprayer.objects.last()

    focolare = FocolarePassword.objects.all().order_by('-posted_date')[:4]
    sacrament = Sacramental.objects.all().order_by('-created_at')[:4]
    saints = SaintOfTheDay.objects.all().order_by('-created_at')[:4]

    prayer = Prayers.objects.all().order_by('date_posted')[:4]
    novena =Novena.objects.all()[:6]
    stations1 = StationsImages.objects.first()
    stations2 = StationsImages.objects.last()
    stations3 = StationsImages.objects.all()[3:5]

    search_blog = blogsearch(request)
    counting = count(request)

    context = {
        'dailys':dailyprayer,
        'blogs':all_blogs,
        'first':first_blog,
        'last':last_blog,
        'prayers':prayer,
        'focolares':focolare,
        'sacraments':sacrament,
        'saints':saints,
        'novenas':novena,
        'stations':stations1,
        'stations2':stations2,
        'stations3':stations3,
        'searches':search_blog,
        'count':counting
        
    }

    return render(request, 'homeApp/index.html', context)

def sacrament(request):
    counting = count(request)
    sacrament = Sacramental.objects.all()
    saints = SaintOfTheDay.objects.all().order_by('-updated_at')[:4]
    blog = My_blog.objects.all().order_by('-post_date')[:4]

    # pagination
    paginator = Paginator(sacrament, 3)
    page_number = request.GET.get('page')
    try:

        page_obj =paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj =paginator.page(1)
    except EmptyPage:
        page_obj =paginator.page(paginator.num_pages)
    # end of pagination


    context = {
        'sacraments':page_obj,
        'saints':saints,
        'blogs':blog,
        'count':counting
    }
    return render(request, 'homeApp/sacramental.html', context)

def sacramental_detail(request, sac_id):
    counting = count(request)
    password = Sacramental.objects.get(id = sac_id)
    blog_post = My_blog.objects.all().order_by('-post_date')[:4]

    sacrament = Sacramental.objects.all().exclude(id=sac_id).order_by('-created_at')[:12]
    saints = SaintOfTheDay.objects.all().order_by('-updated_at')[:4]

    context = {
        'passwords':password,
        'blogs':blog_post,
        'count':counting,
        'sacraments':sacrament,
        'saints':saints
    }
    return render(request, 'homeApp/sacramental_single.html', context)

def allsaints(request):
    counting = count(request)
    saints = SaintOfTheDay.objects.all()
    # saints = SaintOfTheDay.objects.all().order_by('-updated_at')[:4]
    blog = My_blog.objects.all().order_by('-post_date')[:4]
    sacrament = Sacramental.objects.all().order_by('-created_at')[:4]

    # pagination
    paginator = Paginator(saints, 3)
    page_number = request.GET.get('page')
    try:

        page_obj =paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj =paginator.page(1)
    except EmptyPage:
        page_obj =paginator.page(paginator.num_pages)
    # end of pagination


    context = {
        'saints':page_obj,
        # 'saints':saints,
        'blogs':blog,
        'count':counting,
        'sacraments':sacrament
    }
    return render(request, 'homeApp/saints.html', context)

def saint_detail(request, saint_id):
    counting = count(request)
    saint = SaintOfTheDay.objects.get(id = saint_id)
    blog_post = My_blog.objects.all().order_by('-post_date')[:4]

    sacrament = Sacramental.objects.all().order_by('-created_at')[:4]
    saints = SaintOfTheDay.objects.all().exclude(id=saint_id).order_by('-created_at')[:12]


    context = {
        'saint':saint,
        'saints':saints,
        'sacraments':sacrament,
        'blogs':blog_post,
        'count':counting
    }
    return render(request, 'homeApp/saints_single.html', context)



def all_blogs(request):
    counting = count(request)
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
        'count':counting
    }
    return render(request, 'homeApp/blogs.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if not name:
            messages.info(request, 'You have to enter your name first')
            return redirect('homeApp:contact')
        elif not subject:
            messages.info(request, 'You must input the subject')
            return redirect('homeApp:contact')
        elif not message:
            messages.info(request, 'You must enter your message')
            return redirect('homeApp:contact')
        elif not email:
            messages.info(request, 'Your email cannot be empty')
            return redirect('homeApp:contact')

        # If all fields are filled, save the data
        userData, created = Contact.objects.get_or_create(
            name=name,
            subject=subject,
            email=email,
            message=message
        )

        if created:
            userData.save()
            messages.info(request, 'Message sent successfully! We will get back to you.')
        else:
            messages.info(request, 'Message already exists.')

        return redirect('homeApp:contact')

    return render(request, 'homeApp/contact.html')

def contact_messages(request):
    message = Contact.objects.all()
    counting = count(request)
    slider = Slider.objects.all()

    if request.method =='POST':
        message_id = request.POST.get('message_id')
        update = Contact.objects.get(id = message_id)



        update.read = True
        update.save()

        
        return redirect('homeApp:contact_messages')

    context = {
        'contacts':message,
        'count':counting,
        'sliders':slider
    }
    return render(request, 'blog/all_contact_messages.html', context)

def delete_contact(request, message_id):
    user = request.user
    contact = Contact.objects.get(id=message_id)

    if user.is_staff:
        contact.delete()
        messages.info(request, 'You deleted this message')
        return redirect('homeApp:contact_messages')
    messages.info(request, 'You are not authorize to delete this message')
    return redirect('homeApp:contact_messages')

