from django import forms
from .models import Product

class ProductForm(forms.ModelForm): # a model form
    title       = forms.CharField( # overide the title
        label='This is a label, which can be empty',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Product name'
            }    
        )
    )
    
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary',
            'featured',
            ]
    
    def clean_title(self,*args,**kwargs):
        title = self.cleaned_data.get('title')
        if not 'wine' in title:
            raise forms.ValidationError('Invalid title: title must contain the word "wine".')
        if not ' ' in title:
            raise forms.ValidationError('Invalid title: title must contain at leat two words.')
        else:
            return title
        
class RawProductForm(forms.Form): # a raw form
    title       = forms.CharField(
        label='This is a label, which can be empty',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Product name'
            }    
        )
    )
    description = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'class': 'new-class-name',
                'id': 'my-id-for-textarea',
                'rows': 20,
                'cols': 120,
                'placeholder': 'Product description'
            }
        )
    )
    price       = forms.DecimalField(initial=0.0)
    summary     = forms.CharField(label='Summary')
    featured    = forms.BooleanField(required=False)