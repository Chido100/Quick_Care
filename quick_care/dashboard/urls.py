from django.urls import path
from .views import CreatItemView, DashboardView, ItemDetailView, ItemUpdateView, ItemDeleteView


urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('new_item/', CreatItemView.as_view(), name='new-item'),
    path('item_details/', ItemDetailView.as_view(), name='item-details'),
    path('edit_item/', ItemUpdateView.as_view(), name='edit-item'),
    path('delete_item/', ItemDeleteView.as_view(), name='delete-item'),
]