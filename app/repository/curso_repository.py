from app.database.connection import get_db
from app.models.curso import CursoModel

class CursoRepository:

    def get_all_cursos(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM curso")
        rows = cursor.fetchall()
        return [CursoModel(id=row[0], nome=row[1], descricao=row[2], carga_horaria=row[3]) for row in rows]
    
    def get_curso_by_id(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM curso WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row:
            return CursoModel(id=row[0], nome=row[1], descricao=row[2], carga_horaria=row[3])
        return None
    
    def create_curso(self, curso):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(""" INSERT INTO curso (nome, descricao, carga_horaria)
                       VALUES (?, ?, ?)""", 
                       (curso.get_nome(), curso.get_descricao(), curso.get_carga_horaria()))
        connection.commit()

    def update_curso(self, curso):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(""" UPDATE curso
                       SET nome = ?, descricao = ?, carga_horaria = ?
                       WHERE id = ?""",
                       (curso.get_nome(), curso.get_descricao(), curso.get_carga_horaria(), curso.get_id()))
        connection.commit()

    def delete_curso(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM curso WHERE id = ?", (id,))
        connection.commit()



    