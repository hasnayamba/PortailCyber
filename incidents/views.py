from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Commentaire, Incident
from users.decorators import role_required
from django.utils import timezone
from .deepfake_detector import detect_deepfake_api
from django.db.models import Prefetch

@login_required(login_url='login')
def signaler_incident(request):
    if request.method == 'POST':
        type_incident = request.POST.get('type_incident')
        description = request.POST.get('description')
        geoloc = request.POST.get('geolocalisation')

        preuve_image = request.FILES.get('preuve_image')
        preuve_video = request.FILES.get('preuve_video')
        preuve_log = request.FILES.get('preuve_log')

        if not type_incident or not description:
            messages.error(request, "Veuillez remplir les champs obligatoires.")
            return redirect('signaler_incident')

        # Création de l'incident
        incident = Incident.objects.create(
            user=request.user,
            type_incident=type_incident,
            description=description,
            geolocalisation=geoloc,
            preuve_image=preuve_image,
            preuve_video=preuve_video,
            preuve_log=preuve_log,
        )

        # Détection deepfake si image ou vidéo
        fichier = None
        if incident.preuve_image:
            fichier = incident.preuve_image.path
        elif incident.preuve_video:
            fichier = incident.preuve_video.path

        if fichier:
            try:
                score, rapport = detect_deepfake_api(fichier)
                if score is not None:
                    incident.deepfake_score = score
                    incident.deepfake_rapport = rapport
                    incident.deepfake_analyse_date = timezone.now()
                    incident.save()
            except Exception as e:
                print("Erreur API deepfake :", e)

        messages.success(request, "Signalement envoyé avec succès.")
        return redirect('liste_incidents')

    return render(request, 'incidents/signaler_incident.html')



@login_required(login_url='login')
def liste_incidents(request):
    incidents = request.user.incidents.all().order_by('-date_signalement').prefetch_related(
        Prefetch('commentaires', queryset=Commentaire.objects.order_by('-date_creation'), to_attr='commentaires_ordonnees')
    )
    return render(request, 'incidents/liste_incidents.html', {'incidents': incidents})


@login_required(login_url='login')
@role_required(['autorite', 'expert'])
def gestion_incidents(request):
    incidents = Incident.objects.all().order_by('-date_signalement')
    return render(request, 'incidents/gestion_incidents.html', {'incidents': incidents})


@login_required(login_url='login')
@role_required(['autorite', 'expert'])
def detail_incident(request, incident_id):
    incident = get_object_or_404(Incident, id=incident_id)

    if request.method == 'POST':
        statut = request.POST.get('statut')
        if statut in ['en_attente', 'en_cours', 'resolu']:
            incident.statut = statut
            incident.save()
            messages.success(request, "Statut mis à jour.")
            return redirect('gestion_incidents')
        else:
            messages.error(request, "Statut invalide.")

    return render(request, 'incidents/detail_incident.html', {'incident': incident})

@login_required(login_url='login')
@role_required(['autorite', 'expert'])  # seul un rôle autorisé peut analyser
def analyser_deepfake(request, incident_id):
    incident = get_object_or_404(Incident, id=incident_id)

    fichier = None
    if incident.preuve_image:
        fichier = incident.preuve_image.path
    elif incident.preuve_video:
        fichier = incident.preuve_video.path

    if not fichier:
        messages.error(request, "Aucun fichier image ou vidéo à analyser.")
        return redirect('detail_incident', incident_id=incident.id)

    score, rapport = detect_deepfake_api(fichier)

    if score is not None:
        incident.deepfake_score = score
        incident.deepfake_rapport = rapport
        incident.deepfake_analyse_date = timezone.now()
        incident.save()
        messages.success(request, "Analyse Deepfake effectuée avec succès.")
    else:
        messages.error(request, f"Erreur lors de l'analyse : {rapport}")

    return redirect('detail_incident', incident_id=incident.id)



@login_required(login_url='login')
def ajouter_commentaire(request, incident_id):
    incident = get_object_or_404(Incident, id=incident_id)

    if request.method == 'POST':
        contenu = request.POST.get('contenu')
        if contenu:
            Commentaire.objects.create(
                incident=incident,
                user=request.user,
                contenu=contenu
            )
            messages.success(request, "Commentaire ajouté avec succès.")
        else:
            messages.error(request, "Le commentaire ne peut pas être vide.")

    return redirect('detail_incident', incident_id=incident.id)