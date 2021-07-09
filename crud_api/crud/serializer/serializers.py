"""Serializers allow complex data such as querysets and model instances to be converted to native 
Python datatypes that can then be easily rendered into JSON"""
from django.db import models
from rest_framework import serializers
from crud.models import Course
from crud.models import Wishlist


class CourseSerializer(serializers.ModelSerializer):
#class CourseSerializer for Course model
    class Meta:
        model = Course #Course class from models is passed as model
        fields = "__all__" #all the fields of course class is taken


class WishlistSerializer(serializers.ModelSerializer):
#class WishlistSerializer for Wishlist model
    class Meta:
        model = Wishlist #Wishlist class from models is passed as model
        fields = "__all__" #all the fields of wishlist class is taken