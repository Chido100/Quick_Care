from django.urls import path
from .views import CreateChildminderView, ChildminderDetailsView


urlpatterns = [
    path('register/', CreateChildminderView.as_view(), name='register'),
    path('childminder_details/<int:pk>/', ChildminderDetailsView.as_view(), name='childminder-details'),
]