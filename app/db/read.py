from app.db.__init_ import get_db_connection

def get_all_agendamentos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM agenda ORDER BY data, horario")
    agendamentos = cursor.fetchall()
    conn.close()
    return agendamentos

# Ler um agendamento específico
def get_agendamento_by_id(agendamento_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM agenda WHERE id = ?", (agendamento_id,))
    agendamento = cursor.fetchone()
    conn.close()
    return agendamento
