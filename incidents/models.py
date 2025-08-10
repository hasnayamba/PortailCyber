from django.db import models
from django.conf import settings

class Incident(models.Model):
    TYPE_CHOICES = [
        ('phishing', 'Phishing'),
        ('malware', 'Malware'),
        ('cyberharcelement', 'Cyberharcèlement'),
        ('deepfake', 'Deepfake'),
        ('desinformation', 'Désinformation'),
        ('autre', 'Autre'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='incidents')
    type_incident = models.CharField(max_length=50, choices=TYPE_CHOICES)
    description = models.TextField()
    date_signalement = models.DateTimeField(auto_now_add=True)
    geolocalisation = models.CharField(max_length=255, blank=True, null=True)

    preuve_image = models.ImageField(upload_to='preuves/images/', blank=True, null=True)
    preuve_video = models.FileField(upload_to='preuves/videos/', blank=True, null=True)
    preuve_log = models.FileField(upload_to='preuves/logs/', blank=True, null=True)

    statut = models.CharField(max_length=20, default='en_attente', choices=[
        ('en_attente', 'En attente'),
        ('en_cours', 'En cours'),
        ('resolu', 'Résolu'),
    ])
    
    deepfake_score = models.FloatField(null=True, blank=True)  # 0 à 1 par ex.
    deepfake_analyse_date = models.DateTimeField(null=True, blank=True)
    deepfake_rapport = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Incident #{self.id} ({self.type_incident}) signalé par {self.user.username}"
    
    
class Commentaire(models.Model):
    incident = models.ForeignKey('Incident', on_delete=models.CASCADE, related_name='commentaires')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire #{self.id} par {self.user.username} sur incident #{self.incident.id}"
