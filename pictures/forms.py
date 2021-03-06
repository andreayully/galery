from django import forms
from django.forms import ModelForm
from pictures.models import Photo


class PhotoForm(ModelForm):
    class Meta:
        model=Photo
        exclude=['date_upload']
        fields=['title', 'image']
        widgets={
        'image': forms.ClearableFileInput(attrs={'id':"id_image", 'size':"520"})}
