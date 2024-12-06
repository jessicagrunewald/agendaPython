from app.db.__init_ import get_db_connection

def get_all_agendamentos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM agenda ORDER BY data, horario")
    agendamentos = cursor.fetchall()
    conn.close()
    return agendamentos
