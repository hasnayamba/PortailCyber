# 🚨 Portail Cyber - Gestion des Incidents avec Analyse Deepfake

Une plateforme Django permettant de signaler, gérer et analyser des incidents (cybersécurité, arnaques, contenus suspects).  
Elle intègre la possibilité d’analyser des preuves (images/vidéos) pour détecter des deepfakes.

---

## 📌 Fonctionnalités
📌 Gestion des utilisateurs : Inscription, connexion, rôles.

🚨 Signalement d’incidents : Formulaire avec upload d’images/vidéos/logs.

🔍 Analyse Deepfake (mode simulateur).

💬 Commentaires sur incidents.

📍 Géolocalisation Google Maps.

🗄 Gestion administrateur via Django Admin.

---

## 🛠 Technologies utilisées
- **Backend :** Django 5.x
- **Base de données :** PostgreSQL
- **Frontend :** HTML5, Bootstrap
- **API externes :** Deepfake detection (ou simulation via script)
- **Autres :**
  - Pillow (gestion images)
  - Requests (appels API)
  - Python Decouple (gestion variables d’environnement)

---

## 📂 Structure du projet
.
├── .env                         # Variables d'environnement (config Django, DB…)
├── .gitignore                   # Fichiers/Dossiers à ignorer par Git
├── manage.py                    # Commande principale Django
├── requirements.txt             # Dépendances Python
├── structure.txt                # Arborescence exportée
├── test_deepai.py               # Script de test API Deepfake
│
├── incidents/                   # Application Django pour la gestion des incidents
│   ├── admin.py
│   ├── apps.py
│   ├── deepfake_detector.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/              # Historique des migrations de base de données
│   └── templates/incidents/     # Templates HTML pour incidents
│       ├── base.html
│       ├── detail_incident.html
│       ├── gestion_incidents.html
│       ├── liste_incidents.html
│       └── signaler_incident.html
│
├── media/                       # Fichiers uploadés (preuves images/vidéos/logs)
│   └── preuves/images/
│
├── portail_cyber/               # Répertoire principal du projet Django
│   ├── settings.py               # Configuration générale (DB, apps…)
│   ├── urls.py                   # Routage global
│   ├── asgi.py
│   ├── wsgi.py
│
└── users/                       # Application Django pour gestion des utilisateurs
    ├── admin.py
    ├── apps.py
    ├── decorators.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── migrations/              # Historique des migrations utilisateurs
    └── templates/users/         # Templates HTML pour utilisateurs
        ├── dashboard.html
        ├── login.html
        ├── protected.html
        └── register.html
