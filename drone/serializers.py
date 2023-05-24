from rest_framework import serializers
from .models import Drone,AuditLog

class DroneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drone
        fields = ['serial_number','drone_model','weight_limit','battery_capacity','state']
    

class AuditLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuditLog
        fields = ['drone','battery_capacity','created_at']
