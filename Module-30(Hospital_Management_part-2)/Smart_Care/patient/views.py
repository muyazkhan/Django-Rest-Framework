
from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient
from .serializers import patient

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = patient
# Create your views here.
