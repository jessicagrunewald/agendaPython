from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db.__init_ import get_db_connection

app = Blueprint('routes', __name__)

@app.route('/')
def index():
    # Página inicial: lista todos os agendamentos
    conn = get_db_connection()
    agendamentos = conn.execute('SELECT * FROM agenda ORDER BY data, horario').fetchall()
    conn.close()
    return render_template('index.html', agendamentos=agendamentos)
