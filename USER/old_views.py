from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout as aut_logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email
from .models import Contact_us_page
from django.http import JsonResponse
from django.urls import reverse_lazy
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_POST
# import time
# Create your views here.
def Sign_in(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username')
        password = request.POST.get('pass')
        

        # Check if the input is an email address
        if '@' in username_or_email:
            # If it's an email address, try to get the user with that email
            try:
                user = User.objects.get(email=username_or_email)
            except User.DoesNotExist:
                user = None
        else:
            # If it's not an email address, try to get the user with that username
            user = User.objects.filter(username=username_or_email).first()

        if user is None:
            # Display an error message if the user does not exist
            messages.error(request, 'Invalid username or email')
            return redirect(reverse_lazy('user:login'))

        # Authenticate the user with the provided username/email and password
        authenticated_user = authenticate(request, username=user.username, password=password)

        if authenticated_user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid password")
            return redirect(reverse_lazy('user:login'))
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, authenticated_user)
            if 'next' in request.POST:
                next = request.POST.get('next').strip('/')
                try:
                    return redirect(reverse_lazy('home:'+ next))
                
                except:
                    return redirect(reverse_lazy('order:'+ next))
            return redirect(reverse_lazy('home:hdashboard'))
    return render (request,'user/login.html')

def Sign_up(request):

    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1==pass2:
            user = User.objects.filter(username=uname)
            
            if user.exists():
                # Display an information message if the username is taken
                messages.info(request, "Username already taken!")
                return redirect(reverse_lazy('user:signup'))
            if len(pass1) <8:
            # Display an error message if password less than 8
                messages.error(request, "password is too short")
                return redirect(reverse_lazy('user:signup'))
            if validate_email(email):
                messages.info(request, "invalid email")
                return redirect(reverse_lazy('user:signup'))
            
            # Create a new User object with the provided information
            user = User.objects.create_user(
                username=uname,
                email=email
            )
            
            # Set the user's password and save the user object
            user.set_password(pass1)
            user.save()
        
            # Display an information message indicating successful account creation
            messages.info(request, "Account created Successfully!")
            return redirect(reverse_lazy('user:login'))
        else:
            messages.info(request,'please make sure to confirm the password correctly')
            return redirect(reverse_lazy('user:signup'))
    return render (request,'user/register.html')

def home_page(request):
    return render(request, 'base1.html')
        

def portfolio_detail(request):
    return render(request,'portfolio-details.html')



def service_details(request):
    return render(request,'service-details.html')

def contactus(request):

#     form = Contact_form()
#     if request.method == 'POST':
#         form = Contact_form(request.POST)
#         if form.is_valid():
#             form.save()

#     else:
#         form = Contact_form()
        # name = request.POST.get('name')
        # print(name)
        # email = request.POST.get('email')
        # subject = request.POST.get('subject')
        # print(subject)
        # message = request.POST.get('message')
        # Contact_us.objects.create(name=name, email=email, subject=subject, message=message)
    return render(request,'contactus.html')



def logout_page(request):
    if request.method == 'POST':
        aut_logout(request)
        return redirect(reverse_lazy('home:home_page'))
