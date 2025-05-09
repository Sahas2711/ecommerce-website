from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    # ForeignKey to link each product to a specific user (for user-based filtering)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # The text field for the customer's product description or details
    text = models.TextField(max_length=240)
    
    # An image field for uploading product photos
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    
    # Timestamps to track when the product was created and last updated
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # String representation for easier identification in admin and logs
        return f'{self.user.username} - {self.text[:10]}'
