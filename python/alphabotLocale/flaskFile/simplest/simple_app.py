from flask import Flask

app = Flask(__name__) #flask associa url a codici pyhton
#@ decoratore, costrutto linguaggio python
@app.route('/') #url abbreviato che richiama una funzione
def index():
    return 'Ciao!'

@app.route('/pagina/')
def index2():
    return 'pagina!'

if __name__ == '__main__':
    app.run(debug=True, host='localhost') #puoi modificare il codice, così vengono eseguite subito appena lo salvi, invece di ricaricarlo