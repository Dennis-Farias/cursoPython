# Cores no terminal
print('\033[1;31;40mOlá Mundo\033[m')
a = 3
b = 5
print("Os valores são \033[1;34;40m{}\033[m e \033[4;35m{}\033[m".format(a, b))
nome = 'Dennis'
print('Olá {}{}{}'.format('\033[7;40m', nome, '\033[m'))
cores = {'limpa': '\033[m',
        'vermelho': '\033[1;31m',
        'fundoverde': '\033[42m'}
print('Que nome lindo você tem {}{}{}'.format(cores['fundoverde'], nome, cores['limpa']))