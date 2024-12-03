import pytest
from aluno import Aluno
from curso import Curso
from professor import Professor

@pytest.fixture
def aluno1():
    return Aluno(1, "João Silva", 21)

@pytest.fixture
def aluno2():
    return Aluno(2, "Maria Oliveira", 22)

@pytest.fixture
def curso():
    return Curso(1, "Programação Orientada a Objetos", "Curso de POO com Python")

@pytest.fixture
def professor():
    return Professor(1, "Dr. Carlos Alberto", "Programação")
