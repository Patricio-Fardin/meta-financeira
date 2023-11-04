def calcular_tempo_para_meta(meta, economia_mensal):
    if economia_mensal <= 0:
        return 'A economia mensal deve ser maior que zero.'

    meses_necessarios = meta / economia_mensal
    return meses_necessarios

# Solicitar entrada do usuário
meta = float(input('Informe o valor da meta financeira: R$'))
economia_mensal = float(input('Informe a economia mensal: R$'))

tempo_necessario = calcular_tempo_para_meta(meta, economia_mensal)

if tempo_necessario > 1:
    print(f'Você levará aproximadamente {int(tempo_necessario)} meses para atingir a meta financeira de R${meta}.')
elif tempo_necessario == 1:
    print('Você levará 1 mês para atingir a meta financeira de R${meta}.')
else:
    print('Você já atingiu sua meta financeira! Não é necessário economizar mais.')
