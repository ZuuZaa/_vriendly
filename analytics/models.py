from django.db import models

# Create your models here.
class Session(models.Model):
    
    email = models.EmailField(max_length=150)
    user_IP = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    user_type = models.CharField(max_length=150)
    log_in_time = models.DateTimeField()
    log_out_time = models.DateTimeField()
    duration = models.CharField(max_length=50)