class AlunoModel:
    def __init__(self, id, nome, email, curso_id):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__curso_id = curso_id

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_curso_id(self):
        return self.__curso_id
        
    def set_nome(self, nome):
        self.__nome = nome
    def set_email(self, email):
        self.__email = email
    def set_curso_id(self, curso_id):
        self.__curso_id = curso_id
        
