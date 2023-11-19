from django.shortcuts import render, get_object_or_404, redirect
from .models import CareSlot
from .forms import CareSlotForm
from django.contrib import messages
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from datetime import datetime, timedelta



# Create a Slot
class CreateCareSlotView(LoginRequiredMixin, CreateView):
    model = CareSlot
    form_class = CareSlotForm
    template_name = 'care_slot/create_slot.html'
    success_url = reverse_lazy('slot-list')

    def form_valid(self, form):
        # Get the current user ID
        user_id = self.request.user.id
        form.instance.creator_id = user_id

        # Validate slot date entered before creating slot
        slot_date_str = form.cleaned_data['slot_date'].strftime("%Y-%m-%d %H:%M:%S")
        slot_date = datetime.strptime(slot_date_str, "%Y-%m-%d %H:%M:%S")

        current_date = datetime.now()
        date_difference = slot_date - current_date

        if date_difference >= timedelta(days=2):
            messages.success(self.request, 'Your slot has been submited successfully.')
            return super().form_valid(form)
        else:
            messages.error(self.request, 'The date selected must be atleast 2 days in the future. Please select a valid date.')
            return self.form_invalid(form)
            


# List all Slots
class ListCareSlotView(LoginRequiredMixin, ListView):
    model = CareSlot
    template_name = 'care_slot/slot_list.html'
    context_object_name = 'slots'

    def get_queryset(self):
        return CareSlot.objects.filter(creator=self.request.user)


# Slot Details
class DetailCareSlotView(LoginRequiredMixin, DetailView):
    model = CareSlot
    template_name = 'care_slot/slot_detail.html'
    context_object_name = 'slot'
    pk_url_kwarg = 'pk'


# Update Slot
class UpdateCareSlotView(LoginRequiredMixin, UpdateView):
    model = CareSlot
    form_class = CareSlotForm
    template_name = 'care_slot/edit_slot.html'
    success_url = reverse_lazy('slot-detail')
    pk_url_kwarg = 'pk'


