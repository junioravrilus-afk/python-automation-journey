import pandas as pd
from excel_report_generator import consolidate_by_product


def test_consolidate_sums_quantities():
    data = pd.DataFrame({
        "Produit": ["Clavier", "Clavier", "Souris"],
        "Quantite": [10, 8, 25],
        "Prix_unitaire": [45.0, 45.0, 15.0],
    })

    result = consolidate_by_product(data)

    clavier_row = result[result["Produit"] == "Clavier"]
    assert clavier_row["Quantite"].values[0] == 18


def test_consolidate_averages_price():
    data = pd.DataFrame({
        "Produit": ["Clavier", "Clavier"],
        "Quantite": [10, 8],
        "Prix_unitaire": [40.0, 50.0],
    })

    result = consolidate_by_product(data)

    clavier_row = result[result["Produit"] == "Clavier"]
    assert clavier_row["Prix_unitaire"].values[0] == 45.0