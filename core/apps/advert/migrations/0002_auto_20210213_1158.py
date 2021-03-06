# Generated by Django 3.0 on 2021-02-13 08:28

import advert.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='poster',
            field=models.ImageField(default='image_default\\default.jpg', upload_to=advert.models.change_file_name, verbose_name='پستر'),
        ),
        migrations.CreateModel(
            name='AdvertView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ip', models.CharField(blank=True, max_length=150, null=True, verbose_name='ip کاربر')),
                ('view', models.IntegerField(blank=True, default=0, null=True, verbose_name='تعداد بازدید')),
                ('advert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertview', to='advert.Advert', verbose_name='آگهی')),
            ],
        ),
    ]
