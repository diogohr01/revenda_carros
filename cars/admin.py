from django.contrib import admin
from cars.models import Car
from cars.models import Brand

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    '''list_display -> lista no admin cada um desses campos do que tu pesquisar'''
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')
    
admin.site.register(Car, CarAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
admin.site.register(Brand, BrandAdmin)

    