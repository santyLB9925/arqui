from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from example.models import Example
from example.models import Example2

from example.serializer import ExampleSerializers
from example.serializer import Example2Serializers

class ExampleList(APIView):
    # METODO GET PARA SOLICITAR INFO
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Example.objects.filter(delete = False)
        #many = True Si aplica si retorno multiples objetos
        serializer = ExampleSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExampleSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class  ExampleDetail(APIView):
    def get_object(self, id):
        try:
            return Example.objects.get(pk=id, delete=False)
        except Example.DoesNotExist:
            return 404
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != 404:
            #many = True No aplica si retorno un solo objeto
            serializer = ExampleSerializers(example)
            return Response(serializer.data)
        else:
            return Response(example)
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != 404:
            serializer = ExampleSerializers(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)




# Create your views here.



class ExampleList2(APIView):
    # METODO GET PARA SOLICITAR INFO
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Example2.objects.filter(delete = False)
        #many = True Si aplica si retorno multiples objetos
        serializer = Example2Serializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Example2Serializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class  ExampleDetail2(APIView):
    def get_object(self, id):
        try:
            return Example2.objects.get(pk=id, delete=False)
        except Example2.DoesNotExist:
            return 404
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != 404:
            #many = True No aplica si retorno un solo objeto
            serializer = Example2Serializers(example)
            return Response(serializer.data)
        else:
            return Response(example)
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != 404:
            serializer = Example2Serializers(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)




# Create your views here.
