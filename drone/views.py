from django.shortcuts import render

# Create your views here.
from .models import Drone
from .serializers import DroneSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def drone_list(request):
    drone = Drone.objects.all()
    ser = DroneSerializer(drone, many=True)
    return Response({'drones':ser.data})

@api_view(['POST'])    
def register_drone(request):
    ser = DroneSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response({'serial_number':ser.data['serial_number']}, status=status.HTTP_201_CREATED)
    else:
        print(ser.error_messages)  

@api_view(['GET']) 
def available_drone(request):
    drone = Drone.objects.all().filter(state="IDLE")
    ser = DroneSerializer(drone, many=True)
    return Response({'available_drones':ser.data})


@api_view(['GET','PUT','DELETE'])
def drone_details(request):
    try:
        print(request.data)
        drone = Drone.objects.get(serial_number=request.data['serial_number'],)
    except Drone.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        ser = DroneSerializer(drone)
        return Response(ser.data)
    elif request.method == 'PUT':
        ser = DroneSerializer(drone, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
    elif request.method =='DELETE':
        drone.delete()
        return Response({'message':f'drone with the serial number {drone.serial_number} has been deleted'},status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def battery_level(request):
    try:
        drone = Drone.objects.get(serial_number=request.data['serial_number'],)
        ser = DroneSerializer(drone)
        battery_level = ser.data['battery_capacity']
        return Response({'battery_level':f'{battery_level}%'})
    except Drone.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
        