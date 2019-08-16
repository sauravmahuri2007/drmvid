from django.contrib import admin
from .models import DRMVideo


class DRMVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'video', 'created_dtm')
    list_search = ('name', 'description')


admin.site.register(DRMVideo, DRMVideoAdmin)