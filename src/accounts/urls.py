from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import CustomLoginView


urlpatterns = [
    path('login/', CustomLoginView.as_view(
        template_name='login.html',
        next_page='index',
    ), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]
