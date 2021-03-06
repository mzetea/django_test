from django.db import models
# from datetime import datetime

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=255, null=False, blank=True, unique=True)
    summary = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    date_added = models.DateField(auto_created=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.title

