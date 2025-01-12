from django.db import models

# Create your models here.


class ElectronicsModel(models.Model):
    CATEGORY_CHOICES = [
        ("Camera","Camera"),
        ("Laptop","Laptop"),
        ("Headphone","Headphone"),
        ("MobileAcc","MobileAcc"),
        ("Powerbank","Powerbank"),
        ("TV","TV"),
        ("WashingMachine","WashingMachine"),
        ("AC","AC"),
        ("Refrigerators","Refrigerators"),
        ("Mobile","Mobile"),
    ]
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    brand = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    rating_rate = models.FloatField(verbose_name="Average Rating")  
    rating_count = models.IntegerField(verbose_name="Total Ratings")
    rating_review = models.IntegerField(verbose_name="Total Review")
    highlight_1 = models.CharField(max_length=500,null=True, blank=True)
    highlight_2 = models.CharField(max_length=500,null=True, blank=True)
    highlight_3 = models.CharField(max_length=500,null=True, blank=True)
    highlight_4 = models.CharField(max_length=500,null=True, blank=True)
    highlight_5 = models.CharField(max_length=500,null=True, blank=True)
    seller = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.category} {self.brand} - ₹{self.price}"
