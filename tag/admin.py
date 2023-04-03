from django.contrib import admin
from .models import TechTag,LangTag


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(TechTag, TagAdmin)
admin.site.register(LangTag, TagAdmin)

# Register your models here.
