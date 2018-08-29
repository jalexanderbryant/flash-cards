from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from .models import Deck, Card
from .serializers import DeckSerializer, CardSerializer


# For all decks
class DeckList(generics.ListAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

# For single deck
class DeckDetail(generics.RetrieveAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer


# For all cards
class CardDetail(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

# For single card
class CardDetail(generics.RetrieveAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
