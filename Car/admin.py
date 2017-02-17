from django.contrib import admin

from Car.models import Brand, Spec


class BrandAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'logo', 'description')
    prepopulated_fields = {'slug': ('name',)}


class SpecAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'price',)
    list_filter = ('name',)
    search_fields = ('name', 'brand', 'category',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Brand, BrandAdmin)
admin.site.register(Spec, SpecAdmin)
