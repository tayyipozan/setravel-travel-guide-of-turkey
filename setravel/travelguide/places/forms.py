from .models import Place, Images
from django import forms


class AddingCardImgForm(forms.ModelForm):
    cardimage = forms.ImageField(label='Place Card Image', widget=forms.FileInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Place Card Image',
            'id': 'floatingInput',
        }))

    class Meta:
        model = Images
        fields = [
            'cardimage',
        ]


class AddingImgForm(forms.ModelForm):
    image = forms.ImageField(label='Place Image', widget=forms.FileInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Place Card Image',
            'id': 'floatingInput',
        }))

    class Meta:
        model = Place
        fields = [
            'image',
        ]
