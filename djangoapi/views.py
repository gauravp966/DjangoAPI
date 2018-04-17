from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import emp
from .serializers import DataSerializer


class dataList(APIView):

    def get(self, request):
        data1 = emp.objects.all()
        serializer = DataSerializer(data1, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class dataDetails(APIView):

    def get_byId(self, empID):
        data1 = emp.objects.all()
        serializer = DataSerializer(data=empID.data)
        employer = [employer for employer in data1 if data1['id'] == serializer]
        return Response(employer)