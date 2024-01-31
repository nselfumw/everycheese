# from django.contrib import admin
# from .models import Cheese

# admin.site.register(Cheese)

from django.contrib import admin

from .models import Cheese


@admin.register(Cheese)
class CheeseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created',
        'id',
        'modified',
        'slug',
        # 'description',
        'firmness',
    )
    list_filter = ('created', 'modified')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}
