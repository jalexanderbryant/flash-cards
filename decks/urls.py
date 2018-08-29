from django.urls import path

from . import views

urlpatterns = [
  path('decks/', views.DeckList.as_view()),
  path('decks/<int:pk>/', views.DeckDetail.as_view())
]