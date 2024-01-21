"""Required modules"""
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    """specifies content of the links on index page"""

    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)
    objects = models.Manager()

    class Meta:
        """Change name frmo djanbo admin from Categorys to Categories"""

        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Page(models.Model):
    """specifies names of urls where you will be redirected"""

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    objects = models.Manager()

    def __str__(self):
        return self.title
