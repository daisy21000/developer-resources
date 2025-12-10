from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from .models import Resource, Category
from .forms import ResourceForm, CategoryForm
from .utils import sort_resources


# Create your views here.
def index(request):
    """
    Display the homepage with a list of published categories.

    This view fetches all published categories, orders them by name,
    and renders them on the homepage.

    :param request: The HTTP request object.

    **Context:**

    ``categories``: A queryset of published :model:`Category` objects ordered
    by name.

    **Template:**

    :template:`resources/index.html`
    """
    categories = Category.objects.filter(published=True).order_by('name')
    context = {
        'categories': categories,
    }
    return render(request, 'resources/index.html', context)


def category_detail(request, category_id):
    """
    Display details of a specific category along with its approved resources.

    This view fetches a published category by its ID and retrieves
    all approved resources associated with that category. It also identifies
    which of these resources are favorited by the current user.
    The resources can be sorted based on user preferences.

    :param request: The HTTP request object.
    :param category_id: The ID of the category to be displayed.

    **Context:**

    ``category``: The :model:`Category` object being viewed.
    ``resources``: A queryset of approved :model:`Resource` objects in the
    category, sorted as per user preference.
    ``favorite_resources``: A queryset of :model:`Resource` objects favorited
    by the current user.

    **Template:**

    :template:`resources/category_detail.html`
    """
    category = Category.objects.get(id=category_id, published=True)
    resources = category.resources.filter(approved=True)
    resources = resources.order_by('-created_at')
    if request.user.is_authenticated:
        favorite_resources = resources.filter(favorites=request.user)
    else:
        favorite_resources = []
    if resources.exists():
        resources = sort_resources(request, resources)

    context = {
        'category': category,
        'resources': resources,
        'favorite_resources': favorite_resources,
    }
    return render(request, 'resources/category_detail.html', context)


def submit_resource(request):
    """
    Handle the submission of a new resource.

    This view processes the resource submission form.
    If the request method is POST, it validates the form data,
    checks for duplicates, and saves the resource if valid.
    It also provides user feedback through messages.

    :param request: The HTTP request object.

    **Context:**

    ``form``: An instance of `ResourceForm`, either empty or populated
    with POST data.

    **Template:**

    :template:`resources/add_resource.html`
    """
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
                # Check if resource with the same URL already exists
                existing_resource_url = Resource.objects.filter(
                    url=resource.url
                ).first()
                if existing_resource_url:
                    messages.add_message(
                        request, messages.ERROR,
                        'A resource with this URL already exists.')
                    return HttpResponseRedirect(request.META.get(
                        'HTTP_REFERER', '/'
                        ))
                # Check if resource with the same name already exists
                existing_resource_name = Resource.objects.filter(
                    name=resource.name
                ).first()
                if existing_resource_name:
                    messages.add_message(
                        request, messages.ERROR,
                        'A resource with this name already exists.')
                    return HttpResponseRedirect(request.META.get(
                        'HTTP_REFERER', '/'
                        ))
                resource.uploader = request.user
                resource.approved = False
                resource.save()
                form.save_m2m()  # Save tags
                messages.add_message(
                    request, messages.SUCCESS,
                    'Resource submitted and awaiting approval.')
                # Reset the form after successful submission
                form = ResourceForm()
            else:
                messages.add_message(
                    request, messages.ERROR,
                    'There was an error submitting the resource. '
                    'Please try again.')
        else:
            form = ResourceForm()

        context = {
            'form': form,
        }
        return render(request, 'resources/add_resource.html', context)


