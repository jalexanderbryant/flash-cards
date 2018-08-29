from django.db import models

# Create your models here.


class Deck(models.Model):
    name = models.CharField(max_length=100, unique = True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_reviewed = models.DateTimeField(auto_now_add=True)
    card_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Card(models.Model):
    front = models.TextField()
    back = models.TextField()
    # Associate with a deck
    belongs_to_deck = models.ForeignKey('decks.Deck',
        related_name='cards',
        on_delete='models.CASCADE')

    def __str__(self):
        return self.front
