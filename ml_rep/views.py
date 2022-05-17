"""familygram views"""

# Django
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# views
from django.views.generic import TemplateView

# home with classes
class HomePageView(TemplateView):
    template_name = 'home.html'

# home with funcs
def home(request):
    """Web home"""
    return render(request, template_name="home.html")

# projects with classes
class ProjectsPageView(TemplateView):
    template_name = 'projects.html'