import os
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


def get_file_ext(filepath):
    base_name = os.path.basename(filepath)
    name , ext = os.path.splitext(base_name)
    return  name , ext

def change_file_name(instance, filename):
    name,ext = get_file_ext(filename)
    new_name = f"User/{instance.first_name}-{ext}"
    return new_name

class UserManager(BaseUserManager):
    def create_user(self, phone, password,**extra_fields):
        """
        Create and save a User with the given email and password.
        """
        user = self.model(phone=phone ,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_new_user(self,username, first_name, last_name,phone, password, **extra_fields):
        user = self.model(username=username,first_name=first_name, last_name=last_name,phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone , password,**extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(phone, password, **extra_fields)

    def get_by_role(self,role_name):
        return self.filter(role__title__icontains=role_name)



class User(AbstractUser):
    picture = models.ImageField(upload_to=change_file_name,default='image_default\default.jpg',blank=False, null=False,verbose_name='عکس')
    username = models.CharField(verbose_name="نام کاربری",max_length=150,unique=True,)
    phone = models.CharField(max_length=12,verbose_name='شماره تلفن',blank=False, null=False,unique=True) 
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ['username']
    role = models.ManyToManyField(to='Role',related_name='user_role',verbose_name='نقش',blank=True, null=True)
    objects = UserManager()
    bio = models.TextField(verbose_name="درباره من",blank=True,null=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    def get_image(self):
        return self.picture.url
    def get_all_advert(self):
        return self.user_advert.all()
    def get_role_title(self):
        return [role.title for role in self.role.all()]
    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ('first_name', 'last_name')
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

class Role(models.Model):
    title = models.CharField(max_length=100,blank=False, null=False,verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    is_active = models.BooleanField(default=True,verbose_name='فعال/غیرفعال')
    
    def __str__(self):
        return f"{self.title}"
    