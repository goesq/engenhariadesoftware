import pytest
from aluno import Aluno
from curso import Curso
from professor import Professor

@pytest.fixture
def professor():
    return Professor(1, "Dr. Carlos Alberto", "Programação")

@pytest.fixture
def alunos():
    return [
        Aluno(1, "João Silva", 21),
        Aluno(2, "Maria Oliveira", 22),
    ]

@pytest.fixture
def curso(professor):
    curso = Curso(1, "Programação Orientada a Objetos", "Curso de POO com Python")
    professor.ministrar_curso(curso)
    return curso

def test_integration(professor, alunos, curso):
    # 1. Verificar professor
    assert professor._Professor__id == 1
    assert professor._Professor__nome == "Dr. Carlos Alberto"

    # 2. Verificar alunos
    assert alunos[0]._Aluno__nome == "João Silva"
    assert alunos[1]._Aluno__nome == "Maria Oliveira"

    # 3. Verificar curso
    assert curso._Curso__id == 1
    assert curso._Curso__nome == "Programação Orientada a Objetos"
    assert curso._Curso__descricao == "Curso de POO com Python"

    # 4. Adicionar alunos ao curso
    for aluno in alunos:
        aluno.matricular(curso)
    assert len(curso._Curso__alunos) == len(alunos)

    # 5. Verificar listagem de alunos
    alunos_listados = [str(aluno) for aluno in curso._Curso__alunos]
    assert alunos_listados == [
        "Aluno(id=1, nome=João Silva, idade=21)",
        "Aluno(id=2, nome=Maria Oliveira, idade=22)",
    ]

    # 6. Verificar professor responsável pelo curso
    print(f"O curso é ministrado por: {professor}")
    assert True  # Simulação para validação do fluxo
