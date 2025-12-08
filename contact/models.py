from django.db import models


# Create your models here.
class Request(models.Model):
    """
    Model representing a contact request.

    Fields:
    - name: The name of the person making the request.
    - email: The email address of the person making the request.
    - message: The message content of the request.
    - created_at: The timestamp when the request was created.
    - read: A boolean indicating whether the request has been read.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Request from {self.name} <{self.email}>"

    class Meta:
        ordering = ['-created_at']
