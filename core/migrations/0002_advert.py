# Generated by Django 3.0 on 2020-12-18 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('poster', models.ImageField(default='#', upload_to='', verbose_name='پستر')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('detail', models.CharField(max_length=80, verbose_name='جزئیات')),
                ('status', models.CharField(choices=[('A', 'انتشار'), ('E', 'اتمام')], default='A', max_length=1, verbose_name='وضعیت اگهی')),
                ('description', models.TextField(max_length=500, verbose_name='توضیحات')),
                ('is_private', models.BooleanField(default=True, verbose_name='ذخیره شخصی')),
                ('is_public_group', models.BooleanField(default=False, verbose_name='انتشار در گروه')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='زمان اپدیت')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_advert', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'آگهی',
                'verbose_name_plural': 'آگهی ها',
                'ordering': ['created_at', 'updated_at'],
            },
        ),
    ]
