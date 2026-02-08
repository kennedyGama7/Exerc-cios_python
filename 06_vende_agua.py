
texto = """"
Escolhar a água para comprar
(1)Água mineral natural
(2)Água mineral com gáz
""" 
opção = input(texto)


if opção == "1":
   conta = 1,50

elif opção == "2":
    conta = 2.50
    
if conta == 0:

    print('Digite uma opção correta...')
else:
    print(f'O valor da água escolhida é R${conta} ')
