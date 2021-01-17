from django.contrib.auth.models import AbstractUser, BaseUserManager
from .GroupModels import Group
from django.db import models
import uuid


class UserManager(BaseUserManager):
    # manage user
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
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
        return self.create_user(email, password, **extra_fields)

    def admin(self):
       return self.filter(is_admin=True)


class User(AbstractUser):
    Uid = models.UUIDField(max_length=36,default=uuid.uuid4,editable=False,unique=True)
    creator = models.BooleanField(default=False,verbose_name='سازنده')
    email = models.EmailField(blank=False, null=False,verbose_name='ایمیل',unique=True)
    Phone_number = models.CharField(max_length=12,verbose_name='شماره تلفن',blank=False, null=False)
    is_admin = models.BooleanField(default=False,verbose_name='ایا ادمین هستید؟')
    description = models.TextField(max_length=500,blank=True, null=True, verbose_name='توضیحات')
    group = models.ForeignKey(to=Group,on_delete=models.SET_NULL,null=True,verbose_name='گروه',related_name='group_user') 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()
    
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_adverts(self):
       return self.user_advert.all()
    
    def get_active_adverts(self):
        return self.user_advert.active()
    
    def get_deactive_adverts(self):
        return self.user_advert.deactive()
    
    def get_privet_adverts(self):
        return self.user_advert.privet()
    
    def get_public_adverts(self):
        return self.user_advert.public()
    
    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ('first_name', 'last_name')
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
        app_label = 'core'

