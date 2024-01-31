from django.contrib.auth.models import User
from django.db import models

# models.py

from django.db import models

class ThreeDPrintOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stl_file = models.FileField(upload_to='stl_files/')
    size_description = models.TextField()
    color = models.CharField(max_length=100)

class LaserEngravingOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_description = models.TextField()
    bmp_file = models.FileField(upload_to='bmp_files/')
    description = models.TextField()
