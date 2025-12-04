from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Q, Count
from .models import Resource, Category
from .forms import ResourceForm, CategoryForm
from django.contrib import messages
from django.shortcuts import render
from .utils import sort_resources


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
    favorite_resources = resources.filter(favorites=request.user) if request.user.is_authenticated else []
    if resources.exists():
        resources = sort_resources(request, resources)

    context = {
        'category': category,
        'resources': resources,
        'favorite_resources': favorite_resources,
    }
    return render(request, 'resources/category_detail.html', context)


def submit_resource(request):
    if not request.user.is_authenticated:
        messages.add_message(
            request, messages.ERROR,
            'You must be logged in to submit a resource.')
        return HttpResponseRedirect('/accounts/login/')
    else:
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
                messages.add_message(
                    request, messages.ERROR,
                    'There was an error submitting the resource. Please try again.')
        else:
            form = ResourceForm()

        context = {
            'form': form,
        }
        return render(request, 'resources/add_resource.html', context)


def edit_resource(request, resource_id):
    resource = Resource.objects.get(id=resource_id)
    if resource.uploader != request.user:
        messages.add_message(
            request, messages.ERROR,
            'You are not authorized to edit this resource.')
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            form = ResourceForm(request.POST, instance=resource)
            if form.is_valid():
                form.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Resource updated successfully.')
            else:
                messages.add_message(
                    request, messages.ERROR,
                    'Something went wrong. Please try again.')
        else:
            form = ResourceForm(instance=resource)

    context = {
        'form': form,
        'resource': resource,
    }
    return render(request, 'resources/add_resource.html', context)


def delete_resource(request, resource_id):
    resource = Resource.objects.get(id=resource_id)
    if resource.uploader == request.user:
        resource.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Resource deleted successfully.')
    else:
        messages.add_message(
            request, messages.ERROR,
            'You are not authorized to delete this resource.')
    return HttpResponseRedirect('/')


def view_favorites(request):
    if not request.user.is_authenticated:
        messages.add_message(
            request, messages.ERROR,
            'You must be logged in to view your favorite resources.')
        return HttpResponseRedirect('/accounts/login/')
    else:
        favorite_resources = request.user.favorite_resources.all().order_by('-created_at')
        if favorite_resources.exists():
            favorite_resources = sort_resources(request, favorite_resources)

        context = {
            'favorite_resources': favorite_resources,
        }
        return render(request, 'resources/favorite_resources.html', context)


def favorite_resource(request, resource_id):
    resource = Resource.objects.get(id=resource_id)
    if request.user.is_authenticated:
        if resource.favorites.filter(id=request.user.id).exists():
            resource.favorites.remove(request.user)
            messages.add_message(
                request, messages.SUCCESS,
                'Resource removed from favorites.')
        else:
            resource.favorites.add(request.user)
            messages.add_message(
                request, messages.SUCCESS,
                'Resource added to favorites.')
    else:
        messages.add_message(
            request, messages.ERROR,
            'You must be logged in to favorite a resource.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def suggest_category(request):
    if not request.user.is_authenticated:
        messages.add_message(
            request, messages.ERROR,
            'You must be logged in to suggest a category.')
        return HttpResponseRedirect('/accounts/login/')
    else:
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                category = form.save(commit=False)
                category.author = request.user
                if request.user.is_superuser:
                    category.published = True
                else:
                    category.published = False
                category.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Category suggestion submitted and awaiting approval.')
                form = CategoryForm()  # Reset the form after successful submission
            else:
                messages.add_message(
                    request, messages.ERROR,
                    'There was an error submitting the category. Please try again.')
        else:
            form = CategoryForm()

        context = {
            'form': form,
        }
        return render(request, 'resources/category_suggestion.html', context)


def search_resources(request):
    query = request.GET.get('q', '')
    search_in = request.GET.getlist('in') or ['name']
    resources = Resource.objects.filter(approved=True).order_by('-created_at') if query else []
    if query:
        q_objects = Q()
        if 'name' in search_in:
            q_objects |= Q(name__icontains=query)
        if 'description' in search_in:
            q_objects |= Q(description__icontains=query)
        if 'keywords' in search_in:
            q_objects |= Q(keywords__name__icontains=query)
        resources = resources.filter(q_objects).distinct()
        resources = sort_resources(request, resources)

    context = {
        'resources': resources,
        'query': query,
        'search_in': search_in,
    }
    return render(request, 'resources/search_results.html', context)
