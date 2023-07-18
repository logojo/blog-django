from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.
class Home(TimeStampedModel):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    about_title = models.CharField(max_length=50)
    aboout_text = models.TextField()
    contact = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name= 'Pagina Principal'
        verbose_name_plural= 'Pagina Principal'

    def __str__(self):
        return self.title
    
class Subscriber(TimeStampedModel):
    email = models.EmailField()

    class Meta:
        verbose_name = 'Subscritor'
        verbose_name_plural = 'Subscritors'

    def __str__(self):
        return self.email
    
class Contact(TimeStampedModel):
    full_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    message = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.full_name


    



