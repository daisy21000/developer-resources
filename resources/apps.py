from django.apps import AppConfig


class ResourcesConfig(AppConfig):
    """
    Provides primary key type for the resources application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'resources'
