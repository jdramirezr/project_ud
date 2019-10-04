"""Platzigram URLs module."""

# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from platzigram import views as local_views
from users import views as users_views


urlpatterns = [

    path('admin/', admin.site.urls),

    path('hello-world/', local_views.hello_world, name='hello_world'),
    path('sorted/', local_views.sort_integers, name='sort'),
    path('hi/<str:name>/<int:age>/', local_views.say_hi, name='hi'),


    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
    path('users/signup/', users_views.signup, name='signup'),
    path('users/new/', users_views.new, name='new'),
    path('users/calculate_address/', users_views.calculate_address, name='calculate_address'),
    path('users/me/profile/', users_views.update_profile, name='update_profile')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
