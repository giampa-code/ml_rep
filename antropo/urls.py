"""Linear regression URLs."""

# Django
from django.urls import path


# Views
from antropo import views as antropo_views


urlpatterns = [
    path(route='',view=antropo_views.antropo_home, name='predict'),
]
