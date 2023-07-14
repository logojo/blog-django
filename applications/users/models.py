from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

# Create your models here.
#PermissionsMixin permite controlar la creacion de usuarios desde la consola
class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
        ('O', 'Otro')
    )
    email = models.EmailField(unique=True)
    full_name = models.CharField('nombre', max_length=100)
    ocupation = models.CharField('Ocupacion',max_length=30, blank=True)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    date_birth = models.DateField('Fecha de nacimiento',  blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    #esto especifica cual campo se usara para hacer el logueo
    USERNAME_FIELD = 'email'
    #campos que solicitara ademas del username y el password para crear el usuario
    REQUIRED_FIELDS = ['full_name',]

    objects = UserManager()

    def __str__(self):
        return  str(self.id) + ' - ' + self.full_name

    def get_short_name(self):
        return self.full_name