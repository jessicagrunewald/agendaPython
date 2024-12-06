from app.db.__init_ import get_db_connection

def delete_agendamento(agendamento_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM agenda WHERE id = ?", (agendamento_id,))
    conn.commit()
    conn.close()
