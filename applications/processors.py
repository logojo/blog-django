from applications.home.models import Home

#procesor para recuperar telefono y correo de registro home

def home_contact(request):
    home = Home.objects.latest('created')
    return { 
        'email': home.contact,
        'phone': home.phone
    }