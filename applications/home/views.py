
from django.shortcuts import render
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy, reverse

from django.views.generic import TemplateView, CreateView

from applications.post.models import Post
from .models import Home
from .forms import subscriberForm


class HomeView(TemplateView):
    template_name = "home/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        #contexto de portada
        #esto se enviara al templete se pueden extraer los datos con el nombre de las variables que va entre []
        context["portada"] = Post.objects.entrada_portada()
        context["posts"] = Post.objects.get_posts()
        context["recientes"] = Post.objects.get_recientes()

        #cargamos el home
        #recuperando el ultimo registro creado
        context["home"] = Home.objects.latest('created')


        #enviando formulario interno a la vista
        #como contexto se puede enviar lo que sea (objetos, formularios, diccionarios, vista, etc)
        context['form'] = subscriberForm
        return context

 
class SubscriberCreateView(CreateView):
    form_class = subscriberForm
    success_url = '.'
 
