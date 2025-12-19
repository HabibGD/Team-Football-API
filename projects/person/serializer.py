from rest_framework import serializers
from team.serializer import TeamSerializer
from team.models import Team
from .models import Person


class PersonSerializer(serializers.ModelSerializer):

    teams = TeamSerializer(read_only=True)

    team_id = serializers.PrimaryKeyRelatedField(

        many= True,
        queryset = Team.objects.all(),
        source = 'teams',
        write_only= True
    )

    class Meta:
        model= Person
        fields = ['id', 'fullname', 'sexe', 'teams', 'team_id']


