from django.db import models

class FavoriteManager(models.Manager):
    
    def posts_user(self, user):
        return self.filter(
            post__public = True,
            user = user,
        ).order_by('-created')
    