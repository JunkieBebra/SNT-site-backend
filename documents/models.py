import os

from django.db import models
from django.dispatch import receiver


class Directory(models.Model):
    name = models.CharField(max_length=128, unique=False)
    date_add = models.DateTimeField(null=False)
    DOCUMENT_TYPE_CHOICES = [
        ("CD", "Учредительный документ"),
        ("GM", "Общее собрание"),
        ("BW", "Работа правления"),
        ("СС", "Работа учредительной комиссии"),
        ("FS", "Финансовая отчетность"),
    ]
    document_type = models.CharField(max_length=2, choices=DOCUMENT_TYPE_CHOICES, default="CD")

    class Meta:
        verbose_name = 'директорий'
        verbose_name_plural = 'Директории'


class Document(models.Model):
    name = models.CharField(max_length=128, unique=False)
    date_add = models.DateTimeField(null=False)
    file = models.FileField(upload_to='documents/')
    directory = models.ForeignKey(to=Directory, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'файл'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return f'{self.name}'


@receiver(models.signals.post_delete, sender=Document)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)


@receiver(models.signals.pre_save, sender=Document)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = Document.objects.get(pk=instance.pk).file
    except Document.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
