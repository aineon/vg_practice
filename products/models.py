from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254,
                            default='', unique=True, null=False)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def get_absolute_url(self):
        kwargs = {
            'category_slug': self.slug,
            }
        return reverse('product_categories', kwargs=kwargs)


class Subcategory(models.Model):

    class Meta:
        verbose_name_plural = 'Subcategories'

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254,
                            default='', unique=True, null=False)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def get_absolute_url(self):
        kwargs = {
            'subcategory_slug': self.slug
            }
        return reverse('product_subcategories',
                       kwargs=kwargs)


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    subcategory = models.ForeignKey('Subcategory', null=True, blank=True,
                                    on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254,
                            default='', unique=True, null=False)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'product_slug': self.slug,
        }
        return reverse('product_detail', kwargs=kwargs)
