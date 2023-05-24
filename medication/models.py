from django.db import models
from drone.models import Drone

# Create your models here.
class Medication(models.Model):
    drone = models.ForeignKey(Drone,related_name='drone', on_delete=models.CASCADE)
    name = models.TextField(max_length=200)
    weight = models.DecimalField(decimal_places=1,max_digits=4)
    code = models.CharField(max_length=10)
    image = models.ImageField(upload_to='item_images',blank=True,null=True)

    def __str__(self):
        return f'{self.name}'