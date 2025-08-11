from app.repository.curso_repository import CursoRepository
from app.models.curso import CursoModel
from app.repository.aluno_repository import AlunoRepository

class CursoService:
    def __init__(self):
        self.curso_repository = CursoRepository()
        self.aluno_repository = AlunoRepository()

    def get_all_cursos(self):
        return self.curso_repository.get_all_cursos()
    
    def get_curso_by_id(self, curso_id):
        if curso_id is None:
            raise ValueError("O ID não pode ser None")
        return self.curso_repository.get_curso_by_id(curso_id)
    
    def create_curso(self, curso: CursoModel):
        if curso.get_id() is not None:
            raise ValueError("Não é permitido criar um curso com o ID já definido.")
        if not curso.get_nome() or not curso.get_descricao():
            raise ValueError("O nome e a descrição do curso são obrigatórios.")
        if curso.get_nome().isdigit():
            raise ValueError("O nome do curso não pode conter apenas números.")
        if curso.get_descricao().isdigit():
            raise ValueError("A descrição da categoria não pode conter apenas números.")
        if len(curso.get_descricao()) < 10:
            raise ValueError("A descrição do curso deve conter mais de 10 caracteres.")
        self.curso_repository.create_curso(curso)
        
    def update_curso(self, curso: CursoModel):
        if curso.get_id() is not None:
            raise ValueError("Não é permitido criar um curso com o ID já definido.")
        if not curso.get_nome() or not curso.get_descricao():
            raise ValueError("O nome e a descrição do curso são obrigatórios.")
        if curso.get_nome().isdigit():
            raise ValueError("O nome do curso não pode conter apenas números.")
        if curso.get_descricao().isdigit():
            raise ValueError("A descrição da categoria não pode conter apenas números.")
        if len(curso.get_descricao()) < 10:
            raise ValueError("A descrição do curso deve conter mais de 10 caracteres.")
        self.curso_repository.update_curso(curso)

    def delete_curso(self, curso_id):
        if curso_id is None:
            raise ValueError("O ID do curso não pode ser None")
        alunos = self.aluno_repository.get_all_alunos()
        for aluno in alunos:
            if aluno.get_curso_id() == curso_id:
                raise ValueError("Não é permitido excluir um curso com alunos matriculados.")
        self.curso_repository.delete_curso(curso_id)