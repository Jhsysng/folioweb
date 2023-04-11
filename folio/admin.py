from django.contrib import admin
from .models import Portfolio
from .models import TechTag,LangTag
from markdownx.admin import MarkdownxModelAdmin

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)



admin.site.register(Portfolio, MarkdownxModelAdmin)
admin.site.register(TechTag, TagAdmin)
admin.site.register(LangTag, TagAdmin)
# Register your models here.
