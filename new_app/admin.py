from django.contrib import admin

from new_app import models

# Register your models here.
admin.site.register(models.Login)
admin.site.register(models.seller)
admin.site.register(models.coustmer)
admin.site.register(models.blog)