from django.urls import path
from .views import TeamView, TeamDetailView

urlpatterns = [
    path('teams/', TeamView.as_view(), name='team'),
    path('teams/<int:pk>/',
         TeamDetailView.as_view(), name='team-update'),


]
