from django.shortcuts import render
import json
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
