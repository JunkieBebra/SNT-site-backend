from django.db import models


class News(models.Model):
    name = models.CharField(max_length=128, null=False)
    date_add = models.DateTimeField(null=False)
    content = models.TextField(null=False)
    visible = models.BooleanField(default=True)

    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return f'"{self.name}" от ({self.date_add})'


