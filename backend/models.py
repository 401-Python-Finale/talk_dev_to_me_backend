from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class User_Profile(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=64) # NEEDED???
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now=True)
    # POST -  Separate Models?


    def __str__(self):
        return self.title