def edit_resource(request, resource_id):
    """
    Handle the editing of an existing resource.

    This view allows the uploader of a resource to edit its details.
    If the request method is POST,
    it validates the form data and saves the changes if valid.
    It also provides user feedback through messages.

    :param request: The HTTP request object.
    :param resource_id: The ID of the resource to be edited.

    **Context:**

    ``form``: An instance of `ResourceForm`, either populated with the
    resource data or with POST data.
    ``resource``: The :model:`Resource` object being edited.

    **Template:**

    :template:`resources/add_resource.html`
    """
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
                resource = form.save(commit=False)
                resource.approved = False  # Re-approval after edit
                resource.save()
                form.save_m2m()  # Save tags
                messages.add_message(
                    request, messages.SUCCESS,
                    'Resource updated successfully and awaiting re-approval.')
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
    """
    Handle the deletion of an existing resource.

    This view allows the uploader of a resource to delete it.
    It provides user feedback through messages.

    :param request: The HTTP request object.
    :param resource_id: The ID of the resource to be deleted.

    **Context:**

    `resource`: The :model:`Resource` object being deleted.

    **Redirects to:**

    The homepage after deletion.
    """
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
    """
    Display the user's favorite resources.

    This view fetches all resources favorited by the current user
    and displays them.
    If the user is not authenticated, they are redirected to the login page.

    :param request: The HTTP request object.

    **Context:**

    ``favorite_resources``: A queryset of :model:`Resource` objects favorited
    by the current user.

    **Template:**

    :template:`resources/favorite_resources.html`
    """
    if not request.user.is_authenticated:
        messages.add_message(
            request, messages.ERROR,
            'You must be logged in to view your favorite resources.')
        return HttpResponseRedirect('/accounts/login/')
    else:
        favorite_resources = request.user.favorite_resources.all()
        favorite_resources = favorite_resources.order_by('-created_at')
        if favorite_resources.exists():
            favorite_resources = sort_resources(request, favorite_resources)

        context = {
            'favorite_resources': favorite_resources,
        }
        return render(request, 'resources/favorite_resources.html', context)


def favorite_resource(request, resource_id):
    """
    Toggle the favorite status of a resource for the current user.

    This view adds or removes a resource from the user's favorites
    based on its current status.
    If the user is not authenticated, an error message is displayed.

    :param request: The HTTP request object.
    :param resource_id: The ID of the resource to be favorited or unfavorited.

    **Context:**

    `resource`: The :model:`Resource` object being favorited or unfavorited.

    **Redirects to:**

    The referring page or homepage if no referrer is found.
    """
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
    """
    Handle the suggestion of a new category.

    This view processes the category suggestion form.
    If the request method is POST,
    it validates the form data, checks for duplicates,
    and saves the category if valid.
    It also provides user feedback through messages.

    :param request: The HTTP request object.

    **Context:**

    ``form``: An instance of `CategoryForm`, either empty or populated
    with POST data.

    **Template:**

    :template:`resources/category_suggestion.html`
    """
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
                # Check if category with the same name already exists
                existing_category = Category.objects.filter(
                    name__iexact=category.name
                    ).first()
                if existing_category:
                    messages.add_message(
                        request, messages.ERROR,
                        'A category with this name already exists.')
                    return HttpResponseRedirect(request.META.get(
                        'HTTP_REFERER', '/'
                        ))
                category.author = request.user
                # Automatically publish if the user is a superuser
                if request.user.is_superuser:
                    category.published = True
                else:
                    category.published = False
                category.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Category suggestion submitted and awaiting approval.')
                # Reset the form after successful submission
                form = CategoryForm()
            else:
                messages.add_message(
                    request, messages.ERROR,
                    'There was an error submitting the category. '
                    'Please try again.')
        else:
            form = CategoryForm()

        context = {
            'form': form,
        }
        return render(request, 'resources/category_suggestion.html', context)


def search_resources(request):
    """
    Handle the search for resources based on user queries.

    This view processes search queries submitted by users. It allows searching
    within resource names, descriptions, and keywords.
    The results can be sorted based on user preferences.

    :param request: The HTTP request object.

    **Context:**

    ``resources``: A queryset of :model:`Resource` objects matching
    the search criteria, sorted as per user preference.
    ``query``: The search query string.
    ``search_in``: A list of fields to search within
    (name, description, keywords).

    **Template:**

    :template:`resources/search_results.html`
    """
    query = request.GET.get('q', '')
    search_in = request.GET.getlist('in') or ['name']
    if query:
        resources = Resource.objects.filter(approved=True).order_by(
            '-created_at'
        )
    else:
        resources = []
    if query:
        # Build the Q object based on selected search fields
        q_objects = Q()
        # Search in name, description, and keywords as per user selection
        if 'name' in search_in:
            q_objects |= Q(name__icontains=query)
        if 'description' in search_in:
            q_objects |= Q(description__icontains=query)
        if 'keywords' in search_in:
            q_objects |= Q(keywords__name__icontains=query)
        # Filter resources based on the constructed Q object
        resources = resources.filter(q_objects).distinct()
        resources = sort_resources(request, resources)

    context = {
        'resources': resources,
        'query': query,
        'search_in': search_in,
    }
    return render(request, 'resources/search_results.html', context)
