print("---------PIZZARIA ITALY---------")
print("OLÁ BOA NOITE! SEJA BEM VINDO . O QUE VOCÊ DESEJA?")
print(" ")
print("Sabores das pizzas:")
print("Calabresa , Frango e Catupiry")
print("Tamanhos das pizzas:")
print("Pizza pequena :  R$ 25.00")
print("Pizza média   :  R$ 45.00")
print("Pizza grande  :  R$ 65.00")
print("Refrigerantes: ")
print("Coca-cola     :   R$ 7.00")
print("Guaraná       :   R$7.00")
print("Fanta         :   R$6.OO")
print("-------------------------")
print(" ")
print("AGORA ESCOLHA:")
print("1- Calabresa")
print("2- Frango")
print("3- Frango com Catupiry")
print("--------------------------")
#lê a escolha do sabor da pizza do usuário e converte para inteiro.
pedidopizza = int(input())

print("Agora escolha o tamanho:")
print("P- Pequena")
print("M- Média")
print("G- Grande")
print("-------------------------")
#Lê a escolha do tamanho da pizza do usuário e converte para maiúsculo
tampizza = input().upper()

print("Agora escolha o refrigerante: ")
print("1-Coca-cola")
print("2-Guaraná")
print("3-Fanta")
#Lê a escolha do refrigerante do usuário e converta para inteiro
pedidorefri = int(input())

#Calcular o preço total e descreve o pedido utilizado elif com parênteses.

if (pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 1) :
    precopagar = 25.00 + 7.00 
    pedidos = "Calabresa , Pequena e Coca-cola"

elif (pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 2) :
    precopagar = 25.00 + 7.00 
    pedidos = "Calabresa , Pequena e Guaraná"
    
elif (pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 3) :
    precopagar = 25.00 + 6.00 
    pedidos = "Calabresa , Pequena e Fanta"
    
if (pedidopizza == 2) and (tampizza == "P") and (pedidorefri == 1) :
    precopagar = 45.00 + 7.00 
    pedidos = "Frango , Pequena e Coca-cola"
    
elif (pedidopizza == 2) and (tampizza == "P") and (pedidorefri == 2) :
    precopagar = 45.00 + 7.00 
    pedidos = "Frango , Pequena e Guaraná"
    
elif (pedidopizza == 2) and (tampizza == "P") and (pedidorefri == 3) :
    precopagar = 45.00 + 6.00 
    pedidos = "Frango , Pequena e Fanta"
    
if (pedidopizza == 3) and (tampizza == "P") and (pedidorefri == 1) :
    precopagar = 65.00 + 7.00 
    pedidos = "Frango com Catupiry , Pequena e Coca-cola"
    
elif (pedidopizza == 3) and (tampizza == "P") and (pedidorefri == 2) :
    precopagar = 65.00 + 7.00 
    pedidos = "Frango com Catupiry , Pequena e Guaraná"
    
elif (pedidopizza == 3) and (tampizza == "P") and (pedidorefri == 3) :
    precopagar = 65.00 + 6.00 
    pedidos = "Frango com Catupiry , Pequena e Fanta"

if (pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 1) :
    precopagar = 25.00 + 7.00 
    pedidos = "Calabresa , Média e Coca-cola"

elif (pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 2) :
    precopagar = 25.00 + 7.00 
    pedidos = "Calabresa , Média e Guaraná"

elif (pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 3) :
    precopagar = 25.00 + 6.00 
    pedidos = "Calabresa , Média e Fanta"
    
if (pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 1) :
    precopagar = 45.00 + 7.00 
    pedidos = "Frango , Média e Coca-cola"
    
elif (pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 2) :
    precopagar = 45.00 + 7.00 
    pedidos = "Frango , Média e Guaraná"
    
elif (pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 3) :
    precopagar = 45.00 + 6.00 
    pedidos = "Frango , Média e Fanta"
    
if (pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 1) :
    precopagar = 65.00 + 7.00 
    pedidos = "Frango com Catupiry , Média e Coca-cola"
    
elif (pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 2) :
    precopagar = 65.00 + 7.00 
    pedidos = "Frango com Catupiry , Média e Guaraná"

elif (pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 3) :
    precopagar = 65.00 + 6.00 
    pedidos = "Frango com Catupiry , Média e Fanta"    
 
if (pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 1) :
    precopagar = 65.00 + 7.00 
    pedidos = "Calabresa , Grande e Coca-cola"
    
elif (pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 2) :
    precopagar = 65.00 + 7.00 
    pedidos = "Calabresa , Grande e Guaraná"
    
elif (pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 3) :
    precopagar = 65.00 + 6.00 
    pedidos = "Calabresa , Grande e Fanta"
    
if (pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 1) :
    precopagar = 65.00 + 7.00 
    pedidos = "Frango , Grande e Coca-cola"
    
if (pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 2) :
    precopagar = 65.00 + 7.00 
    pedidos = "Frango , Grande e Guaraná"
    
if (pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 3) :
    precopagar = 65.00 + 6.00 
    pedidos = "Frango , Grande e Coca-cola"

if (pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 1) :
    precopagar = 65.00 + 7.00 
    pedidos = "Calabresa , Grande e Coca-cola"
    
elif (pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 2) :
    precopagar = 65.00 + 7.00 
    pedidos = "Frango com Catupiry , Grande e Guaraná"
    
elif (pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 3) :
    precopagar = 65.00 + 6.00 
    pedidos = "Frango com Catupiry , Grande e Fanta"


    
# Exibe o resumo do pedido e preço total a pagar
print("                                       ")
print(f"O TOTAL A PAGAR É: R$ {precopagar:.2f}") 
print("                                       ")
print(f"OS PEDIDOS FORAM {pedidos}")  
print("                                       ")
print("BOM APETITE E MUITO OBRIGADO!")

    

