from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placehoder':'نام کاربری'}
        ),
        label='نام کاربری'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placehoder':'رمز عبور'}
        ),
        label='رمز عبور'
    )

    def __init__(self, request = None ,*args, **kwargs):
        self.request = request 
        super().__init__(*args,**kwargs)
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError('User Not Found!')
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data















# class ContactsForm(forms.ModelForm):
#    # Metadata
#     class Meta:
#         model = Contacts
#         exclude = ['picture','description']
#         fields = ['first_name','last_name']
#         error_messages ={
#             'first_name':{
#                 'required': "این فیلد اجباری است",
#             },
#             'last_name':{
#                 'required': "این فیلد اجباری است",
#             }
#         }
#         labels = {
#             'first_name' : 'نام :',
#             'last_name' : 'نام خانوادگی :'
#         }
#         widgets = {
#             'first_name' : forms.TextInput(
#                 attrs = {'placeholder': 'نام',
#                         'class': 'form-control',
#                 }),
#             'last_name' : forms.TextInput(
#                 attrs = {
#                     'placeholder': 'نام خانوادگی',
#                     'class': 'form-control',
#                 }
#             )
#         }
