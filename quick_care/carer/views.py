from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import ChildMinderKYC
from .forms import ChildMinderForm
from django.urls import reverse_lazy


# Register as a Childminder
class CreateChildminderView(LoginRequiredMixin, CreateView):
    model = ChildMinderKYC
    form_class = ChildMinderForm
    template_name = 'carer/register.html'

    def form_valid(self, form):
        form.instance.childminder = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('childminder-details', kwargs={childminder_id: self.object.id})

    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['title'] = self.title
    #    return context


# Childminder Details
class ChildminderDetailsView(LoginRequiredMixin, DetailView):
    model = ChildMinderKYC
    template_name = 'carer/childminder_details.html'
    context_object_name = 'childminder'
    pk_url_kwarg = 'pk'
