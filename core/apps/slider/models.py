from django.db import models
from advert.models import Advert
import os

def get_file_ext(filepath):
    base_name = os.path.basename(filepath)
    name , ext = os.path.splitext(base_name)
    return  name , ext

def change_file_name(instance, filename):
    name,ext = get_file_ext(filename)
    new_name = f"SliderImage/{instance.id}-{instance.title}{ext}"
    return new_name



class Slider(models.Model):
    adverts = models.ManyToManyField(to=Advert,related_name='slider_advert')
    # def get_poster_url(self):
    #     return self.poster.url
    
    def __str__(self):
        return f"{self.adverts.all().first().title}"
    
    class Meta:
        verbose_name="اسلاید"
        verbose_name_plural="اسلاید ها"