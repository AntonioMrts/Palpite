#exercicio 1
lista_compras = ["maçã", "banana", "leite", "pao"]

#exercicio 2 
lista_compras.append("ovos")
print(lista_compras)

#exercicio 3 
lista_compras.remove("leite")
print(lista_compras)

#exercicio 4
tarefas = ["estudar", "dormir", "acordar"]
tarefas.sort()
print(tarefas)

#exercicio 5
notas = [7.5, 8.0, 6.5, 9]
notas.sort(reverse=True)
print(notas)

#exercicio 6
contatos = ["Ana", "Carlos", "Maria"]
for i in range(len(contatos)):
    if contatos[i] == "Carlos":
        contatos[i] = "João"
print(contatos)

#exercicio 7
cores = ["azul", "vermelho", "azul", "amarelo", "azul"]
azul = 0
for i in range(len(cores)):
    azul += 1
print("A palavra 'azul' apareceu ", azul, "vezes.")