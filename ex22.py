nome = str(input("Digite seu nome: ")).strip()
print(nome.upper())
print(nome.lower())
dividido = nome.replace(' ', '')
print(len(dividido))
n1 = nome.split()
print(len(n1[0]))
# outra opção parar não contabilizar os espaços entre os nomes
print(len(nome) - nome.count(' '))
# outra opão para ver quantas letras tem o primeiro nome
print(nome.find(' '))