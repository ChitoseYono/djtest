from django.contrib import admin

# Register your models here.
from djtest import models

admin.site.register(models.Log)
