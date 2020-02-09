from rest_framework import serializers
from .models import Journal


class JournalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['url', 'id', 'title', 'body', 'date']
        model = Journal