class alunos:
    def __init__(self,matricula, sexo, nome, idade):
        self.matricula = matricula
        self.sexo = sexo
        self.nome = nome
        self.idade = idade

if __name__ == "__main__":
    alunos = alunos("123", "masculino", "joão", "17")
    print(alunos.matricula, alunos.sexo, alunos.nome, alunos.idade)
