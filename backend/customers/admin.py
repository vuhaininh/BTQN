from django.contrib import admin
from customers import models
# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.CustomerGroup)
