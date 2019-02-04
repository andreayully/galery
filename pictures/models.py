from django.db import models

# Create your models here.
class RelatedPhoto(models.Model):
    image= models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.image.url


class PhotoInfo(models.Model):
    title = models.CharField(max_length=30)
    date_upload = models.DateTimeField(auto_now_add=True, blank=True)
    #image= models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.title

class PhotoPost(models.Model):
    image = models.ForeignKey(RelatedPhoto)
    photoInfo= models.ForeignKey(PhotoInfo)
