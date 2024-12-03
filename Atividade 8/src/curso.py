class Curso:
    def __init__(self, id, nome, descricao):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__alunos = []

    def adicionar_aluno(self, aluno):
        if aluno not in self.__alunos:
            self.__alunos.append(aluno)

    def remover_aluno(self, aluno):
        if aluno in self.__alunos:
            self.__alunos.remove(aluno)

    def __str__(self):
        return f"Curso(id={self.__id}, nome={self.__nome}, descricao={self.__descricao})"
