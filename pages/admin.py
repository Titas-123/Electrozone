from django.contrib import admin
from .models import team
from django.utils.html import format_html
# Register your models here.

class teamadmin(admin.ModelAdmin):
        def thumbnail(self,object):
            return format_html('<img src="{}" width="100" style="border-radius: 50px" />'.format(object.photo.url))

        list_display = ('id','first_name','thumbnail','designation','created_date')
        list_display_links = ('id','thumbnail','first_name')
        search_fields = ('first_name','last_name','designation')
        list_filter = ('designation',)

admin.site.register(team, teamadmin)
