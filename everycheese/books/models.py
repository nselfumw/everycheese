from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


class Author(TimeStampedModel):
    first = models.CharField("First Name", max_length=255)
    last = models.CharField("Last Name", max_length=255)
    slug = AutoSlugField("Book URL Slug",
        unique=True, always_update=False, populate_from="title")

    def __str__(self):
        return f"{self.last}, {self.first}"


class Book(TimeStampedModel):
    title = models.CharField("Title of Book", max_length=255)
    slug = AutoSlugField("Book URL Slug",
        unique=True, always_update=False, populate_from="title")
    blurb = models.TextField("Description", blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} by {self.author}"
