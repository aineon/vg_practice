from django.db import models


class BlogPost(models.Model):
    class Meta:
        verbose_name = 'Blog Post'

    title = models.CharField(max_length=254, blank=False, null=False)
    author = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(max_length=254, unique=True)
    intro = models.TextField(blank=False, null=False)
    section_one = models.TextField(blank=False, null=False)
    section_two = models.TextField(blank=True, null=True)
    section_three = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    original_url = models.URLField(max_length=1024, blank=True, null=True)
    source = models.CharField(max_length=254, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
