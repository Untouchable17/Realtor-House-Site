from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions

from src.realtor_app import models
from src.realtor_app import serializers


class RealtorListAPIView(ListAPIView):

    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.RealtorSerializer
    queryset = models.Realtor.objects.all()
    pagination_class = None


class RealtorAPIView(RetrieveAPIView):

    serializer_class = serializers.RealtorSerializer
    queryset = models.Realtor.objects.all()


class RatingTopAPIView(ListAPIView):

    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.RealtorSerializer
    queryset = models.Realtor.objects.filter(rating_top=True)
    pagination_class = None


