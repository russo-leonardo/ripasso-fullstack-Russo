CREATE DATABASE IF NOT EXISTS negozio;
USE negozio;

CREATE TABLE prodotti (
  id     INT AUTO_INCREMENT PRIMARY KEY,
  nome   VARCHAR(100) NOT NULL,
  prezzo DECIMAL(8,2) NOT NULL
);
INSERT INTO prodotti (nome, prezzo) VALUES
 ('Mouse', 19.90), ('Tastiera', 45.00),
 ('Monitor 24 pollici', 149.00), ('Cuffie', 39.50);

CREATE TABLE ordini (
  id        INT AUTO_INCREMENT PRIMARY KEY,
  cliente   VARCHAR(100) NOT NULL,
  totale    DECIMAL(10,2) NOT NULL,
  creato_il TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);CREATE DATABASE IF NOT EXISTS negozio;
USE negozio;

CREATE TABLE prodotti (
  id     INT AUTO_INCREMENT PRIMARY KEY,
  nome   VARCHAR(100) NOT NULL,
  prezzo DECIMAL(8,2) NOT NULL
);
INSERT INTO prodotti (nome, prezzo) VALUES
 ('Mouse', 19.90), ('Tastiera', 45.00),
 ('Monitor 24 pollici', 149.00), ('Cuffie', 39.50);

CREATE TABLE ordini (
  id        INT AUTO_INCREMENT PRIMARY KEY,
  cliente   VARCHAR(100) NOT NULL,
  totale    DECIMAL(10,2) NOT NULL,
  creato_il TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- un ordine con 3 prodotti = 3 righe qui
CREATE TABLE righe_ordine (
  id          INT AUTO_INCREMENT PRIMARY KEY,
  ordine_id   INT NOT NULL,
  prodotto_id INT NOT NULL,
  FOREIGN KEY (ordine_id)   REFERENCES ordini(id),
  FOREIGN KEY (prodotto_id) REFERENCES prodotti(id)
);

-- un ordine con 3 prodotti = 3 righe qui
CREATE TABLE righe_ordine (
  id          INT AUTO_INCREMENT PRIMARY KEY,
  ordine_id   INT NOT NULL,
  prodotto_id INT NOT NULL,
  FOREIGN KEY (ordine_id)   REFERENCES ordini(id),
  FOREIGN KEY (prodotto_id) REFERENCES prodotti(id)
);
