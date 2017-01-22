from django import forms
from django.db import models


class SpecForm(forms.ModelForm):

		class Meta: 
				exclude = ['date_submitted']