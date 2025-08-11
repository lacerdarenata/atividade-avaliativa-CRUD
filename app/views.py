from app import app
from flask import render_template, request, redirect, url_for
from app.models.aluno import AlunoModel
from app.service.aluno_service import AlunoService
from app.models.curso import CursoModel
from app.service.curso_service import CursoService

aluno_service = AlunoService()
curso_service = CursoService()

@app.route('/')
def index():
    return redirect(url_for('listar_cursos'))

@app.route('/cursos')
def listar_cursos():
    cursos = curso_service.get_all_cursos()
    return render_template('cursos/lista_cursos.html', cursos=cursos)


@app.route('/cursos/novo', methods=['GET', 'POST'])
def criar_curso():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        carga_horaria = request.form['carga_horaria']
        curso_service.create_curso(
            CursoModel(
                id=None, nome=nome, descricao=descricao, carga_horaria=carga_horaria
            )
        )
        return redirect(url_for('listar_cursos'))
    return render_template('cursos/form_cursos.html')


@app.route('/cursos/editar/<int:id>', methods=['GET', 'POST'])
def editar_curso(id):
    curso = curso_service.get_curso_by_id(id)
    if request.method == 'POST':
        curso_service.update_curso(
            CursoModel(
                id,
                request.form['nome'],
                request.form['descricao'],
                request.form['carga_horaria']
            )
        )
        return redirect(url_for('listar_cursos'))
    return render_template('cursos/form_cursos.html', curso=curso)

@app.route('/cursos/excluir/<int:id>')
def excluir_curso(id):
    curso_service.delete_curso(id)
    return redirect(url_for('listar_cursos'))

from app import app
from flask import render_template, request, redirect, url_for
from app.models.aluno import AlunoModel
from app.service.aluno_service import AlunoService
from app.models.curso import CursoModel
from app.service.curso_service import CursoService

aluno_service = AlunoService()
curso_service = CursoService()

# ===== ALUNOS =====
@app.route('/alunos')
def listar_alunos():
    alunos = aluno_service.get_all_alunos()
    return render_template('alunos/lista_alunos.html', alunos=alunos)

@app.route('/alunos/novo', methods=['GET', 'POST'])
def criar_aluno():
    cursos = curso_service.get_all_cursos()  # Para preencher o select
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        curso_id = request.form['curso_id']
        aluno_service.create_aluno(
            AlunoModel(
                id=None,
                nome=nome,
                email=email,
                curso_id=curso_id
            )
        )
        return redirect(url_for('listar_alunos'))
    return render_template('alunos/form_alunos.html', cursos=cursos)

@app.route('/alunos/editar/<int:id>', methods=['GET', 'POST'])
def editar_aluno(id):
    aluno = aluno_service.get_aluno_by_id(id)
    cursos = curso_service.get_all_cursos()  # Para preencher o select
    if request.method == 'POST':
        aluno_service.update_aluno(
            AlunoModel(
                id=id,
                nome=request.form['nome'],
                email=request.form['email'],
                curso_id=request.form['curso_id']
            )
        )
        return redirect(url_for('listar_alunos'))
    return render_template('alunos/form_alunos.html', aluno=aluno, cursos=cursos)

@app.route('/alunos/excluir/<int:id>')
def excluir_aluno(id):
    aluno_service.delete_aluno(id)
    return redirect(url_for('listar_alunos'))

