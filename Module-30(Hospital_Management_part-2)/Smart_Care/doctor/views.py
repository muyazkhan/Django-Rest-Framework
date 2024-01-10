from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor,specialization,designation,AvailableTime,review
from .serializers import doctorserializers,designationserializers,AvailableTimeserializers,reviewserializers,specializationserializers

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = doctorserializers

class DesignatioViewSet(viewsets.ModelViewSet):
    queryset = designation.objects.all()
    serializer_class = designationserializers

class AvailableTimeViewSet(viewsets.ModelViewSet):
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeserializers

class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = specialization.objects.all()
    serializer_class = specializationserializers

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = review.objects.all()
    serializer_class = reviewserializers
