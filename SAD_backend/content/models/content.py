from datetime import datetime
import pytz
from django.db import models
from account.models import Member

from content.utils.file_utils import content_file_path


class ContentType(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    @classmethod
    def get_default_type_pk(cls):
        obj, _ = cls.objects.get_or_create(name='other')
        return obj.pk

    def is_compatible_as_attachment(self, attachment_type):
        return ContentType.objects.filter(name=attachment_type, type=f'{self.type}-attachment').exists()


class Library(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(verbose_name='date_created', default=datetime.fromtimestamp(0, tz=pytz.UTC))
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    type = models.CharField(max_length=30, default=ContentType.get_default_type_pk)

    class Meta:
        unique_together = ('name', 'member',)


class Content(models.Model):
    name = models.CharField(max_length=150, blank=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date_created = models.DateTimeField(verbose_name='date_created', default=datetime.fromtimestamp(0, tz=pytz.UTC))
    type = models.ForeignKey(ContentType,
                             default=ContentType.get_default_type_pk,
                             on_delete=models.SET_DEFAULT)
    library = models.ForeignKey(Library, null=True, on_delete=models.CASCADE)
    file = models.FileField(upload_to=content_file_path)
    father_content = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    info = models.CharField(max_length=2000, default='{}')

    @property
    def path(self):
        return self.file.name
