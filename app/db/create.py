from app.db.__init_ import get_db_connection

def add_agendamento(titulo, data, horario, descricao, participantes, emails, link, notas):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO agenda (titulo, data, horario, descricao, participantes, emails, link, notas)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (titulo, data, horario, descricao, participantes, emails, link, notas))
    conn.commit()
    conn.close()
