import sqlite3

def create_database():
    # Crée une connexion à la base de données SQLite
    conn = sqlite3.connect('products.db')  # Ce fichier est celui qui sera créé
    cursor = conn.cursor()

    # Crée la table Products si elle n'existe pas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Insère des produits d'exemple
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')

    # Commit (valide les changements) et ferme la connexion
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
