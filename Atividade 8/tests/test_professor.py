import unittest
from professor import Professor
from curso import Curso

class TestProfessor(unittest.TestCase):
    def test_ministrar_curso(self):
        professor = Professor(1, "Dr. Teste", "Teste")
        curso = Curso(1, "Teste Curso", "Descrição Teste")
        
        self.assertEqual(
            str(professor), 
            "Professor(id=1, nome=Dr. Teste, especialidade=Teste)"
        )

if __name__ == "__main__":
    unittest.main()

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

