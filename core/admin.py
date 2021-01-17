from django.contrib import admin
from .models import User , Group , Advert


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    '''Admin View for User'''
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('اطلاعات شخصی'), {'fields': ('first_name','email' ,'last_name','Phone_number')}),
        (('مجوز ها'), {
            'fields': ('group','creator','is_active', 'is_staff','is_superuser','is_admin' , 'groups', 'user_permissions','description'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    '''Admin View for Group'''

    list_display = ('title','description','place','phone_number','much_users')
    # list_filter = ('',)
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
    def much_users(self, obj):
        return obj.group_user.all().count()
    much_users.short_description = 'تعداد کاربران'

@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    '''Admin View for Advet'''

    list_display = ('title','detail','status')
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    ordering = ('created_at', 'updated_at')