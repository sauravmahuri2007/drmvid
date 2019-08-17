from django.contrib import admin

from video_encoding.admin import FormatInline

from .models import DRMVideo


class DRMVideoAdmin(admin.ModelAdmin):
    inlines = (FormatInline,)

    list_display = ('id', 'name', 'description', 'video', 'created_dtm',
         'width', 'height', 'duration')
    list_search = ('name', 'description')


admin.site.register(DRMVideo, DRMVideoAdmin)