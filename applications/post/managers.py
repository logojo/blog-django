from django.db import models

class PostManager(models.Manager):
    
    def entrada_portada(self):
       return self.filter(
            public = True,
            cover = True
            #el guion indica que se ordenara por la fecha en orden asendente
        ).order_by('-created').first()
    
    def get_posts(self):
        return self.filter(
            public = True,
            in_home = True
        ).order_by('-created')[:4]
    
    def get_recientes(self):
        return self.filter(
            public = True,
        ).order_by('-created')[:6]
   
        
