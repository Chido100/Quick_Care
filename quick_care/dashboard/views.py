from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Item, Category
from .forms import NewItemForm, EditItemForm
from django.urls import reverse_lazy



# Dashboard view
class DashboardView(LoginRequiredMixin, View):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.filter(is_expired=False).order_by('-date_created')[:6]
        context['categories'] = Category.objects.all()
        return context


# Create Item
class CreatItemView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = NewItemForm
    template_name = 'dashboard/new_item.html'
    title = 'New Item'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('item-details', kwargs={'item_id': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


# Item Detail Page
class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = 'dashboard/item_details.html'
    context_object_name = 'item'
    pk_url_kwarg = 'pk'


# Edit Item
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = EditItemForm
    template_name = 'dashboard/edit_item.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'item'

    def get_success_url(self):
        return reverse_lazy('item-details', kwargs={'item_id': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Item'
        return context


# Delete Item
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = 'dashboard/delete_item.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('dashboard')




