from django.shortcuts import render
from django.http import HttpResponse
from .models import Resource, Category
from .forms import ResourceForm, CategoryForm
from django.contrib import messages


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


def submit_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.uploader = request.user
            resource.approved = False
            resource.save()
            form.save_m2m()  # Save tags
            messages.add_message(
                request, messages.SUCCESS,
                'Resource submitted and awaiting approval.')
            form = ResourceForm()  # Reset the form after successful submission
    else:
        form = ResourceForm()

    context = {
        'form': form,
    }
    return render(request, 'resources/add_resource.html', context)
