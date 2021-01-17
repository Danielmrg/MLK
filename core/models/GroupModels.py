from django.db import models
import uuid

# class GroupManager(models.Manager):
#     def 


class Group(models.Model):
    choices = [
        ('kp','کیانپارس'),
        ('ka','کیان اباد'),
        ('ks','کیانشهر')
    ]
    Uid = models.UUIDField(max_length=36,default=uuid.uuid4,editable=False,unique=True)
    title = models.CharField(max_length=50,verbose_name='عنوان',blank=False,null=False)
    description = models.TextField(max_length=500,null=True,blank=True,verbose_name='توضیحات')
    place  = models.CharField(max_length=2,choices=choices,default='kp',verbose_name='منطقه')
    phone_number = models.CharField(max_length=12,verbose_name='شماره تلفن',blank=False, null=False)
    # object = GroupManager()

    def get_all_users(self):
        return self.group_user.all()
    
    def get_all_adverts(self):
        advert_list = [ user.get_public_adverts() for user in self.get_all_users() if user.get_public_adverts()]
        return advert_list[0]

    def get_len_adverts(self):
        count = len(self.get_all_adverts())
        return count

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'گروه'
        verbose_name_plural = 'گروه ها'
        app_label = 'core'
