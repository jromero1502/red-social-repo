from django.db import models


class User(models.Model):

    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    names = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    password = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Usuario: {self.username}"
