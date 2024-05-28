import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Car, Color, Brand


class CarSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    brand_id = serializers.IntegerField()
    color_id = serializers.IntegerField()
    speed = serializers.IntegerField()
    price = serializers.FloatField()
    created = serializers.DateTimeField(read_only=True)
    published = serializers.BooleanField(default=True)


class ColorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=35)
    created = serializers.DateTimeField(read_only=True)
    published = serializers.BooleanField(default=True)


class BrandSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    created = serializers.DateTimeField(read_only=True)
    published = serializers.BooleanField(default=True)


# class NewSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#
#
# class News:
#     def __init__(self, name, content):
#         self.name = name
#         self.content = content
#
#
# def serialization():
#     news1 = News("test", "test content")
#     serializer = NewSerializer(news1)
#     print(serializer.data)
#
#     json = JSONRenderer().render(serializer.data)
#     print(json)
#     print(type(json))
#
#
# def deserialization():
#     json = b'{"name":"test","content":"test content"}'
#     stream = io.BytesIO(json)
#     data = JSONParser().parse(stream)
#     print(data, "Json parser object")
#
#     serializer = NewSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
