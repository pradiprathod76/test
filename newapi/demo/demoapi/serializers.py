from .models import *
from rest_framework import serializers,fields

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ('id','img','name','des','audio','cg','sub','date')

class CategorySerializer(serializers.ModelSerializer):
    cg_audio = AudioSerializer(read_only=True, many=True,required=False)

    class Meta:
        model = Category
        fields = ('id', 'img', 'name', 'des', 'cg_audio')