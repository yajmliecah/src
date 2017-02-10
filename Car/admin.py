from django.contrib import admin

from Car.models import Brand, Spec


class BrandAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'logo', 'description')
    prepopulated_fields = {'slug': ('name',)}


class SpecAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Brand, BrandAdmin)
admin.site.register(Spec, SpecAdmin)
