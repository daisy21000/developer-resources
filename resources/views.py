from django.shortcuts import render
from django.http import HttpResponse
from .models import Resource, Category


# Create your views here.
def index(request):
    resources = Resource.objects.filter(approved=True).order_by('-created_at')
    categories = Category.objects.filter(published=True).order_by('name')
    context = {
        'resources': resources,
        'categories': categories,
    }
    return render(request, 'resources/index.html', context)
