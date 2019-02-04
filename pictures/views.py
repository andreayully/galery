from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
#from pictures.models import Photo
#from pictures.forms import PhotoForm
import datetime

# Create your views here.
class PhotoCreateView(CreateView):
    #model=Photo
    #form_class= PhotoForm
    template_name = 'pictures/upload_picture.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        photo = form.save(commit=False)
        #photo.date_upload =
        form.save()
        return super(PhotoCreateView, self).form_valid(form)

class PhotoListView(ListView):
    #model=Photo
    paginate_by= 5
    #context_object_name= 'photos'
    template_name= 'pictures/list_picture.html'

    def get_context_data(self, **kwargs):
        context = super(PhotoListView, self).get_context_data(**kwargs)
        context['photos'] = Photo.objects.all()
        return context
