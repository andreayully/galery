from django.conf.urls import url, include
from pictures.views import *

urlpatterns = [
     url(r'^$', PhotoCreateView.as_view(), name='upload_picture'),
     url(r'^$', PhotoListView.as_view(), name='list_picture'),
]
