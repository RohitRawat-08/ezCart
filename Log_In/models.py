from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Address(models.Model):
    STATE_CHOICES = [
        ('Uttarakhand', 'Uttarakhand'),
        ('Bihar', 'Bihar'),      
        ('Haryana', 'Haryana'),               
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'), 
        ('Delhi', 'Delhi'),
        ('Tamil Nadu', 'Tamil Nadu'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uname = models.CharField(max_length=100, verbose_name="Name")
    number = models.CharField(max_length=10, verbose_name="Mobile Number",unique=True)
    pincode = models.CharField(max_length=6, verbose_name="Pincode")
    locality = models.CharField(max_length=150,blank=True, verbose_name="Locality")
    address = models.CharField(max_length=500,verbose_name="Address (Area / Street)")
    city = models.CharField(max_length=100, verbose_name="City/District/Town")
    state = models.CharField(max_length=50, choices=STATE_CHOICES, verbose_name="State")
    landmark = models.CharField(max_length=150, blank=True, null=True, verbose_name="Landmark (Optional)")
    alternate_number = models.CharField(max_length=10, blank=True, null=True, verbose_name="Alternate Phon(Optional)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.uname} - {self.city}, {self.state}"



class ProfileImage(models.Model):
    image = models.ImageField(default='profile.png')
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile Image"



class MyOrdersModel(models.Model):
    order_id = models.CharField(max_length=20,unique=True,blank=False,primary_key=True)
    title = models.CharField(max_length=500)
    img_url = models.URLField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    order_date = models.DateField(default=now)
    order_time = models.TimeField(default=now)
    created_at = models.DateTimeField(default=now)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Shipped', 'Shipped'),
            ('Delivered', 'Delivered'),
            ('Cancelled', 'Cancelled')
        ],
        default='Pending'
    )

    def __str__(self):
        return f"{self.title} - {self.status}"