from django.contrib.auth.models import User,AbstractUser
from django.db import models
from django.utils import timezone


class UserProfile(AbstractUser):
    email = models.EmailField(max_length=254,unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30, blank=False)  # Required
    last_name = models.CharField(max_length=30, blank=False)   # Required
    class Meta:
        db_table = 'UserProfile'  # Set the desired table name

  

        

class Items(models.Model):
    item_id = models.AutoField(primary_key=True,unique=True)
    title = models.CharField(max_length=50)
    description= models.CharField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    user_profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'items'
