from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Cart_Items(models.Model):
    title = models.CharField(max_length=500) 
    image_url = models.URLField(blank=True, null=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    quantity = models.PositiveIntegerField(default=1) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.title} (x{self.quantity}) - {self.user.username}"