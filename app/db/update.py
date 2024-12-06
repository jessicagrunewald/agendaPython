from app.db.__init_ import get_db_connection

def update_agendamento(agendamento_id, titulo, data, horario, descricao, participantes, emails, link, notas):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE agenda
        SET titulo = ?, data = ?, horario = ?, descricao = ?, participantes = ?, emails = ?, link = ?, notas = ?
        WHERE id = ?
    """, (titulo, data, horario, descricao, participantes, emails, link, notas, agendamento_id))
    conn.commit()
    conn.close()
