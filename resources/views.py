from django.shortcuts import render
from django.http import HttpResponse
from .models import Resource, Category


# Create your views here.
def index(request):
    categories = Category.objects.filter(published=True).order_by('name')
    context = {
        'categories': categories,
    }
    return render(request, 'resources/index.html', context)


def category_detail(request, category_id):
    category = Category.objects.get(id=category_id, published=True)
    resources = category.resources.filter(approved=True).order_by('-created_at')
    context = {
        'category': category,
        'resources': resources,
    }
    return render(request, 'resources/category_detail.html', context)
