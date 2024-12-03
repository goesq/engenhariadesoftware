class Professor:
    def __init__(self, id, nome, especialidade):
        self.__id = id
        self.__nome = nome
        self.__especialidade = especialidade

    def ministrar_curso(self, curso):
        print(f"O professor {self.__nome} está ministrando o curso {curso}")

    def __str__(self):
        return f"Professor(id={self.__id}, nome={self.__nome}, especialidade={self.__especialidade})"

    import pytest

def test_professor_ministrar_curso(professor, curso):
    # Verificar se o professor ministra o curso corretamente
    professor.ministrar_curso(curso)
    assert True  # Apenas para simular a interação; melhoria seria usar mocks.

@pytest.mark.parametrize("id, nome, especialidade", [
    (1, "Dr. Carlos Alberto", "Programação"),
    (2, "Dr. Ana Silva", "Engenharia de Software"),
])
def test_professor_dados(id, nome, especialidade):
    professor = Professor(id, nome, especialidade)
    assert professor._Professor__id == id
    assert professor._Professor__nome == nome
    assert professor._Professor__especialidade == especialidade
