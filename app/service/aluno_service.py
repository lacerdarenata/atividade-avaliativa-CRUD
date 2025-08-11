from app.models.aluno import AlunoModel
from app.repository.aluno_repository import AlunoRepository

class AlunoService:
    def __init__(self):
        self.repository = AlunoRepository()

    def get_all_alunos(self):
        return self.repository.get_all_alunos()
    
    def get_aluno_by_id(self, aluno_id):
        if aluno_id is None:
            raise ValueError("ID do aluno não pode ser None")
        return self.repository.get_aluno_by_id(aluno_id)
    
    def create_aluno(self, aluno: AlunoModel):
        if aluno.get_id() is not None:
            raise ValueError("ID do aluno deve ser None para criação")
        if not aluno.get_nome() or not aluno.get_email() or not aluno.get_curso_id():
            raise ValueError("Nome, email e curso_id são obrigatórios para criação do aluno")
        if len(aluno.get_nome()) < 3:
            raise ValueError("Nome do aluno deve ter pelo menos 3 caracteres")
        if any(char.isdigit() for char in aluno.get_nome()):
            raise ValueError("Nome do aluno não pode conter números")
        self.repository.create_aluno(aluno)


    def update_aluno(self, aluno: AlunoModel):
        if aluno.get_id() is None:
            raise ValueError("ID do aluno não pode ser None para atualização")
        if not aluno.get_nome() or not aluno.get_email() or not aluno.get_curso_id():
            raise ValueError("Nome, email e curso_id são obrigatórios para atualização do aluno")
        if len(aluno.get_nome()) < 3:
            raise ValueError("Nome do aluno deve ter pelo menos 3 caracteres")
        if any(char.isdigit() for char in aluno.get_nome()):
            raise ValueError("Nome do aluno não pode conter números")
        self.repository.update_aluno(aluno)


    def delete_aluno(self, aluno_id):
        if aluno_id is None:
            raise ValueError("O ID do aluno não pode ser None.")
        self.repository.delete_aluno(aluno_id)
