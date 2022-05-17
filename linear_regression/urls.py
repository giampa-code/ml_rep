"""Linear regression URLs."""

# Django
from django.urls import path


# Views
from linear_regression import views as lr_views


urlpatterns = [
    path(route='',view=lr_views.lr_home, name='predict'),
]
