from django.db import models

# Create your models here.
class Material(models.Model):
    """Material object"""
    name = models.CharField(max_length=100)
    properties = models.JSONField(default=dict)
    access = models.CharField(max_length=10, default = 'admin')

    def __str__(self):
        return self.name