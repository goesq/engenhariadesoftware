class Aluno:
    def __init__(self, id, nome, idade):
        self.__id = id
        self.__nome = nome
        self.__idade = idade
        self.__cursos = []

    def matricular(self, curso):
        if curso not in self.__cursos:
            self.__cursos.append(curso)
            curso.adicionar_aluno(self)

    def cancelar_matricula(self, curso):
        if curso in self.__cursos:
            self.__cursos.remove(curso)
            curso.remover_aluno(self)

    def __str__(self):
        return f"Aluno(id={self.__id}, nome={self.__nome}, idade={self.__idade})"
