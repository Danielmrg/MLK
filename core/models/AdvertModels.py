import os
import uuid

from core.utils import unique_slug_generator
from django.db import models
from django.db.models.signals import pre_save
from django.utils.html import format_html
from django.db.models import Q
from django.http import Http404
from django.urls import reverse

from .UserModels import User
from django_jalali.db import models as jmodels


# class TimestampedModel(models.Model):
#     # A timestamp representing when this object was created.
#     created_at = models.DateTimeField(auto_now_add=True)

#     # A timestamp reprensenting when this object was last updated.
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True

#         # By default, any model that inherits from `TimestampedModel` should
#         # be ordered in reverse-chronological order. We can override this on a
#         # per-model basis as needed, but reverse-chronological is a good
#         # default ordering for most models.
#         ordering = ['-created_at', '-updated_at']

def get_file_ext(filepath):
    base_name = os.path.basename(filepath)
    name , ext = os.path.splitext(base_name)
    return  name , ext

def change_file_name(instance, filename):
    name,ext = get_file_ext(filename)
    new_name = f"{instance.id}-{instance.title}{ext}"
    return new_name


# class AdvertQuerySet(models.QuerySet):
#     def search(self, **kwargs):
#         qs = self
#         if kwargs.get('q', ''):
#             qs = qs.filter(name__icontains=kwargs['q'])
#         # if kwargs.get('government_type', []):
#         #     qs = qs.filter(government_type=kwargs['government_type'])
#         # if kwargs.get('industry', []):
#         #     qs = qs.filter(industry=kwargs['industry'])
#         return qs

class AdvertManager(models.Manager):
    def active(self):
        return self.filter(status="A")

    def deactive(self):
        return self.filter(status="E")
    
    def public(self):
        return self.filter(status="A").filter(is_public_group=True)
    
    def search_public(self,query):
        q = query
        if q:
            lookup = Q(title__icontains=q)|Q(detail__icontains=q)|Q(description__icontains=q)
            qs = self.filter(lookup,is_public_group=True,status='A').distinct()
            return qs
        raise Http404('not found')
    
    def search_all(self,query=None):
        q = query
        if q:
            lookup = Q(title__icontains=q)|Q(detail__icontains=q)|Q(description__icontains=q)
            qs = self.filter(lookup).distinct()
            return qs
        raise Http404('not found')

class Advert(models.Model):
    choices = [
        ('A','انتشار'),
        ('E','اتمام'),
    ]
    Uid = models.UUIDField(max_length=36,default=uuid.uuid4,editable=False,unique=True)
    slug = models.SlugField(unique=True,blank=True)
    poster = models.ImageField(upload_to=change_file_name,default='image_default\default.jpg',blank=False, null=False,verbose_name='پستر')
    title = models.CharField(max_length=50,null=False,blank=False,verbose_name='عنوان')
    detail = models.CharField(max_length=80,null=False,blank=False,verbose_name='جزئیات')
    price = models.CharField(max_length=50,null=True,blank=True,verbose_name='قیمت')
    status = models.CharField(choices=choices,max_length=1,null=False,blank=False,default='A',verbose_name='وضعیت اگهی')
    description = models.TextField(max_length=500,blank=False, null=False,verbose_name='توضیحات')
    is_public_group = models.BooleanField(default=False,verbose_name='انتشار در گروه')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='زمان ساخت')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='زمان اپدیت')
    user = models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name='کاربر',related_name='user_advert')
    objects = AdvertManager()

    @classmethod
    def get_fields_advert(cls):
        list_fields =[field.name for field in  cls._meta.get_fields()]
        return list_fields

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def get_poster(self):
        return self.poster.url
    
    def get_html_poster(self):
        return format_html(f"<img src='{self.get_poster()}' class='img-thumbnail' style='max-height:100px; max-width:500px;' alt='{self.slug}'>")
    
    def get_status(self):
        if self.status == "A":
            return True
        return False
    
    def get_price(self):
        if self.price:
            return self.price
        return 'توافقی'

    def get_group_name(self):
        return self.user.group.title
    
    def get_group(self):
        return self.user.group

    def __str__(self): 
        return self.title


    class Meta:
        ordering = ['-created_at','updated_at']
        verbose_name = 'آگهی'
        verbose_name_plural = 'آگهی ها'
        app_label = 'core'


def advert_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(advert_pre_save_receiver,sender=Advert)
