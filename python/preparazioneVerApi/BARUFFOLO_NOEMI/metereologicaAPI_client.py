import requests
from datetime import datetime

BASE_URL = "http://127.0.0.1:5000"

# /grandezza/<string:nome>
def get_grandezza(nome):
    url = f"{BASE_URL}/grandezza/{nome}"
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    else:
        print("Errore nella get grandezza")

# /stazione/<string:nome>
def get_stazione(nome):
    url = f"{BASE_URL}/stazione/{nome}"
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    else:
        print("Errore nella get stazione")

# /misurazione
def post_misura(id_stazione, id_grandezza, data_ora, valore):
    url = f"{BASE_URL}/misurazione"
    payload = {
        "id_stazione": id_stazione,
        "id_grandezza": id_grandezza,
        "data_ora": data_ora,
        "valore": valore
    }

    resp = requests.post(url, json=payload)
    if resp.status_code == 201:
        print("Misurazione inserita con successo")
    else:
        print("Errore nella post della misurazione")

# BONUS – /statistiche/<int:id_stazione>/<int:id_grandezza>
def get_statistiche(id_stazione, id_grandezza):
    url = f"{BASE_URL}/statistiche/{id_stazione}/{id_grandezza}"
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    else:
        print("Errore nel recupero delle statistiche")

def main():
    """
    Author: Noemi Baruffolo
    date: 02/05/2025
    es. preparazioneVerApi
    text: client Web API metereologica (vedi testo su Classroom)
    """

    while True:
        print("\n--- Menu ---")
        print("1. Inserisci una nuova misurazione")
        print("2. Ottieni statistiche (BONUS)")
        print("3. Esci")
        scelta = input("Scelta: ")

        if scelta == "1": #inserimento misura
            grandezza_nome = input("Nome grandezza (es. temperatura): ").strip()
            stazione_nome = input("Nome stazione (es. cuneo1): ").strip()
            valore = float(input("Valore misurazione: "))
            data_ora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            grandezza = get_grandezza(grandezza_nome)
            stazione = get_stazione(stazione_nome)

            if grandezza and stazione:
                post_misura(
                    id_stazione = stazione["id_stazione"],
                    id_grandezza = grandezza["id_misura"],
                    data_ora = data_ora,
                    valore = valore
                )

        elif scelta == "2": #statistica misure
            stazione_nome = input("Nome stazione: ").strip()
            grandezza_nome = input("Nome grandezza: ").strip()

            grandezza = get_grandezza(grandezza_nome)
            stazione = get_stazione(stazione_nome)

            if grandezza and stazione:
                stats = get_statistiche(stazione["id_stazione"], grandezza["id_misura"])
                if stats:
                    print(f"\nStatistiche per {stazione_nome} - {grandezza_nome}")
                    print(f"Media: {stats['media']}")
                    print(f"Massimo: {stats['massimo']}")
                    print(f"Minimo: {stats['minimo']}")

        elif scelta == "3": #uscire
            break
        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    main()