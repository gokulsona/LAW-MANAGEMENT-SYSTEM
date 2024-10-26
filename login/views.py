from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from . forms import SignupForm
from django.contrib.auth import logout as logouts
# Create your views here.


#user registration using Form
def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login/')
    else:
        form = SignupForm()
    return render(request, 'register.html', {
        'form' : form
    })
#login using LoginViews in urls.py

#user logout
def logout(request):
    logouts(request)
    return redirect('home')

#user profile (not completed yet)
def user_profile(request):
    return render(request, 'user_profile.html')


def edit_user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)  # Fetch the user by ID
    
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()  # Save the updated profile
            return redirect('login')  # Redirect to a profile detail page
    else:
        form = SignupForm(instance=user)  # Prepopulate the form

    return render(request, 'edit_user_profile.html', {'form': form, 'user': user})
















'''
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return redirect('register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already taken")
                return redirect('register/')
            else:
                user_reg = User.objects.create_user(username=username, email=email, password=password)
                user_reg.save()
                messages.info(request, "Registered Successfully")
                return redirect('login')
        else:
            messages.info(request, "password doesn't match")
            return redirect('register/')

    return render(request, "register.html")



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'invalid password')
            return redirect('login')
        else:
            return redirect('home')
    return render(request, 'login.html')
    '''