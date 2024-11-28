import sqlite3

# Inicialização do banco de dados e preparação da estrutura necessária
def init_db():
    conn = sqlite3.connect('agenda.db')
    conn.execute("""
    CREATE TABLE IF NOT EXISTS agenda (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        data DATE NOT NULL,
        horario TIME NOT NULL,
        descricao TEXT,
        participantes TEXT,
        emails TEXT,
        link TEXT,
        notas TEXT
    )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
