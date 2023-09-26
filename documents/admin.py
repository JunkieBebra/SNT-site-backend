from django.contrib import admin

from documents.models import Category, Document, Directory

admin.site.register(Directory)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'directory', 'date_add')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
# Register your models here.
