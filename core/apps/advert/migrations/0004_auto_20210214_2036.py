# Generated by Django 3.0 on 2021-02-14 17:06

import advert.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0003_auto_20210213_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='عنوان')),
            ],
        ),
        migrations.AlterField(
            model_name='advert',
            name='poster',
            field=models.ImageField(default='image_default\\default.jpg', upload_to=advert.models.change_file_name, verbose_name='پستر'),
        ),
        migrations.AddField(
            model_name='advert',
            name='options',
            field=models.ManyToManyField(blank=True, null=True, related_name='advert_option', to='advert.Option'),
        ),
    ]
