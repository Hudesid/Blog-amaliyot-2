from django.db import models
from django.contrib.auth import settings
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    class StatusChoice(models.TextChoices):
        Published = 'published', _("Published")
        Pending = 'pending', _('Pending')
        Rejected = 'rejected', _('Rejected')

    slug = models.SlugField(unique=True, blank=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    categories = models.ManyToManyField("categories.Category", related_name='posts')
    tags = models.ManyToManyField("tags.Tag", related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=StatusChoice.choices, default=StatusChoice.Pending)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)