from django.db import models

id_user = models.SlugField(_("id_user"), max_length=10, primary_key=True)    
name_user = models.CharField(max_length=150)
cpf_cnpj_user = models.CharField(max_length=18)
email_user = models.EmailField(max_length=150)
cep_user = models.CharField(max_length=11)
address_user = models.CharField(max_length=255)
number_user = models.CharField(max_length=8)
neighborhood_user = models.CharField(max_length=150)
complement_user = models.CharField(max_length=255)
city_user = models.CharField(max_length=150)    
uf_user = models.(max_length=2)