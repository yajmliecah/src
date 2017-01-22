from django.contrib import admin

from Car.models import Condition, Brand, Spec


class ConditionAdmin(admin.ModelAdmin):
	exclude = ('old', 'used')


class BrandAdmin(admin.ModelAdmin):
	fields = ('name',)


class SpecAdmin(admin.ModelAdmin):
	pass

admin.site.register(Condition, ConditionAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Spec, SpecAdmin)
