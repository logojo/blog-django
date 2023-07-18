from datetime import timedelta, datetime

from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
from django.template.defaultfilters import slugify


from ckeditor_uploader.fields import RichTextUploadingField

from model_utils.models import TimeStampedModel
from .managers import PostManager

# Create your models here.
class Category(TimeStampedModel):
    short_name = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Tag(TimeStampedModel):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name
    
class Post(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    Category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE
    )
    Tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=200)
    resume = models.TextField(max_length=50)
    content = RichTextUploadingField()
    public = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='Posts', max_length=100)
    cover = models.BooleanField(default=False)#portada
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, max_length=300, blank=True)

    objects = PostManager()


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
    
    #esta funcion se utiliza para generar el sitemap 
    def get_absolute_url(self):
        #definiendo como se creara la url de seo
        return reverse_lazy(
            'post_app:detail',
            kwargs={ 'slug': self.slug }
        )
    
    def save(self, *args, **kwargs):
        #calculamos el ttal de segundo de l hora actual
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )

        seconds = int(total_time.total_seconds())
        #generando url 
        #concatendando dos cadenas
        #la funcion str() convierte a cadenas 
        slug_unique = '%s %s' % (self.title, str(seconds))


        #generando slug y asignadoselo al campo slug
        self.slug = slugify(slug_unique) 
        #sobre escribiendo metodo save
        super(Post, self).save(*args, **kwargs)