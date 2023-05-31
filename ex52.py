n = int(input("Digite um número: "))
mult = 0
for c in range(2,n):
    if n % c == 0:
        mult = mult + 1
if mult == 0:
    print('Esse número é primo')
else:
    print('Esse número não é primo')