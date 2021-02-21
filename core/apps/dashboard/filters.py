# from .models import *
# import django_filters
# from django import forms
# from django.db import models

# class AdvertFilter(django_filters.FilterSet):
#     class Meta:
#         model = Advert
#         fields = {
#             'title':['icontains']
#         }
#         # widgets = {
#         #     'title':django_filters.CharFilter(attrs={'class':'form-control'})
#         # }
#         filter_overrides = {
#             models.CharField: {
#                 'field_name':None,
#                 'filter_class': django_filters.CharFilter,
#                 'extra': lambda f: {
#                     'label': '',
#                     'widget': forms.TextInput(attrs={'class':'form-control','placeholder':'نام'}),
#                 },
#             }
#         }