Rm = []
Nome = []
Curso = []

for i in range(5):

    Rm.append(int(input("Digite o RM do Aluno: ")))
    Nome.append(input("Digite o Nome do Aluno: "))
    Curso.append(input("Digite o Curso em que está matrículado: "))
    print()

    while Rm == "" or Nome == "":

        Rm = input("Digite o RM do Aluno: ")
        Nome = input("Digite o Nome do Aluno: ")
        print()

    if Curso == "":
        Curso = "Não Informado" 
    
for i in range(5):

    print("RM: ", Rm[i])
    print("Nome: ", Nome[i])
    print("Curso: ", Curso[i])
    print()

print("Fim do CheckPoint 2")

#RM : 97210# 
#Nome : Vinicius Cruzeiro Barbosa#

#Bom Feriado Professsor#
