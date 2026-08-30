import pandas as pd

ventes_janvier = pd.DataFrame({
    "Produit": ["Clavier", "Souris", "Ecran"],
    "Quantite": [10, 25, 5],
    "Prix_unitaire": [45.0, 15.0, 200.0],
})

ventes_fevrier = pd.DataFrame({
    "Produit": ["Clavier", "Souris", "Webcam"],
    "Quantite": [8, 30, 12],
    "Prix_unitaire": [45.0, 15.0, 60.0],
})

ventes_janvier.to_excel("ventes_janvier.xlsx", index=False)
ventes_fevrier.to_excel("ventes_fevrier.xlsx", index=False)

print("Fichiers de test generes avec succes.")