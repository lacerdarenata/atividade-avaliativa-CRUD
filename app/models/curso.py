class CursoModel:
    def __init__(self, id, nome, descricao, carga_horaria):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__carga_horaria = carga_horaria

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_descricao(self):
        return self.__descricao
    def get_carga_horaria(self):
        return self.__carga_horaria
    
    def set_nome(self, nome):
        self.__nome = nome
    def set_descricao(self, descricao):
        self.__descricao = descricao
    def set_carga_horaria(self, carga_horaria):
        self.__carga_horaria = carga_horaria
    