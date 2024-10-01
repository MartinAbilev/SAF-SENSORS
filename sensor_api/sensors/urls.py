from django.urls import path
from . import views

urlpatterns = [
    path('sensors/', views.get_sensors_data, name='sensors_data'),
]
