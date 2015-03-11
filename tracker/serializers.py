__author__ = 'tomnahass'
from django.contrib.auth.models import User
from django.forms import widgets
from rest_framework import serializers
from .models import Medication, Personal, FREQ, FORM

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ('rx_name','formulation', 'total_quantity',
                  'take_quantity', 'prn', 'freq')
        owner = serializers.ReadOnlyField(source='owner.username')

class UserSerializer(serializers.ModelSerializer):
    medications = serializers.PrimaryKeyRelatedField(many=True, queryset=Medication.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'medications')
