from django.db import models
from user.models import User


class ProminentOnes(models.Model):

    TYPE_CHOICES = [
        ("CR", "Председатель"),
        ("GV", "В составе правления"),
        ("GP", "Член правления"),
        ("OB", "В составе ревизионной комиссии"),
    ]

    user = models.ForeignKey(to=User, on_delete=models.PROTECT)
    date_start = models.DateField()
    date_end = models.DateField()
    type = models.CharField(verbose_name="Тип", choices=TYPE_CHOICES, max_length=2)

    class Meta:
        verbose_name = "ключевое лицо"
        verbose_name_plural = "Ключевые лица"

    def __str__(self):
        if self.type == 'CR':
            return f'Председатель (с {self.date_start} по {self.date_end}) {self.user.last_name}'
        elif self.type == 'GV':
            return f'Состав правления {self.user.last_name}'
        elif self.type == 'GP':
            return f'Член правления {self.user.last_name}'
        else:
            return f'Ревизор {self.user.last_name}'


class ImportantMessage(models.Model):
    header = models.CharField(max_length=128, null=False)
    content = models.TextField()
    date_add = models.DateField()

    class Meta:
        verbose_name = "событие"
        verbose_name_plural = "События"

