from django.db import models


# Create your models here.
class Request(models.Model):
    """
    Model representing a contact request.

    Fields:
    - name (CharField): The name of the person making the request.
    - email (EmailField): The email address of the person making the request.
    - message (TextField): The message content of the request.
    - created_at (DateTimeField): The timestamp when the request was created.
    - read (BooleanField): A boolean indicating whether the request has been read.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        # Return a string representation of the contact request
        return f"Request from {self.name} <{self.email}>"

    class Meta:
        # Set default ordering to show newest requests first
        ordering = ['-created_at']
