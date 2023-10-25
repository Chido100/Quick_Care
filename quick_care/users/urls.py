from django.urls import path
from .views import CreateUserView, ProfileView
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('profile/', ProfileView.as_view(), name='profile'),
]