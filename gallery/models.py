import os
from django.db import models
from django.dispatch import receiver


class Image(models.Model):
    img = models.ImageField(upload_to='images')
    name = models.CharField(max_length=56, null=False)
    date_add = models.DateTimeField(null=False)

    class Meta:
        verbose_name = 'картинку'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return f'{self.name}, {self.date_add}'


@receiver(models.signals.post_delete, sender=Image)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)


@receiver(models.signals.pre_save, sender=Image)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = Image.objects.get(pk=instance.pk).file
    except Image.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

