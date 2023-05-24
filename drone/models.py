from django.db import models

# Create your models here.
class Drone(models.Model):
    DRONE_MODEL = [
        ('LIGHTWEIGHT', 'LIGHTWEIGHT'),
        ('MIDDLEWEIGHT','MIDDLEWEIGHT'),
        ('CRUISERWEIGHT', 'CRUISERWEIGHT'),
        ('HEAVYWEIGHT','HEAVYWEIGHT')]
    DRONE_STATE = [
         ('IDLE','IDLE'),
        ('LOADING', 'LOADING'),
         ('LOADED', 'LOADED'),
        ('DELIVERING', 'DELIVERING'),
        ('DELIVERED', 'DELIVERED'),
        ('RETURNING','RETURNING'),]
    serial_number = models.CharField(max_length=100,primary_key=True)
    drone_model = models.CharField(
        max_length=13,
        choices=DRONE_MODEL,
        )
    weight_limit = models.DecimalField(decimal_places=1,max_digits=4)
    battery_capacity = models.IntegerField()
    state = models.CharField(
        max_length=13,
        choices=DRONE_STATE,
        default='IDLE',
        )
    
    def get_weight(self):
        return self.weight_limit

    def __str__(self):
        return f"{self.drone_model} {self.serial_number}"

