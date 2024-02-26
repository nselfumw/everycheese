from django.contrib import admin

from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'modified', 'first', 'last')
    list_filter = ('created', 'modified')


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
    list_filter = ('created', 'modified', 'author')
    search_fields = ('slug',)
