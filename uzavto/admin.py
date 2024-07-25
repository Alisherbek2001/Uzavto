from django.contrib import admin
from .models import Category,SubCategory

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    search_fields = ['name']
    list_filter = ['name']
    list_per_page = 10
admin.site.register(Category,CategoryAdmin)


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category','type']
    search_fields = ['name']
    list_filter = ['name','type']
    list_editable = ['category','type']
    list_per_page = 10
admin.site.register(SubCategory,SubcategoryAdmin)
