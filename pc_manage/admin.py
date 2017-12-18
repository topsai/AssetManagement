from django.contrib import admin
from pc_manage import models

# Register your models here.
admin.site.register(models.DepartmentType)
admin.site.register(models.ComputerInfo)
admin.site.register(models.ComputerType)
admin.site.register(models.User)