from django import forms


class SpecForm(forms.ModelForm):

		class Meta: 
				exclude = ['date_submitted']