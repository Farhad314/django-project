from django.urls import path, include
from . import views

app_name = 'carousel'
urlpatterns = [
    path('',views.carou,name='carou'),
    
]