from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, get_user_model
# from blog.forms import UserCreationForm, CustomUserCreationForm
from blog.models import Slider, SubscribedUser
from blog.like import slider
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from authentications.forms import NewsletterForm
from django.core.mail import EmailMessage

# User =get_user_model




def subscribe(request):
    if request.method =='POST':
        name =request.POST.get('name', None)
        email =request.POST.get('email', None)

        if not name or not email:
            messages.error(request, 'You must type a legit name and email to subscribe')
            return redirect('/')
        if get_user_model().objects.filter(email=email).first():
            messages.error(request, f'You already subscribe with this {email}.')
            return redirect(request.META.get('HTTP_REFERER', '/'))
        subscribe_user=SubscribedUser.objects.filter(email=email).first()
    if subscribe_user:
        messages.error(request, f'{email} email address is already a subscriber')
        return redirect('/')
    try:
        validate_email(email)
    except ValidationError as e:
        messages.erro(request, e.messages[0])
        return redirect('/')
    subscribe_model_instance =SubscribedUser()
    subscribe_model_instance.name = name
    subscribe_model_instance.email =email
    subscribe_model_instance.save()
    messages.success(request, f'{email} email was subscribed successfully')
    return redirect('/')


def loggin(request):
    sliders = Slider.objects.all()
    if request.method =='POST':
        username =request.POST.get('username')
        password =request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials') 
            return redirect('authentications:loggin')
        
    else:
        return render(request, 'authentications/login.html', {'sliders':sliders})


def signup(request):
    sliders = Slider.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exist')
                return redirect('authentications:signup')
            elif User.objects.filter(email =email).exists():
                messages.error(request, 'Email already exist')
                
                return redirect('authentications:signup')
            else:
                user =User.objects.create_user(username = username, email=email, password=password1)
                user.save()
                messages.success(request, 'Signup Successful')
                return redirect('authentications:loggin')
        else:
            messages.error(request, 'Password not match')
            return redirect('authentications:signup')
    else:
        return render(request, 'authentications/signup.html', {'sliders':sliders})

def logout(request):
    auth.logout(request)
    messages.success(request, 'You logout! Loging again?')
    return redirect('authentications:loggin')
           


