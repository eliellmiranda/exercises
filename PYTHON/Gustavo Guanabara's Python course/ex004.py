algo = input("Digite alguma coisa: ")

print("O tipo primitivo desse valor é:", (type(algo)))

print("É alfanumérico?", algo.isalnum())
print("É alfabético?", algo.isalpha())
print("É numérico?", algo.isnumeric())
print("Só tem espaços?", algo.isspace())  

