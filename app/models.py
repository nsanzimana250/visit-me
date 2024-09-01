from django.db import models
from django.contrib import admin

class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.fullname} ({self.email})"

class Project(models.Model):
    logo = models.ImageField(upload_to='logos/')
    website_name = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    link = models.URLField()

    def __str__(self) -> str:
        return f"{self.website_name} ({self.link})"
