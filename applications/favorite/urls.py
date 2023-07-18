from django.urls import path
from . import views

app_name = "favorite_app"

urlpatterns = [
    path('perfil', views.ProfileView.as_view(), name='perfil',),  
    path('create-favorite/<pk>', views.CreateFavorite.as_view(), name='create-favorite',),  
    path('delete-favorite/<pk>', views.FavoriteDelete.as_view(), name='delete-favorite',),  
]