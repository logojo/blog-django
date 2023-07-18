"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

#archivo de configuracion de url de imagenes
from django.conf import settings
from django.conf.urls.static import static

#sitemaps para seo
from django.contrib.sitemaps.views import sitemap
from applications.home.sitemap import PostSitemap, Sitemap


#urls principales
urlpatterns_main = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.post.urls')),
    re_path('', include('applications.favorite.urls')),
    #urls para ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urls para sitemap seo

sitemaps = {
    'site' : Sitemap(
        [
            'home_app:home'
        ]
    ),
    'posts' : PostSitemap
}

urlpatterns_sitemap = [
     path(
        'sitemap.xml', 
        sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views',
     )
]

urlpatterns = urlpatterns_main + urlpatterns_sitemap