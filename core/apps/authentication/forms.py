from django.contrib.auth import login , authenticate
from django.shortcuts import redirect
from django.core import validators
from django.contrib.auth.models import BaseUserManager
from django import forms
from .models import User

class LoginForm(forms.Form):
    UserName = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder':"شماره تلفن"
            }
        )
    )
    Password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "رمز عبور",
            }
        )
    )
    
    def clean_UserName(self):
        username = self.cleaned_data.get("UserName")
        get_user = User.objects.filter(phone=username).exists()
        if not get_user:
            raise  forms.ValidationError("با مشخصات بالا هیچ کاربری یافت نشد!")
        return username
    def clean_Password(self):
        password = self.cleaned_data.get("Password")
        return password

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        return cleaned_data
    
    def LoginUser(self,request):
        username = self.cleaned_data.get("UserName")
        password = self.cleaned_data.get("Password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return True
        raise  forms.ValidationError("با مشخصات بالا هیچ کاربری یافت نشد!")
        

class SignUpForm(forms.Form):
    Firstname = forms.CharField(
        label="نام",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':"form-control",
                "placeholder":"نام"
            }
            
        )
    )
    Lastname = forms.CharField(
        label="نام خانوادگی",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':"form-control",
                "placeholder":"نام خانوادگی"
            }
            
        )
    )
    username = forms.CharField(
        label="نام مستعار",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':"form-control",
                "placeholder":"نام مستعار"
            }
            
        )
    )
    phone = forms.CharField(
        label="تلفن",
        required=True,
        widget=forms.NumberInput(
            attrs={
                "class":"form-control",
                "placeholder":"تلفن"
            }
        )
    )
    password = forms.CharField(
        label="رمز عبور",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder":"رمز عبور"
            }
        )
    )
    re_password = forms.CharField(
        label="تکرار رمز عبور",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder":"تکرار رمز عبور"
            }
        )
    )
    def clean_username(self):
        username = self.cleaned_data.get("username")
        get_user = User.objects.filter(username=username).exists()
        if get_user:
            raise forms.ValidationError("کاربری با این مشخصات قبلا ثبت نام کرده!")
        return username
    
    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        return cleaned_data
    
    def clean_re_password(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("re_password")
        if password != re_password:
            raise forms.ValidationError("رمز عبور و تکرار ان یکی نیستند!")
    
    def Save(self):
        cleaned_data = super(SignUpForm, self).clean()
        first_name = cleaned_data.get("Firstname")
        last_name = cleaned_data.get("Lastname")
        username = cleaned_data.get("username")
        phone = cleaned_data.get("phone")
        password = cleaned_data.get("password")
        make_user = User.objects.create_new_user(
            username = username,
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            password = password
        )
        if make_user:
            return True
        raise forms.ValidationError("Problem!")
    
class UserUpdateForm(forms.ModelForm):
    # TODO
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone']
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class":"form-control",
                }  
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class":"form-control",
                }  
            ),
            "phone": forms.TextInput(
                attrs={
                    "class":"form-control",
                }
            ),  
        }