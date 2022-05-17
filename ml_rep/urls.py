"""ml_rep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ml_rep import views as local_views

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # home
    path('',local_views.HomePageView.as_view(), name='home'),

    # projects
    path('projects/',local_views.ProjectsPageView.as_view(), name='projects'),

    # Linear regression
    path('linear-regression/',include(('linear_regression.urls','linear_regression'),namespace='linear-regression'))
]
