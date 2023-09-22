with open("Alunos.txt", "r") as notas_alunos:
    with open("Aprovados.txt", "w") as alunos_aprovados, open("Reprovados.txt", "w") as alunos_reprovados:
        for linha in notas_alunos:
            partes = linha.strip().split(",")  
            if len(partes) == 2:
                aluno = partes[0].strip()
                nota = float(partes[1].strip())

                if nota >= 7.5:
                    alunos_aprovados.write(f"{aluno}: {nota}\n")
                else:
                    alunos_reprovados.write(f"{aluno}: {nota}\n")

alunos_aprovados.close()
alunos_reprovados.close()