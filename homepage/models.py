from django.contrib.auth.models import User
from django.db import models

# models.py

from django.db import models

from django.contrib.auth.models import User
from django.db import models

# Define color choices
COLOR_CHOICES = [
    ('gold', 'Gold'),
    ('silk', 'Rainbow'),
    ('white', 'White'),
]

class ThreeDPrintOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stl_file = models.FileField(upload_to='stl_files/')
    size_description = models.TextField()
    color = models.CharField(max_length=100, choices=COLOR_CHOICES)

class LaserEngravingOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_description = models.TextField()
    bmp_file = models.FileField(upload_to='bmp_files/')
    what_material = models.CharField(max_length=25)
