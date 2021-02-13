from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Artworks(models.Model):

    class art_category(models.TextChoices):
        PAINTING = 'PA', _('Painting')
        DRAWING = 'DR', _('Drawing')
        CERAMIC = 'CE', _('Ceramics')
        SCULPTURE = 'SC', _('Sculpture')
        PRINTS = 'PR', _('Prints')
        CARDS = 'CA', _('Cards')
        BOOKS = 'BO', _('Books')
        MIXED = 'MX', _('Mixed')

    title = models.CharField(max_length=254, null=False, blank=False)
    artist_id = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sold = models.BooleanField(default=False)
    category = models.CharField(max_length=2,
                                choices=art_category.choices,
                                default=art_category.PAINTING,
                                )
    created_at = models.DateTimeField()
    image_path = models.URLField(max_length=1024, null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    width = models.DecimalField(max_digits=5, decimal_places=2)
    depth = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.title
