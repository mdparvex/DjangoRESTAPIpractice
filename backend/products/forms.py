from django import forms

from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        models = Products

        fields=[
            "title",
            "content",
            "price"
            ]