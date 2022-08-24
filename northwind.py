# 1. Neste tópico, estabelecemos uma conexão com o banco de dados.
 

import mysql.connector
mydb = mysql.connector.connect(
    host = "relational.fit.cvut.cz",
    user = "guest",
    password = "relational",
    database = "northwind"
)


# 2. Neste tópico, apresentamos ao usuário suas opções de tabela que podem ser escolhidas.
 
print("Hello World!")
print(" ")
print("Essa aplicação permite que você faça consultas ao Banco de Dados Northwind de uma maneira mais prática e interativa. Primeiramente, escolha o número correspondente a tabela que deseja acessar.")
print(" ")
print("1 - Orders")
print("2 - Costumers")
print("3 - Employees")
print("4 - Products")
print("5 - Shippers")
print("6 - Suppliers")
print(" ")


# 3. Este tópico trabalha na localização dos nomes, das tabelas e das colunas.

while True:
    tabela = input("- Insira o número referente a tabela que deseja acessar: ")
    if (tabela == '1'):
        tabela = "Orders"
        coluna = "shipName"
        break
    elif (tabela == '2'):
        tabela = "Customers"
        coluna = "ContactName"
        break
    elif (tabela == '3'):
        tabela = "Employees"
        coluna = "FirstName"
        break
    elif (tabela == '4'):
        tabela = "Products"
        coluna = "ProductName"
        break
    elif (tabela == '5'):
        tabela = "Shippers"
        coluna = "CompanyName"
        break
    elif (tabela == '6'):
        tabela = "Suppliers"
        coluna = "ContactName"
        break
    else:
        print("Opção inválida. Informe outro número: ")

# 4. Esse tópico é responsável por realizar ou não a verificação de nomes e pela inserção dos mesmos.


nome = input("Deseja pesquisar por algum nome específico? (Sim/Não): ")

if (nome == 'Sim'):
    op = True
    nome = input(f"Informe o nome que deseja pesquisar ({coluna}): ")

else:
    op = False


# 5. Esse tópico é responsável pela criação do cursor.


mycursor = mydb.cursor()


# 6. Esse tópico é responsável por realizar a pesquisa no banco de dados.


if (op):
    mycursor.execute(f"SELECT * FROM {tabela} where {coluna} like '%{nome}%'")

else:
    mycursor.execute(f"SELECT * FROM {tabela}")


# 7. Esse tópico é responsável por armazenar os resultados encontrados em uma única variável.


myresult = mycursor.fetchall()


# 8. Esse tópico retorna os resultados encontrados.


for registro in myresult:
    print(registro)


# Finish!