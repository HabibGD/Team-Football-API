from rest_framework import serializers
from .models import Championship


class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Championship
        fields = ['id', 'champ_name', 'country']