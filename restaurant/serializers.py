from rest_framework import serializers
from .models import Menu, Booking


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']
        extra_kwargs = {
            'price': {'min_value': 5},
            'inventory': {'min_value': 0},
        }


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'name', 'no_of_guests', 'booking_date']
        extra_kwargs = {
            'no_of_guests': {'min_value': 1},
        }
