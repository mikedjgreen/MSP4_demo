from django.contrib import admin
from .models import Product, Category, Artworks


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ArtworksAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'artist_id',
        'price',
        'sold',
        'category',
        'created_at',
        'image_path',
        'height',
        'width',
        'depth'
    )

    ordering = ('title',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Artworks, ArtworksAdmin)
