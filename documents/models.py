import os
from django.db import models
from django.dispatch import receiver


class Category(models.Model):
    CATEGORY_ID_CHOICES = [
        (1, "Учредительный документ"),
        (2, "Общее собрание"),
        (3, "Работа правления"),
        (4, "Работа учредительной комиссии"),
        (5, "Финансовая отчетность"),
    ]
    CATEGORY_NAME_CHOICES = [
        ("Учредительный документ", "Учредительный документ"),
        ("Общее собрание", "Общее собрание"),
        ("Работа правления", "Работа правления"),
        ("Работа учредительной комиссии", "Работа учредительной комиссии"),
        ("Финансовая отчетность", "Финансовая отчетность"),
    ]
    id = models.IntegerField(choices=CATEGORY_ID_CHOICES, primary_key=True, unique=True)
    name = models.CharField(choices=CATEGORY_NAME_CHOICES, max_length=128, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Directory(models.Model):
    name = models.CharField(max_length=128, unique=False)
    date_add = models.DateTimeField(null=False)
    document_type = models.ForeignKey(to=Category, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'директорию'
        verbose_name_plural = 'Директории'

    def __str__(self):
        return f'{self.name}'


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
