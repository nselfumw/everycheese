from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'title',
        'slug',
        'blurb',
        'author',
    )
    list_filter = ('created', 'modified')
    search_fields = ('slug',)
