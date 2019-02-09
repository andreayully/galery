from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from pictures.models import Photo
from pictures.forms import PhotoForm
import datetime
import json

# Create your views here.
class PhotoCreateView(CreateView):
    model=Photo
    form_class= PhotoForm
    template_name = 'pictures/portafolio_form.html'
    success_url = reverse_lazy('pictures:list_picture')

    def form_valid(self, form):
        photo = form.save(commit=False)
        form.save()
        return super(PhotoCreateView, self).form_valid(form)

class PhotoListView(ListView):
    model=Photo
    paginate_by= 5
    #context_object_name= 'photos'
    template_name= 'pictures/portafolio_list.html'

    def get_context_data(self, **kwargs):
        context = super(PhotoListView, self).get_context_data(**kwargs)
        context['photos'] = Photo.objects.all()[::-1]
        return context

class PhotoUpdateView(UpdateView):
    model=Photo
    form_class= PhotoForm
    template_name = 'pictures/portafolio_form.html'
    success_url = reverse_lazy('pictures:list_picture')

    def get_object(self, queryset=None):
        obj = Photo.objects.get(pk=self.kwargs['id'])
        return obj

    def get_context_data(self, **kwargs):
        context = super(PhotoUpdateView, self).get_context_data(**kwargs)
        isUpdate = True
        obj = Photo.objects.get(pk=self.kwargs['id'])
        context['isUpdate'] = isUpdate
        context['ph'] = obj
        return context


def deletePhoto(request, id):
    photo = Photo.objects.get(id=id)
    photo.delete()
    return redirect('pictures:list_picture')
