from rest_framework import serializers
from .models import Drone

class DroneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drone
        fields = ['serial_number','drone_model','weight_limit','battery_capacity','state']
    
