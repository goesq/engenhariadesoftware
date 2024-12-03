from aluno import Aluno
from curso import Curso
from professor import Professor

# Criar objetos do sistema
aluno1 = Aluno(1, "João Silva", 21)
aluno2 = Aluno(2, "Maria Oliveira", 22)

curso1 = Curso(1, "Programação Orientada a Objetos", "Curso de POO com Python")

professor1 = Professor(1, "Dr. Carlos Alberto", "Programação")

# Vincular Alunos e Curso
aluno1.matricular(curso1)
aluno2.matricular(curso1)

# Professor ministra o curso
professor1.ministrar_curso(curso1)

# Exibir informações
print(aluno1)
print(aluno2)
print(curso1)
print(professor1)
