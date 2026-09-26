#Entrada de dados, nome e idade do usuário

excelente=0
ruim=0
for i in range(50):
 print("Olá seja-bem vindo(a) a nossa pesquisa de satisfação.")
 Nome= input("Por gentileza, Digite seu nome:") 
 idade=int(input("Agora, Digite sua idade:"))

 #Processamento de dados da avaliação
 print("Você descreveria nosso sistema como?")
 avaliação= int(input("1-Excelente, 2-Bom, 3-Ruim:"))
 while avaliação < 1 or avaliação > 3:
    print("Opção inválida! Por favor, escolha apenas 1, 2 ou 3.")
    avaliação = int(input("1-Excelente, 2-Bom, 3-Ruim: "))

#Saída de dados 
 if avaliação ==3:
    ruim = ruim + 1
 elif avaliação ==1:
    excelente = excelente + 1
print(f"O total de avaliações ruins foram de:{ruim}")
print(f"O total de avaliações excelente foram de:{excelente}")
print("Obrigada! Sua avaliação é muito importante para nós!")
