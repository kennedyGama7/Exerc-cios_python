print('='*40)
print(' Validador de Senha ')
print('='*40)


while True:
   
   tem_numero = False
   tem_maiuscula = False

   senha = input('Digite sua senha (8 caracteres,pelo menos 1 número e  1 letra maiúscula.):')
   qtd_caracteres = len(senha)

   if qtd_caracteres < 8:
      print('mínimo de 8 caracteres.')
      continue
   else:
      for i in senha:
         if i.isdigit():
            tem_numero = True
         if i.isupper():
            tem_maiuscula = True
   if tem_numero == False:
      print('É necessário pelo menos 1 número.')
   elif tem_maiuscula == False:
      print('É necessário pelo menos 1 letra maiúscula. ')
   else:
      print('Senha cadastrada com sucesso!')
      break
      

    
