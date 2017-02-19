from django import forms
from Car.models import Spec, Brand


class BrandForm(forms.ModelForm):
    
    class Meta:
        model =Brand
        fields = ('name', 'logo', 'description')
        exclude = ('slug', )
    

class SpecForm(forms.ModelForm):
   
    class Meta:
        model = Spec
        fields = ('name', 'slug', 'brand', 'condition', 'category', 'price',
                  'details', 'location', 'transmission', 'fuel', 'lifestyle',
                  'seller_type', 'mileage', 'color_family',)
        exclude = ('slug', )

        
        widgets = {
            'name': forms.TextInput(attrs=({'placeholder': 'Name', 'class': 'mandatory'})),
            'brand': forms.TextInput(attrs=({'placeholder': 'Brand', 'class': 'mandatory'})),
            'condition':forms.Select(attrs=({'placeholder': 'Condition', 'class': 'mandatory'})),
            'category': forms.Select(attrs=({'placeholder': 'Category', 'class': 'mandatory'})),
            'price': forms.TextInput(attrs=({'placeholder': 'Price', 'class': 'mandatory'})),
            'details': forms.Textarea(attrs=({'placeholder': 'Details', 'class': 'mandatory'})),
            'locations': forms.TextInput(attrs=({'placeholder': 'Locations', 'class': 'mandatory'})),
            'transmission': forms.TextInput(attrs=({'placeholder': 'Transmission', 'class': 'mandatory'})),
            'fuel': forms.TextInput(attrs=({'placeholder': 'Fuel', 'class': 'mandatory'})),
            'lifestyle': forms.TextInput(attrs=({'placeholder': 'LifeStyle', 'class': 'mandatory'})),
            'seller_type': forms.TextInput(attrs=({'placeholder': 'Seller Type', 'class': 'mandatory'})),
            'mileage': forms.TextInput(attrs=({'placeholder': 'Mileage', 'class': 'mandatory'})),
            'color_family': forms.TextInput(attrs=({'placeholder': 'Color', 'class': 'mandatory'})),
        }
    
        def __init__(self, *args, **kwargs):
            super(SpecForm, self).__init__(*args, **kwargs)

            
            
class SearchForm(forms.ModelForm):
    search_query = forms.CharField(max_length=100)
