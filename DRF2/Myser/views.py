from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.viewsets import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from Myser.serializers import *


class StudentVS(viewsets.ModelViewSet):
    pass


class StudentAPIView(APIView):

    def get(self, request):
        # print("In APIview get ")
        # return None
        stus = Student.objects.all()  # 拿到学生的所有数据，得到一个查询集合即query_set
        ser = StudentSerializers(stus, many=True)  # 这一步不就是序列化吗，得到一个序列化类型
        return Response(data=ser.data)  # ser.data 得到序列化结果，就是json数据，类似于字典


class StudentGenAPIView(generics.GenericAPIView):

    queryset = Student.objects.all()  # 拿到学生的所有数据，得到一个查询集合即query_set
    serializer_class = StudentSerializers

    def get(self, request):
        ser = self.serializer_class(self.get_queryset(), many=True)  # 这一步不就是序列化吗，得到一个序列化类型
        return Response(data=ser.data)  # ser.data 得到序列化结果，就是json数据，类似于字典


