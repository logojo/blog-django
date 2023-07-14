from django.db import models
from django.conf import settings

from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

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

    objects = PostManager()


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title