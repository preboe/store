from django.forms import ModelChoiceField
from django.contrib import admin


from .models import *





#Мыло
class soapAdmin(admin.ModelAdmin):


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='soap'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)





#косметика
class cosmeticsAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='cosmetics'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)





#Парфюм
class parfumeAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='hatural_parfume'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)






admin.site.register(Category)
admin.site.register(soap, soapAdmin)#мыло с нуля
admin.site.register(cosmetics, cosmeticsAdmin)#децкое мыло
admin.site.register(perfume, parfumeAdmin)#порфим
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
