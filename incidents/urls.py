from django.urls import path
from . import views

urlpatterns = [
    path('incidents/signaler/', views.signaler_incident, name='signaler_incident'),
    path('incidents/liste/', views.liste_incidents, name='liste_incidents'),
    path('incidents/gestion/', views.gestion_incidents, name='gestion_incidents'),
    path('incidents/detail/<int:incident_id>/', views.detail_incident, name='detail_incident'),
    path('incidents/<int:incident_id>/analyser-deepfake/', views.analyser_deepfake, name='analyser_deepfake'),
    path('incident/<int:incident_id>/commentaire/ajouter/', views.ajouter_commentaire, name='ajouter_commentaire'),

]