import requests

API_URL = 'https://api.deepai.org/api/fake-detector'  # Vérifie bien cette URL dans la doc DeepAI
API_KEY = 'ecb02c10-e45d-4454-bc7a-783b106847ef'      # Ta clé API

try:
    response = requests.post(API_URL, headers={'api-key': API_KEY})
    print("Statut HTTP:", response.status_code)
    print("Réponse API :", response.text)
except Exception as e:
    print("Erreur lors de l'appel API :", e)
