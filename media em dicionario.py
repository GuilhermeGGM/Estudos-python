aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input('Digite a média do aluno: '))
if aluno['media'] < 6 and aluno['media'] > 3.2:
    aluno['status'] = 'Aprovado com recuperação'
elif aluno['media'] < 3.2:
    aluno['status'] ='Reprovado'
elif aluno['media'] >= 6:
    aluno['status'] = 'Aprovado'
print('-='*30)
print(aluno)
print(f'O nome do aluno é {aluno["nome"]}')
print(f'a média do aluno é de {aluno["media"]}, então ele está {aluno["status"]}')
