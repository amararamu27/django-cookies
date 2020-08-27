from django import forms
from app26.models import ProductModel


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'
        labels = {'pname':'Product Name','price':'Product Price','quantity':'Product Quantity'}

