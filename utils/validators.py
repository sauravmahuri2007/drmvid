import os
from magic import Magic

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _


@deconstructible
class MimeTypeValidator(object):
    """
    Validates the mime type of inmemory object before uploading to the server.
    Requires python-magic library.
    """

    message = _(
        "File mime type '%(mimetype)s' is not allowed. "
        "Allowed mime types are: '%(allowed_mimetypes)s'."
    )
    code = 'invalid_mimetype'

    def __init__(self, allowed_mimetypes=None, message=None, code=None):
        self.allowed_mimetypes = allowed_mimetypes
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if self.allowed_mimetypes is not None:
            for chunk in value.chunks():
                mimetype = Magic(mime=True).from_buffer(chunk)
                if mimetype not in self.allowed_mimetypes:
                    raise ValidationError(
                        self.message,
                        code=self.code,
                        params={
                            'mimetype': mimetype,
                            'allowed_mimetypes': ', '.join(
                                self.allowed_mimetypes)
                        }
                    )
                return

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.allowed_mimetypes == other.allowed_mimetypes and
            self.message == other.message and
            self.code == other.code
        )