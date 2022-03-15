from django.contrib import admin

# Register your models here.
from library.models import Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'author', 'publication_date', 'is_active')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'is_active')
