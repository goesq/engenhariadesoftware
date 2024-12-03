import unittest
from curso import Curso
from aluno import Aluno

class TestCurso(unittest.TestCase):
    def test_adicionar_remover_aluno(self):
        curso = Curso(1, "Teste Curso", "Descrição Teste")
        aluno = Aluno(1, "Teste Aluno", 20)
        
        curso.adicionar_aluno(aluno)
        self.assertIn(aluno, curso._Curso__alunos)

        curso.remover_aluno(aluno)
        self.assertNotIn(aluno, curso._Curso__alunos)

if __name__ == "__main__":
    unittest.main()


import pytest

def test_curso_adicionar_remover_aluno(aluno1, aluno2, curso):
    # Adicionar alunos ao curso
    curso.adicionar_aluno(aluno1)
    curso.adicionar_aluno(aluno2)
    assert aluno1 in curso._Curso__alunos
    assert aluno2 in curso._Curso__alunos

    # Remover aluno do curso
    curso.remover_aluno(aluno1)
    assert aluno1 not in curso._Curso__alunos

def test_curso_dados(curso):
    assert curso._Curso__id == 1
    assert curso._Curso__nome == "Programação Orientada a Objetos"
    assert curso._Curso__descricao == "Curso de POO com Python"
