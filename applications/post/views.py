from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView


class PostView(ListView):
    template_name = "posts/list.html"
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        kword = self.request.GET.get('kword','')
        print(kword)
        return []

