from django.db import models

# Create your models here.

class Blog(models.Model):

    LIGHT = 'light'

    DARK = 'dark'

    STYLES = [
        [LIGHT, 'Light version'],
        [DARK, 'Dark version']
    ]

    name = models.CharField(max_length=150)

    description = models.TextField(null=True, blank=True, max_length=400)

    creation_date = models.DateTimeField(auto_now_add=True)

    modification_date = models.DateTimeField(auto_now=True)

    style = models.CharField(max_length=5, choices=STYLES)

    def __str__(self):
        return self.name