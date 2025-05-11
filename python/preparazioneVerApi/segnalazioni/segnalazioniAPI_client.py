import requests
from datetime import datetime

BASE_URL = "http://127.0.0.1:5000"

def aggiungi_quartiere():
    nome = input("Nome del nuovo quartiere: ")
    resp = requests.post(f"{BASE_URL}/quartieri", json={"nome": nome})
    print(resp.json())

def lista_quartieri():
    resp = requests.get(f"{BASE_URL}/quartieri")
    for q in resp.json():
        print(f"- {q['nome']}")

def inserisci_segnalazione():
    quartiere = input("Nome quartiere: ")
    categoria = input("Categoria (es. strada, rifiuti...): ")
    descrizione = input("Descrizione problema: ")
    stato = input("Stato (invio per default): ").strip()
    payload = {
        "quartiere": quartiere,
        "categoria": categoria,
        "descrizione": descrizione,
    }
    if stato:
        payload["stato"] = stato
    payload["data_ora"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    resp = requests.post(f"{BASE_URL}/segnalazioni", json=payload)
    print(resp.json())

def aggiorna_stato():
    id_segn = input("ID segnalazione: ")
    nuovo_stato = input("Nuovo stato: ")
    resp = requests.put(f"{BASE_URL}/segnalazioni/{id_segn}", json={"stato": nuovo_stato})
    print(resp.json())

def filtra_segnalazioni():
    stato = input("Filtro stato (invio per ignorare): ")
    categoria = input("Filtro categoria: ")
    quartiere = input("Filtro quartiere: ")

    params = {}
    if stato:
        params["stato"] = stato
    if categoria:
        params["categoria"] = categoria
    if quartiere:
        params["quartiere"] = quartiere

    resp = requests.get(f"{BASE_URL}/segnalazioni", params=params)
    for seg in resp.json():
        print(f"\nID: {seg['id']}\nQuartiere: {seg['quartiere']}\nCategoria: {seg['categoria']}\nDescrizione: {seg['descrizione']}\nStato: {seg['stato']}\nData/Ora: {seg['data_ora']}")

def main():
    """
    Author: Noemi Baruffolo
    date: 5/05/2025
    es. preparazioneVerApi 2
    text: client Web API segnalazioni (vedi testo su Classroom)
    """
    while True:
        print("\n--- Menu ---")
        print("1. Aggiungi un nuovo quartiere")
        print("2. Lista quartieri")
        print("3. Inserisci nuova segnalazione")
        print("4. Aggiorna stato segnalazione")
        print("5. Filtra segnalazioni")
        print("6. Esci")
        scelta = input("Scelta: ")
        if scelta == "1":
            aggiungi_quartiere()
        elif scelta == "2":
            lista_quartieri()
        elif scelta == "3":
            inserisci_segnalazione()
        elif scelta == "4":
            aggiorna_stato()
        elif scelta == "5":
            filtra_segnalazioni()
        elif scelta == "6":
            break
        else:
            print("Scelta non valida")

if __name__ == "__main__":
    main()
