# Generated by Django 3.0 on 2021-01-01 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20201230_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='اسلاگ'),
        ),
    ]
