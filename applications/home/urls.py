#
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path('', views.HomeView.as_view(),name='home',),  
    path('subscriber', views.SubscriberCreateView.as_view(), name='create-subscriber'),
    path('constact', views.ContactCreateView.as_view(), name='create-constact')
]