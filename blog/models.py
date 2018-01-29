from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    STATUS_CHOICES = (
            ('draft', 'Draft'),
            ('published', 'Published'),
        )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')

    # We specify the name of the reverse relationship, from User to Post,
    # with the related_name attribute
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    # auto_now_add  - The date will saved when creating an object
    created = models.DateTimeField(auto_now_add=True)

    # auto_now - the date will be updated automatically when creating an object
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
        default='draft')

    class Meta:
        # Sort results by the publish field in descending order by default
        ordering = ('-publish',)

    def __str__(self):
        return self.title
