#
from django.urls import path
from . import views

app_name = "post_app"

urlpatterns = [
    path('posts', views.PostView.as_view(), name='posts',)
]