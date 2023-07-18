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
   
    #procedimiento de busqueda por palabra clave o categoria
    def buscar_post(self, kword, category):         
        #verificando si se ha enviado una categoria por url
        print('category')
        print(category)
        if len(category) > 0:
            return self.filter(
                Category__short_name = category,
                title__icontains = kword,
                public=True,
            ).order_by('-created')
        else :
            return self.filter(
                title__icontains = kword,
                public=True,
            ).order_by('-created')

       
        
