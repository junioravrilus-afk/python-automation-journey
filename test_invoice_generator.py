from invoice_generator import load_clients


def test_load_clients_calculates_total(tmp_path):
    csv_content = "nom,produit,quantite,prix_unitaire\nTest Client,Produit Test,2,100\n"
    csv_file = tmp_path / "test_clients.csv"
    csv_file.write_text(csv_content, encoding="utf-8")

    clients = load_clients(csv_file)

    assert len(clients) == 1
    assert clients[0]["montant_total"] == 200.0

