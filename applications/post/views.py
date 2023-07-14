from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView

from .models import Post, Category


class PostView(ListView):
    template_name = "posts/list.html"
    context_object_name = 'posts'
    paginate_by = 10

    
    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    

    def get_queryset(self):
        #recuperando variable de formulario
        kword = self.request.GET.get('kword','')
        #recuperando valor de url
        category = self.request.GET.get('categoria','')
        #consulta de busqueda
        result = Post.objects.buscar_post(kword, category)
        return result

