import sqlite3

def check_table():
    # Verifica se a tabela 'agenda' existe no banco de dados.
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()

    # Verificar as tabelas existentes
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='agenda'")
    tabela = cursor.fetchone()

    if tabela:
        print("A tabela 'agenda' existe no banco de dados.")
    else:
        print("A tabela 'agenda' não foi encontrada no banco de dados.")

    conn.close()

if __name__ == "__main__":
    check_table()