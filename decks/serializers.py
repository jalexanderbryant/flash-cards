from rest_framework import serializers
from . import models

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'created_at', 'last_reviewed', 'count')
        model = models.Deck

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'front', 'back', 'belongs_to_deck')
        model = models.Card
