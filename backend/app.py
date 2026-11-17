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