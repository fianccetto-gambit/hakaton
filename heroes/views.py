from django.shortcuts import render
from rest_framework import generics
from .models import Hero
from .serializers import HeroSerializer

class HeroAPIView(generics.ListAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
