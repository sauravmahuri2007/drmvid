import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.timezone import now

from utils.validators import MimeTypeValidator

# Helper functions

# This allows django to upload file to any path even outside project directory
upload_storage = FileSystemStorage(
    location=settings.VID_UPLOAD_PATH, base_url=settings.VID_UPLOAD_PATH)

def get_filename_extension(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def get_current_date_time():
    timestamp = now()
    _date = timestamp.strftime('%Y-%m-%d')  # eg: '2019-08-16'
    _time = timestamp.strftime('%H%M%S%f')  # eg: '234421718277'
    return _date, _time

def file_upload_path(instance, filename):
    name, ext = get_filename_extension(filename)
    current_date, current_time = get_current_date_time()
    new_name = '{0}_{1}{2}'.format(instance.name, current_time, ext)
    return os.path.join(current_date, new_name)

def mime_validator(value):
    if hasattr(settings, 'VID_ALLOWED_MIMETYPES'):
        allowed_mimetypes = settings.VID_ALLOWED_MIMETYPES
    else:
        allowed_mimetypes = []
    validator = MimeTypeValidator(allowed_mimetypes=allowed_mimetypes)
    return validator(value)

def extension_validator(value):
    if hasattr(settings, 'VID_ALLOWED_EXTENSIONS'):
        allowed_extensions = settings.VID_ALLOWED_EXTENSIONS
    else:
        allowed_extensions = []
    validator = FileExtensionValidator(allowed_extensions=allowed_extensions)
    return validator(value)


# Create your models here.

class DRMVideo(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(max_length=200, blank=False, null=False)
    video = models.FileField(upload_to=file_upload_path, max_length=500,
                             null=False, storage=upload_storage, blank=False,
                             validators=[extension_validator, mime_validator])
    created_dtm = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'drm_video'

    def __str__(self):
        return self.name