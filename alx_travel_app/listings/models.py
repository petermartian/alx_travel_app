from django.db import models

class Listing(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location    = models.CharField(max_length=100)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    available   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
