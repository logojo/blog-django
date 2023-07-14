from django.contrib import admin

from .models import Home, Subscriber, Contact

# Register your models here.

admin.site.register(Home)
admin.site.register(Subscriber)
admin.site.register(Contact)