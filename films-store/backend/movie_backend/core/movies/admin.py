from django.contrib import admin

from .models import Movies


class MoviesAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "director",
        "image",
        "release_date",
        "slug",
    )
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Movies, MoviesAdmin)
