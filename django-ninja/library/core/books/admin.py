from django.contrib import admin

from .models import Book, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "pub_date", "isbn", "slug"]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "birthdate"]

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)