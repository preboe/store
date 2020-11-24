from django.forms import ModelChoiceField
from django.contrib import admin


from .models import *





#Мыло с нуля
class soap_from_scratchAdmin(admin.ModelAdmin):


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='soap_from_scratch'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



#Сувенирное мыло
class souvenir_soapAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='souvenir_soap'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


#децкое мыло
class baby_soapAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='baby_soap'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


#Бактериальная мыло
class bacterial_soapAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='bacterial_soap'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



#уходовое мыло
class care_soapAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='care_soap'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


#Мыло скраб
class scrub_soapAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='scrub_soap'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


#Крем мыло
class cream_soapAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='cream_soap'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


#Мыло под нарезку
class bar_soapAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='bar_soap'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


#Парфюм
class hatural_parfumeAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='hatural_parfume'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



#Скраб
class scrubAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='scrub'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(soap_from_scratch, soap_from_scratchAdmin)#мыло с нуля
admin.site.register(souvenir_soap, souvenir_soapAdmin)#сувенирное мыло
admin.site.register(baby_soap, baby_soapAdmin)#децкое мыло
admin.site.register(bacterial_soap, bacterial_soapAdmin)#бактыриальное мыло
admin.site.register(care_soap, care_soapAdmin)#уходовое мыло
admin.site.register(scrub_soap, scrub_soapAdmin)#мыло скраб
admin.site.register(cream_soap, cream_soapAdmin)#крем мыло
admin.site.register(Bar_soap, bar_soapAdmin)#мыло под нарезку
admin.site.register(natural_parfume, hatural_parfumeAdmin)#порфим
admin.site.register(scrub, scrubAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
