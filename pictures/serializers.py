from rest_framework import serializers
from pictures.models import RelatedPhoto

class RelatedPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedPhoto
        fields =('id', 'image')
