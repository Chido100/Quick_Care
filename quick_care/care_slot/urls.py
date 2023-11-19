from django.urls import path
from .views import CreateCareSlotView, ListCareSlotView


urlpatterns = [
    path('create_slot/', CreateCareSlotView.as_view(), name='create-slot'),
    path('slot_list/', ListCareSlotView.as_view(), name='slot-list'),
]