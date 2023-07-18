from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from .models import Favorite
from applications.post.models import Post


class ProfileView(LoginRequiredMixin, ListView):
    template_name = "favorites/perfil.html"
    context_object_name = 'favorites_user'
    login_url = reverse_lazy('users_app:user-login')

    def get_queryset(self):
        # self.request.user obtiene el usuario activo de la sesion actual
        return Favorite.objects.posts_user(self.request.user)
    
class CreateFavorite(LoginRequiredMixin, View):
    login_url = reverse_lazy('users_app:user-login')

    def post(self, *args, **kwargs):
        #recuperando el usiario
        usuario = self.request.user

        #recuperando post desde url
        post = Post.objects.get(id=self.kwargs['pk'])

        #registrando facoritos
        Favorite.objects.create(
            user = usuario,
            post = post,
        )

        return HttpResponseRedirect( 
            reverse(
                'favorite_app:perfil'
            )
        )
    

class FavoriteDelete(DeleteView):
    model = Favorite
    success_url = '/perfil'


