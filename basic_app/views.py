from django.shortcuts import render
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
from basic_app import models
from django.urls import reverse_lazy

class index(TemplateView):
    template_name = 'index.html'

class VillaListView(ListView):
    context_object_name = 'villas_list'
    model = models.Villa

class VillaDetailView(DetailView):
    model = models.Villa
    template_name = 'basic_app/villa_detail.html'

class VillaCreateView(CreateView):
    fields = '__all__'
    model = models.Villa

class OwnerCreateView(CreateView):
    fields = '__all__'
    model = models.Owner

class OwnerUpdateView(UpdateView):
    fields = ('name', 'age', 'mobile')
    model = models.Owner

class OwnerDeleteView(DeleteView):
    model = models.Owner
    success_url = reverse_lazy('basic_app:list')

class OwnerListView(ListView):
    model = models.Owner
