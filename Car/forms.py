from django import forms
from Car.models import Spec, Brand


class BrandForm(forms.ModelForm):
    
    class Meta:
        model =Brand
        fields = ['name']


class SpecForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    brand = forms.ModelMultipleChoiceField(queryset=Brand.objects.all())
    category = forms.CharField(max_length=100, widget=forms.Select(choices=Spec.CATEGORY))
    price = forms.DecimalField(max_digits=9)
    details = forms.CharField(widget=forms.Textarea)
    locations = forms.CharField(max_length=100)
    transmission = forms.CharField(max_length=100, widget=forms.Select(choices=Spec.TRANS),)
    fuel = forms.CharField(max_length=100)
    
    class Meta:
        model = Spec
        exclude = ('fuel',)