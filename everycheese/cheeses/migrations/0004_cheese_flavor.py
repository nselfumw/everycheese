# Generated by Django 3.1.1 on 2024-02-12 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheeses', '0003_cheese_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheese',
            name='flavor',
            field=models.TextField(blank=True, verbose_name='Flavor'),
        ),
    ]
