from django.db import models
from django.conf import settings

from model_utils.models import TimeStampedModel

from .managers import FavoriteManager
from applications.post.models import Post


# Create your models here.

class Favorite(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_favorites',
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Post, 
        related_name='posts_favorites',
        on_delete=models.CASCADE,
    )

    objects = FavoriteManager()

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return self.post.title