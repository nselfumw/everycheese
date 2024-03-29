# Generated by Django 3.1.1 on 2024-01-31 14:36

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20240131_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True, verbose_name='Book URL Slug'),
        ),
    ]
