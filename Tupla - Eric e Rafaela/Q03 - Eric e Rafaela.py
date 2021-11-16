"""
@author: Rafaela e Eric
"""

"Crie um programa tenha um tupla única com as fórmulas fisicas da cinemática, montando uma lista com as fórmulas em ordem de ocorrência, de forma tabular"

formulas = ( 'Velocidade média', '(Vm = Δs/Δt)',
           'Aceleração', '(a = Δv/Δt)',
           'Função horária do deslocamento', '(S = So + VΔt)',
           'Função horária da velocidade', '(V = Vo + at)',
           'Função horária da posição', '(S = So + vot + (at^2)/2)',
           'Equação de Torricelli', '(V^2 = Vo^2 + 2aΔs)',
           'Equação de Torricelli (lançamento vertical)', '(V^2 = Vo^2+2gh)',)

print('=' * 80)
print(f'{"FÓRMULAS DA CINEMÁTICA":^75}')
print('=' * 80)
for i in range(0, len(formulas)):
    if i % 2 == 0:
        print(f'{(formulas[i]):.<50}', end='')
    else:
        print(f'{formulas[i]:.>10}')
print('=' * 80)