from django.db import models

# Create your models here.

class FashionModel(models.Model):
    CATEGORY_CHOICES = [
        ("MenTopWear","MenTopWear"),
        ("MenBottomWear","MenBottomWear"),
        ("MenFootWear","MenFootWear"),
        ("WomenEthnicWear","WomenEthnicWear"),
        ("WomenFootWear","WomenFootWear"),
        ("kids","kids"),
    ]
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    brand = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    rating_rate = models.FloatField(verbose_name="Average Rating")  
    rating_count = models.IntegerField(verbose_name="Total Ratings")
    rating_review = models.IntegerField(verbose_name="Total Review")
    size = models.CharField(max_length=10, null=True ,blank=True )
    seller = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.category} {self.brand} - ₹{self.price}"