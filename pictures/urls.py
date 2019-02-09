from django.conf.urls import url, include
from pictures.views import *

urlpatterns = [
     url(r'^$', PhotoCreateView.as_view(), name='upload_picture'),
     url(r'list/', PhotoListView.as_view(), name='list_picture'),
     url(r'^delete_photo/(?P<id>\d+)/$', deletePhoto, name='delete_photo'),
     url(r'^update_person/(?P<id>\d+)/$', PhotoUpdateView.as_view(), name='update_photo'),
]
