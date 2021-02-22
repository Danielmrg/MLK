from django import forms
from advert.models import Option , Advert
from authentication.models import User

class AdvertForm(forms.Form):
    title = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'عنوان',
            }
        )
    )
    poster = forms.ImageField(
        widget = forms.FileInput(
            attrs={
                'class':'form-control-file',
            }
        )
    )
    detail = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'جزئیات',
            }
        )
    )
    price = forms.CharField(
        widget = forms.NumberInput(
            attrs = {
                'class':'form-control',
                'placeholder': 'قیمت',
            }
        )
    )
    area = forms.CharField(
        widget = forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'متراز'
            }
        )
    )
    stat = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'منطقه',
            }
        )
    )
    beds = forms.IntegerField(
        min_value=0,
        widget = forms.NumberInput(
            attrs={
                'class':'form-control',
                # 'placeholder':'تعداد خواب'
            }
        )
    )
    baths = forms.IntegerField(
        min_value=0,
        widget = forms.NumberInput(
            attrs={
                'class':'form-control',
                # 'placeholder':'تعداد حمام'
            }
        )
    )
    wc = forms.IntegerField(
        min_value=0,
        widget = forms.NumberInput(
            attrs = {
                'class':'form-control',
                # 'placeholder':'تعداد سرویس '
            }
        )
    )
    garages = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'class':'form-check-input',
                'value':'پارکینگ'         
            }
        )
    )
    house_type = forms.ChoiceField(
        choices=[
            ('V','ویلایی'),
            ('A','آپارتمانی'),
            ('O','سایر موارد')
        ],
        widget = forms.Select(
            attrs = {
                'class':'form-control',
            }
        )
    )
    category = forms.ChoiceField(
        choices=[
            ('B','خرید'),
            ('S','فروش'),
            ('R','رهن'),
            ('A','اجاره')
        ],
        widget = forms.Select(
            attrs={
                'class':'form-control',
            }
        )
    )
    description = forms.CharField(
        widget = forms.Textarea(
            attrs={
                'class':'form-control',
            }
        )
    )
    is_public = forms.BooleanField(
        widget= forms.CheckboxInput(
            attrs = {
                'class':'form-check-input',
            }
        )
    )
    year_created = forms.IntegerField(
        widget = forms.NumberInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    user = forms.IntegerField(
        widget = forms.HiddenInput()
    )
    url = forms.URLField(
        widget = forms.URLInput(
            attrs={
                'class':'form-control',
                'placeholder':'ادرس ویدیو'
            }
        )
    )
    def label_from_instance(self, option):
        return f"{option.title}"
    
    options = forms.ModelMultipleChoiceField(
        queryset = Option.objects.all(),
        widget = forms.CheckboxSelectMultiple(
            attrs={
                'class':'form-check-input'
            }
        )
    )
    def clean_user(self):
        user = self.cleaned_data.get('user')
        return User.objects.get(id=user)
        
    def Save(self):
        data = self.cleaned_data()
        advert = Advert.objects.create(**data)
        return advert