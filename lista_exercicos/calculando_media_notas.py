notas = []
qntdNotas = int(input("Insira quantas notas irá digitar para o aluno: "))

while qntdNotas > 0:
    nota = int(input("Nota: "))
    notas.append(nota)
    qntdNotas -= 1

media = sum(notas) / len(notas)

print(f"Média: {media}")