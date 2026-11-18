from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

def get_conn():
    # il MySQL nel container Docker (sezione 1)
    return mysql.connector.connect(
        host="127.0.0.1", user="root",
        password="root", database="negozio")

def riga_to_dict(r):
    return {"id": r[0], "nome": r[1],
            "prezzo": float(r[2]),
            "prezzo_ivato": float(r[3])}

@app.get("/api/prodotti")
def lista_prodotti():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, nome, prezzo, "
                "prezzo * 1.22 AS prezzo_ivato "
                "FROM prodotti")
    righe = cur.fetchall()
    cur.close(); conn.close()
    prodotti = [riga_to_dict(r) for r in righe]
    return jsonify(prodotti), 200
@app.get("/api/prodotti/<int:id>")
def dettaglio(id):
    conn = get_conn(); cur = conn.cursor()
    cur.execute("SELECT id, nome, prezzo, "
                "prezzo * 1.22 AS prezzo_ivato "
                "FROM prodotti WHERE id = %s", (id,))
    r = cur.fetchone()
    cur.close(); conn.close()
    if r is None:
        return jsonify({"errore": "non trovato"}), 404
    return jsonify(riga_to_dict(r)), 200

# nuovo ordine: i dati arrivano nel BODY
# {"cliente": "Rossi", "totale": 72.47, "prodotti": [1, 4]}
@app.post("/api/ordini")
def crea_ordine():
    dati = request.get_json()        # JSON → dizionario
    conn = get_conn(); cur = conn.cursor()
    cur.execute("INSERT INTO ordini (cliente, totale) "
                "VALUES (%s, %s)",
                (dati["cliente"], dati["totale"]))
    nuovo_id = cur.lastrowid         # id appena creato
    for pid in dati["prodotti"]:      # una riga per prodotto
        cur.execute("INSERT INTO righe_ordine "
                    "(ordine_id, prodotto_id) VALUES (%s, %s)",
                    (nuovo_id, pid))
    conn.commit()                    # salva tutto insieme
    cur.close(); conn.close()
    return jsonify({"id": nuovo_id}), 201