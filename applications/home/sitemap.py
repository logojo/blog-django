from datetime import datetime
from django.urls import reverse_lazy
from django.contrib.sitemaps import Sitemap


#modelos a incluir en el sitemap
from applications.post.models import Post

class PostSitemap(Sitemap):
    #fecuencia de cambiion al sitio
    changefreq = 'weekly'
    #priodidad en el seo
    priority = 0.8
    protocol = 'https'

    #items a incluir
    def items(self):
        return Post.objects.filter(public=True)
    
    #orden de creación
    #obj se refiere al modelo en este cas Post
    def lastmod(self, obj):
        return obj.created
    
#redefiniendo el sitemap
class Sitemap(Sitemap):
    protocol = 'https'

    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names
    
    def changefreq(self, obj):
        return 'weekly'
    
    #funciones que podemos sobreescribir para crear ek sitemao
    def lastmod(self, obj):
        return datetime.now()
    
    def location(self, obj):
         return reverse_lazy(obj)

