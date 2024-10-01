from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
import json

def get_sensors_data(request):
    with open('sensors.json') as sensors_file:
        sensors_data = json.load(sensors_file)
    with open('metrics.json') as metrics_file:
        metrics_data = json.load(metrics_file)
    with open('sensorTypes.json') as sensor_types_file:
        sensor_types_data = json.load(sensor_types_file)

    # Process data to return a structured response
    response_data = {
        'sensors': sensors_data,
        'metrics': metrics_data['data']['items'],
        'sensor_types': sensor_types_data
    }

    return JsonResponse(response_data)

