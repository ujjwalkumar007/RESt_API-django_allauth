from datetime import date
from django.db.models import fields
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Wishlist
from crud.serializer.serializers import CourseSerializer, WishlistSerializer
from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Course_Description(request):
    """
    Function to perfom CRUD operations
    """
    if request.method == 'GET':  # for retrieving the data
        # course variable in which all the data of Course class is stored
        course = Course.objects.all()
        # we are using the serializer which we have created 
        serializer = CourseSerializer(course, many=True)
        # data is returned in proper JSON format
        return Response(serializer.data)

    elif request.method == 'POST':
        #if method is post we are going to add new data to the table
        serializer = CourseSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save() #if data is valid table is updated and we get response in proper JSON format
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#else we will get error

    elif request.method == 'PUT':
        #if method is put we are going to update the table
        id = request.data.get('id') #whatever id we are passing  should be equal to the id we want to updated
        course = Course.objects.get(pk=id)
        serializer = CourseSerializer(
            course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) #data is updated and returned in proper JSON format
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#else we will see an error

    elif request.method == 'DELETE':
        #if method is delete we are going to delete the table
        course = Course.objects.all()
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Wishlist_Description(request):
    """
    Function to perfom CRUD operations
    """

    if request.method == 'GET': #for retrieving the data
        wishlist = Wishlist.objects.all() # wishlist variable in which all the data of Wishlist class is stored
        serializer = WishlistSerializer(wishlist, many=True) # we are using the serializer which we have created
        return Response(serializer.data) ## data is returned in proper JSON format

    elif request.method == 'POST':
        #if method is post we are going to add new data to the table
        serializer = WishlistSerializer(data=request.data) # we are using the serializer which we have created
        if serializer.is_valid(): ##if data is valid table is updated and we get response in proper JSON format
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#else we will get an error

    elif request.method == 'PUT':
        #if method is put we are going to update the table
        id = request.data.get('id') ##whatever id we are passing  should be equal to the id we want to updated
        wishlist = Wishlist.objects.get(pk=id)
        serializer = WishlistSerializer(wishlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) ##data is updated and returned in proper JSON format
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#else we will get an error

    elif request.method == 'DELETE':
        #if method is delete we are going to delete the table
        wishlist = Wishlist.objects.all()
        wishlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



        