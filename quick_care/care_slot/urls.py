from django.urls import path
from .views import ListCareSlotView, CreateCareSlotView, DetailCareSlotView, UpdateCareSlotView



urlpatterns = [
    path('create_slot/', CreateCareSlotView.as_view(), name='create-slot'),
    path('slot_list/', ListCareSlotView.as_view(), name='slot-list'),
    path('slot_detail/<int:pk>/', DetailCareSlotView.as_view(), name='slot-detail'),
    path('edit_slot/<int:pk>/', UpdateCareSlotView.as_view(), name='edit-slot'),
]