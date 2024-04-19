inteiro: int = 10

real: float = 10.0

print(inteiro + real)

print("\n")

def funcao_soma(a: int, b: int) -> int:
    print(a + b)  

print("\n")

#lista é feita uma seguencia
lista_1 = [1, 2, 3, 4, 5]
                                      #diferença da tupla da lista:
lista_2 = list(range(1,6))            #lista é mutavel tupla nao é,
                                      #lista é definida por colchetes e tupla por parenteses,
print(lista_1, lista_2)               #a lista é mais lenta,
                                      # lista é mais flexivel,
#tupla                                #lista é mais utilizada,
tupla = (1, 2, 3, 4, 5)               #tupla é mais segura que lista
print(tupla)

print("\n")

#Dicionario
dicionario = {'nome': 'Roberto', 'idade': 20}
print(dicionario)

print("\n")

dicionario_2 = {"lista_animais": ["cachorro", "gato", "papagaio"], "lista_carros":["fusca", "gol", "prisma"]}
print(dicionario_2)


print("\n")
for carro in dicionario_2["lista_carros"]:
    print(carro)

print("\n")

valor_a: int = 10
valor_b: int = 20                                   #operadores logicos
                                                    # >= maior ou igual
if valor_a > valor_b:                               # <= menor ou igual
    print("valor_a é maior que valor_b")            # ! ou != diferente
elif valor_a < valor_b:                             # and, &&, & e
  print("valor_a é menor a volor_b")                # or, ||, |, ou
else:                                               # == igual 
    print("valor_a é igual a valor_b")             

print("\n")

teste = 10 < 9

print(f"O teste é: {teste}")

if not (teste and True):                          # not serve para inverter uma porta
    print("O teste é verdadeiro")
else:
    print("O teste é falso")

print("\n")
print("Laços")
print("\n")

# laços
# for usando uma estrutura convencional 
for i in range(10):
    print(i)

print("\n\n")

# usando uma estrutura de list comprehension
[print(i) for i in range(10)]

print("\n")

# usando estrutura de list compreheision com if
[print(i) for i in range(20) if i % 2 == 0]

print("\n")

# usando uma esrtrutura de list comprehesion com if
[print(i) for i in range(20) if i % 2 != 0]