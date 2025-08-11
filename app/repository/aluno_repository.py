from app.database.connection import get_db
from app.models.aluno import AlunoModel

class AlunoRepository:
    
    def get_all_alunos(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(""" SELECT a.id, a.nome, a.email, a.curso_id, c.nome
                       FROM aluno a
                       JOIN curso c ON a.curso_id = c.id""")
        rows = cursor.fetchall()
        alunos = []
        for row in rows:
            aluno = AlunoModel(
                id=row[0],
                nome=row[1],
                email=row[2],
                curso_id=row[3]
            )
            aluno.curso_nome = row[4]
            alunos.append(aluno)
        return alunos
    
    def get_aluno_by_id(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(""" SELECT a.id, a.nome, a.email, a.curso_id, c.nome
                       FROM aluno a
                       JOIN curso c ON a.curso_id = c.id
                       WHERE a.id = ?""", (id,))
        row = cursor.fetchone()
        if row:
            aluno = AlunoModel(
                id=row[0],
                nome=row[1],
                email=row[2],
                curso_id=row[3]
            )
            aluno.curso_nome = row[4]
            return aluno
        
    def create_aluno(self, aluno):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO aluno (nome, email, curso_id)
                       VALUES (?, ?, ?)""", 
                       (aluno.get_nome(), aluno.get_email(), aluno.get_curso_id()))
        connection.commit()

    def update_aluno(self, aluno):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(""" UPDATE aluno
                       SET nome = ?, email = ?, curso_id = ?
                       WHERE id = ?""",
                       (aluno.get_nome(), aluno.get_email(), aluno.get_curso_id(), aluno.get_id()))
        connection.commit()
    
    def delete_aluno(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(""" DELETE FROM aluno WHERE id = ?""", (id,))
        connection.commit()

    def get_alunos_by_curso_id(self, curso_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM aluno WHERE curso_id = ?", (curso_id,))
        return cursor.fetchall()
    
    