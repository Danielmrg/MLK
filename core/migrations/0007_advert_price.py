# Generated by Django 3.0 on 2020-12-20 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20201220_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='price',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='قیمت'),
        ),
    ]