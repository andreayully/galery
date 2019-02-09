# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=30, verbose_name='Título')
    date_upload = models.DateTimeField(auto_now_add=True, blank=True)
    image= models.FileField(upload_to='uploads/', verbose_name='Imagen')

    def __str__(self):
        return self.title
