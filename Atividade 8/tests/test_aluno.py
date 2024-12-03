import unittest
from aluno import Aluno
from curso import Curso

class TestAluno(unittest.TestCase):
    def test_matricular_e_cancelar(self):
        aluno = Aluno(1, "Teste Aluno", 20)
        curso = Curso(1, "Teste Curso", "Descrição Teste")
        
        aluno.matricular(curso)
        self.assertIn(aluno, curso._Curso__alunos)

        aluno.cancelar_matricula(curso)
        self.assertNotIn(aluno, curso._Curso__alunos)

if __name__ == "__main__":
    unittest.main()

import pytest

def test_aluno_matricular_e_cancelar(aluno1, curso):
    # Matricular o aluno no curso
    aluno1.matricular(curso)
    assert aluno1 in curso._Curso__alunos

    # Cancelar matrícula
    aluno1.cancelar_matricula(curso)
    assert aluno1 not in curso._Curso__alunos

@pytest.mark.parametrize("id, nome, idade", [
    (1, "João Silva", 21),
    (2, "Maria Oliveira", 22),
])
def test_aluno_dados(id, nome, idade):
    aluno = Aluno(id, nome, idade)
    assert aluno._Aluno__id == id
    assert aluno._Aluno__nome == nome
    assert aluno._Aluno__idade == idade
