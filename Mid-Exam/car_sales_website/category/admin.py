from django.contrib import admin
from . import models 
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('brandName',)}
    list_display = ['brandName', 'slug']


admin.site.register(models.Brand,CategoryAdmin)