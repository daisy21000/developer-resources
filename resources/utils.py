from django.db.models import Count


def sort_resources(request, resources):
    """
    Sort resources based on user-selected criteria.

    :param request: The HTTP request object containing GET parameters.
    :param resources: A queryset of :model:`Resource` objects to be sorted.
    """
    sort_by = request.GET.get('sort_by', 'alphabetical')
    if sort_by == 'alphabetical':
        resources = resources.order_by('name')
    elif sort_by == 'newest':
        resources = resources.order_by('-created_at')
    elif sort_by == 'oldest':
        resources = resources.order_by('created_at')
    elif sort_by == 'most_favorited':
        # Annotate each resource with the count of favorites and order by that count
        resources = resources.annotate(num_favorites=Count('favorites', distinct=True)).order_by('-num_favorites')
    return resources
