from django.urls import path,include
from . import views

app_name = 'album'
urlpatterns = [
    path('',views.albumHome,name='album'),
    path('blueberry/',views.blueberry,name='blueberry')
]