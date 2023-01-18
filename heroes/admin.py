from django.contrib import admin
from .models import Hero, Element, Country


admin.site.register(Hero)


# admin.site.register(Element, ElementAdmin)

# class ElementAdmin(admin.ModelAdmin):
#     list_display = ['name_element']

# class HeroAdmin(admin.ModelAdmin):
#     list_display = ['city']

# admin.site.register(Element,  ElementAdmin)
# admin.site.register(Hero, HeroAdmin)