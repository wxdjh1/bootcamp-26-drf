from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=9999999)
    description = models.CharField(max_length=999999999999)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.title

