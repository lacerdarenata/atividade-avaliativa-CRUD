# Sistema de Gerenciamento de Alunos e Cursos

## 📌 Descrição
Este é um sistema web desenvolvido em **Python (Flask)** e **SQLite** para gerenciar **alunos** e **cursos**.  
O sistema permite **cadastrar, listar, editar e excluir** cursos e alunos, mantendo um relacionamento **1:N** (um curso pode ter vários alunos).

---

## 🗂 Estrutura das Entidades

### **Curso**
- `id` → Identificador único (PK)
- `nome` → Nome do curso
- `descricao` → Descrição do curso
- `carga_horaria` → Carga horária em horas

### **Aluno**
- `id` → Identificador único (PK)
- `nome` → Nome do aluno
- `email` → E-mail do aluno (único)
- `curso_id` → ID do curso (FK)

---

## 🔗 Relacionamento
- **1 Curso** → **N Alunos**  
- Um curso pode ter vários alunos matriculados.  
- Um aluno pertence a apenas um curso.

### Executar o projeto:

1. Criar ambiente virtual
    ```
    python -m venv venv
    ```
2. Ativar ambiente virtual
    ```
    venv/Scripts/activate
    ```
   2.1. Atualizar o pip
   ```
    pip install --upgrade pip
    ```
3. Instalar o Flask
    ```
    pip install Flask
    ```
4. Executar o script `run.py`
```
python run.py
```
