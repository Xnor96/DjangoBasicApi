from django.contrib import admin
from .models import Programmer

# Register your models here.
#Se registra el modelo para que sea visible atraves del panel de administracion
admin.site.register(Programmer)