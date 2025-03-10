aluno = {}
aluno['nome'] = input('Nome do aluno: ')
aluno['media'] = float(input(f"Média do aluno {aluno['nome']}: "))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
# print(aluno)
print('-=' * 20)
# print(f'{"Nome do aluno "}{aluno["nome"]}'.center(30))
# print(f"    - Nome do aluno: {aluno['nome']}")
# print(f"    - Média do aluno: {aluno['media']}")
# print(f"    - Situação do aluno: {aluno['situacao']}")
for k, v in aluno.items():
    print(f"   - {k} é igual a {v}")

