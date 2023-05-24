from django.shortcuts import render
from .models import Medication
from drone.models import Drone
from drone.serializers import DroneSerializer 
from .serializers import MedicationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import re

# Create your views here.
@api_view(['GET'])
def get_meds(request):
    meds = Medication.objects.select_related('drone').all()
    ser = MedicationSerializer(meds, many=True)
    return Response({'drones':ser.data})

@api_view(['POST'])
def load_med(request):
    try:
        drone = Drone.objects.get(serial_number=request.data['drone'])
        if drone.state != 'IDLE':
            return Response({'message':f"drone {drone.serial_number} cannot be loaded, find another drone in idle state "},status=status.HTTP_400_BAD_REQUEST)
        elif drone.battery_capacity < 25:
            return Response({'message':f"drone {drone.serial_number} battery is too low to load"},status=status.HTTP_400_BAD_REQUEST)
        elif not re.match('^[A-Z0-9_]*$',request.data['code']):
            return Response({'message':f"code for medication should be uppercase letters and underscore only"},status=status.HTTP_400_BAD_REQUEST)
        elif not re.match('^[a-zA-Z0-9_-]*$',request.data['name']):
            return Response({'message':f"code for medication should be letters,numbers, underscore and hypen only"},status=status.HTTP_400_BAD_REQUEST)
        elif request.data['weight'] > drone.weight_limit:
            return Response({'message':f"weight exceed the weight limit for the drone {drone.weight_limit}"},status=status.HTTP_400_BAD_REQUEST)
        else:
            ser = MedicationSerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                drone.state = 'LOADED'
                drone.save()
                return Response({'med':ser.data},status=status.HTTP_201_CREATED)
    except Drone.DoesNotExist:
        return Response({'message':f"Drone with the serial number {request.data['drone']} do not exist"},status=status.HTTP_404_NOT_FOUND,)
    
@api_view(['GET'])
def get_med(request):
    meds = Medication.objects.all().filter(drone=request.data['drone'])
    ser = MedicationSerializer(meds,many=True)
    return Response({'loaded_meds':ser.data},status=status.HTTP_200_OK)