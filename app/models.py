from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.
class account_profile (models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id_user=models.IntegerField()
    bio=models.TextField(blank=True)
    profile_image=models.ImageField(upload_to='profile_image',default='blank-image')
    location=models.CharField(blank=True,max_length=100)
    
    def __str__(self) -> str:
        return self.user.username 