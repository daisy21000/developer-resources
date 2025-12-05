from django.db import models


# Create your models here.
class Request(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Request from {self.name} <{self.email}>"

    class Meta:
        ordering = ['-created_at']
