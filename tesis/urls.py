"""Platzigram URLs module."""

# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from tesis import views as local_views
from app import views as users_views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
    path('users/signup/', users_views.signup, name='signup'),
    path('users/new/', users_views.new, name='new'),
    path('', users_views.page, name='page'),
    path('users/info', users_views.info, name='info'),
    path('users/info_construccion', users_views.info_construccion, name='info_construccion'),
    path('users/stadistic/', users_views.stadistic, name='stadistic'),
    path('users/weight_calculation/', users_views.weight, name='weight'),
    path('users/inicio/', TemplateView.as_view(template_name="video.html"),  name="init_video"),
    path('users/ais/', users_views.Ais.as_view(), name='ais'),
    path('users/nsr/', users_views.Nsr10.as_view(), name='nsr'),
    path('users/soil/', users_views.Soil.as_view(), name='soil'),
    path('users/weight/', users_views.Weight.as_view(), name='weight'),
    path('users/indice/', users_views.Indice.as_view(), name='indice'),
    path('users/ais/<int:pk>/', users_views.AisDetail.as_view(), name='ais_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)








