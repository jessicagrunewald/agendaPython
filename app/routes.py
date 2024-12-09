from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db.__init_ import get_db_connection
from app.db.create import add_agendamento
from app.db.delete import delete_agendamento
from app.db.update import update_agendamento

app = Blueprint('routes', __name__)

# Página inicial: lista todos os agendamentos
@app.route('/')
def index():
    conn = get_db_connection()
    agendamentos = conn.execute('SELECT * FROM agenda ORDER BY data, horario').fetchall()
    conn.close()
    return render_template('index.html', agendamentos=agendamentos)

# Rota GET para exibir o formulário de adição de agendamentos
@app.route('/create', methods=['GET'])
def show_create_form():
    return render_template('create.html')

# Rota POST para adicionar um novo agendamento
@app.route('/create', methods=['POST'])
def create():
    titulo = request.form['titulo']
    data = request.form['data']
    horario = request.form['horario']
    descricao = request.form['descricao']
    participantes = request.form['participantes']
    emails = request.form['emails']
    link = request.form['link']
    notas = request.form['notas']

    add_agendamento(titulo, data, horario, descricao, participantes, emails, link, notas)
    flash("Agendamento adicionado com sucesso!")
    return redirect(url_for('routes.index'))

# Rota função delete
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    delete_agendamento(id)
    flash("Agendamento deletado com sucesso!")
    return redirect(url_for('routes.index'))

# Rota função update
@app.route('/update/<int:id>', methods=['GET'])
def show_update_form(id):
    conn = get_db_connection()
    agendamento = conn.execute('SELECT * FROM agenda WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('update.html', agendamento=agendamento)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    titulo = request.form['titulo']
    data = request.form['data']
    horario = request.form['horario']
    descricao = request.form['descricao']
    participantes = request.form['participantes']
    emails = request.form['emails']
    link = request.form['link']
    notas = request.form['notas']

    update_agendamento(id, titulo, data, horario, descricao, participantes, emails, link, notas)
    flash("Agendamento atualizado com sucesso!")
    return redirect(url_for('routes.index'))
