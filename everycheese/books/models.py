from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


class Book(TimeStampedModel):
    title = models.CharField("Title of Book", max_length=255)
    slug = AutoSlugField("Book URL Slug",
        unique=True, always_update=False, populate_from="title")
    blurb = models.TextField("Description", blank=True)
    author = models.TextField("Author")
    
    def __str__(self):
        return f"{self.title} by {self.author}"
