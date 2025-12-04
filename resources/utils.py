from django.db.models import Count


def sort_resources(request, resources):
    sort_by = request.GET.get('sort_by', 'alphabetical')
    if sort_by == 'alphabetical':
        resources = resources.order_by('name')
    elif sort_by == 'newest':
        resources = resources.order_by('-created_at')
    elif sort_by == 'oldest':
        resources = resources.order_by('created_at')
    elif sort_by == 'most_favorited':
        resources = resources.annotate(num_favorites=Count('favorites', distinct=True)).order_by('-num_favorites')
    return resources
