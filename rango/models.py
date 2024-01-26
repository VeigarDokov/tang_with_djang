"""Required modules"""
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


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


class ContactMessage(models.Model):
    """Contatc via web"""
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    datetime_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    """ This line is required. links UserProfile to user model instance"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # The additiona attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
