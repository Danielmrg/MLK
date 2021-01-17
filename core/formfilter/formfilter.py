from django import forms
from django.db.models import Q
from kivy.uix import widget


class FilterForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(
            blank=True,
            label = 'عنوان/توضیحات',
            attrs={
                'class':'form-control',
                'placeholder':'عنوان/توضیحات',
                'type':'search',
                'name':'qs',
            }
        )
    )








###############################################
# class CustomModelFilter(forms.ModelChoiceField):
#     def label_from_instance(self, obj):
#         return "%s %s" % (obj.column1, obj.column2)

# class CustomForm(ModelForm):
#     model_to_filter = CustomModelFilter(queryset=CustomModel.objects.filter(active=1))

#     class Meta:
#         model = CustomModel
#         fields = ['model_to_filter', 'field1', 'field2']
        
# ################################################################
# # best way for this

# class ExcludedDateForm(ModelForm):
#     class Meta:
#         model = models.ExcludedDate
#         exclude = ('user', 'recurring',)
#     def __init__(self, user=None, **kwargs):
#         super(ExcludedDateForm, self).__init__(**kwargs)
#         if user:
#             self.fields['category'].queryset = models.Category.objects.filter(user=user)
