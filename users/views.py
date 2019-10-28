"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Forms
from users.forms import ProfileForm
from geopy.geocoders import Nominatim

from googlemaps import Client as GoogleMaps
from django.http import HttpResponse


import socket
from ip2geotools.databases.noncommercial import DbIpCity


@login_required
def update_profile(request):
    """Update a user's profile view."""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')

    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )


def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('update_profile')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')


def signup(request):
    """Sign up view."""
    if request.method == 'POST':

        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in user'})

        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')

def new(request):
    if request.method == 'POST':
        return render(request, 'users/signup.html')

def calculate_address(request):

    if request.method == 'POST':
        try:
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            # print(DbIpCity.get(IPAddr, api_key='free'))

            print('++++++++++++++++++++++++++++++++++++++++++')
            print("Your Computer Name is:" + hostname)
            print("Your Computer IP Address is:" + IPAddr)

            # print(response.latitude, response.latitude)
            # print(response.to_json())
            geolocator = Nominatim(user_agent="specify_your_app_name_here")
            location = geolocator.geocode(request.POST['address'])
            print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
            # print('///////////////////////////////////////')
            # print(location.address)

            # print(location.latitude, location.longitude)
            return HttpResponse(location.latitude, location.longitude)

        except:
            return HttpResponse('No se pudo encontrar la direccion')
    else:
        return HttpResponse('fall el internet')

@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('login')
