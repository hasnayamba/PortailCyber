import random

def detect_deepfake_api(file_path):
    # Juste un test simulé
    score = random.uniform(0, 1)
    rapport = f"Simulation détection deepfake : confiance estimée à {score*100:.2f}%"
    return score, rapport
