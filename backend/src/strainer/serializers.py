from rest_framework import serializers
from src.strainer import models


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.House
        exclude = ("description", )


class HouseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.House
        fields = "__all__"
        lookup_field = "slug"
