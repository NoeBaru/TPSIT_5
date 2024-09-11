import random

def ha_compleanni_uguali(studenti):
    return len(studenti) != len(set(studenti))

def stima_probabilita_compleanno_uguale(num_studenti, num_simulazioni):
    conta_corrispondenze = 0
    
    for _ in range(num_simulazioni):
        studenti = [random.randint(1, 365) for _ in range(num_studenti)]
        if ha_compleanni_uguali(studenti):
            conta_corrispondenze += 1
    
    return conta_corrispondenze / num_simulazioni

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 10.8
    text:
    Questo è un esercizio sul cosiddetto “Paradosso del compleanno”; potete approfondirlo leggendo
    http://it.wikipedia.org/wiki/Paradosso_del_compleanno.
    Se in una classe ci sono 23 studenti, quante probabilità ci sono che due di loro compiano gli anni lo stesso giorno? Potete stimare
    questa probabilità generando alcuni campioni a caso di 23 date e controllando le corrispondenze. Suggerimento: per generare date in
    modo casuale usate la funzione randint nel modulo random.
    Potete scaricare la mia soluzione da http://thinkpython2.com/code/birthday.py.
    """
    num_studenti = 23
    num_simulazioni = 10000
    probabilita = stima_probabilita_compleanno_uguale(num_studenti, num_simulazioni)
    print(f"La probabilità stimata che due studenti su {num_studenti} abbiano lo stesso compleanno è circa: {probabilita:.2%}")

if __name__ == '__main__':
    main()
