from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions

from src.strainer import serializers
from src.strainer import models
from datetime import datetime, timezone, timedelta


class HousesAPIView(ListAPIView):

    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.HouseSerializer

    queryset = models.House.objects.order_by('-created_at').filter(is_published=True)

    filter_backends = [SearchFilter]
    search_fields = ['title']
    lookup_field = "slug"


class HouseAPIView(RetrieveAPIView):
    serializer_class = serializers.HouseDetailSerializer
    queryset = models.House
    lookup_field = "slug"


class SearchView(APIView):

    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.HouseSerializer

    filter_backends = [SearchFilter]
    search_fields = ['title']
