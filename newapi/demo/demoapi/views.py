from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class AudioListView(generics.ListCreateAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer

    
class AudioView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AudioSerializer
    queryset = Audio.objects.all()

class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    def retrieve(self, request, pk):
        queryset = Category.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(user)
        return Response(serializer.data)
