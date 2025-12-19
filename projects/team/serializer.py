from rest_framework import serializers
from championship.models import Championship
from championship.serializer import ChampionSerializer


class TeamSerializer(serializers.ModelSerializer):

    # Afficher les info du championship

    championship = ChampionSerializer(read_only=True)

    # Recevoir l'id du championship

    championship_id = serializers.PrimaryKeyRelatedField(

        queryset = Championship.objects.all(),
        source = 'championship',
        write_only= True
    )

    class Meta:
        model= Championship
        fields = ['id', 'team_name', 'championship', 'championship_id']