def digito_unico(x):
  if(x<10):
    return x
  else:
    return digito_unico(x//10) + x%10

def multiplica_str(s,p):
    return s * p

print("Digite 1 para calcular a soma dos algarismos de um numero.")
print("Digite 2 para multiplicar uma string.")
qual = int(input())

if(qual==1):
    x = int(input("Digite um numero:"))
    print(digito_unico(x))
elif(qual==2):
    s = input("Digite a string: ")
    p = int(input("Digite o multiplicador: "))
    print(multiplica_str(s,p))
else:
    print("Opcao invalida.")