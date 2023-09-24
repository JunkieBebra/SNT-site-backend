from django.contrib import admin

from documents.models import Document, Directory

admin.site.register(Directory)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'directory', 'date_add')


# Register your models here.
