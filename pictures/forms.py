from django import forms
from django.forms import ModelForm
from pictures.models import RelatedPhoto


# class PhotoForm(ModelForm):
#     class Meta:
#         model=Photo
#         exclude=['date_upload']
#         fields=['title', 'image']

class PhotoForm(ModelForm):
    image = forms.ModelChoiceField(queryset= RelatedPhoto.objects.all(), required=False)

    class Meta:
        exclude=['date_upload']
        fields=['title']

    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['image'],initial= models.RelatedPhoto.objects.get(photopost__photoinfo=self.instance).values_list('id', flat=True)

    def save(self, commit=True):
        super(PhotoForm, self).save(commit)
        image = self.cleaned_data.pop('image', None)
        if image:
            self.instance.photopost.delete()
            models.PhotoPost.objects.create(photoInfo=self.instance, image=image,)
