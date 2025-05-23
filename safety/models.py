from django.db import models
from django.contrib.auth.models import User as AuthUser
from django.core.validators import MinLengthValidator

class User  ( models.Model ):
    """
    Model to represent a user in the system.
    """
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['name_user']

    def __str__(self):
        return self.name_user
id_user = models.BigAutoField(auto_created=True, primary_key=True)    
name_user = models.CharField(max_length=150, null=False, blank=False)
cpf_cnpj_user = models.CharField(max_length=18, unique=True, null=False, blank=False)
email_user = models.EmailField(max_length=150, unique=True, null=False, blank=False)
cep_user = models.CharField(max_length=11 , null=False, blank=False)
address_user = models.CharField(max_length=255)
number_user = models.CharField(max_length=8)
neighborhood_user = models.CharField(max_length=150)
complement_user = models.CharField(max_length=255)
city_user = models.CharField(max_length=150)    
uf_user = models.CharField(max_length=2, validators= [MinLengthValidator(2)])

class contact_user(models.Model):
    """
    Model to represent a contact user in the system.
    """
    class Meta:
        verbose_name = "Contact User"
        verbose_name_plural = "Contact Users"
        ordering = ['name_user']

    def __str__(self):
        return self.id_user
    id_contact_user = models.BigAutoField(auto_created= True, primary_key=True)
    number_contact_user = models.CharField(max_length=15, null=False, blank=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact_user')

