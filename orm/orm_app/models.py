from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(null=False, max_length=30, default='John')
    last_name = models.CharField(null=False, max_length=30, default='doe')
    dob = models.DateField(null=True)
    