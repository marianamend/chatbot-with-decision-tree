print("\n\n\nSeja bem-vinda(o) ao Mig! \nNosso chatbot que irá lhe fornecer um orçamento sobre imóveis! ")
while True: 
   tree = {"pergunta": "Digite a quantidade de quartos: ", 
         "limiar": 4, 
         "maior":    {
                           "pergunta": "Digite o ano de construção da casa que deseja: ", 
                           "limiar": 2001.5,
                           "maior": "Abaixo da média!",
                           "menor": {
                                        "pergunta": "Por favor, digite o ano de construção da casa novamente: ",
                                        "limiar": 1978.5,
                                        "maior": "Dentro da média!",
                                        "menor": "Abaixo da média!"
                                    },
                     },
            "menor": {
                        "pergunta": "Digite o ano de construção da casa que deseja: ",
                        "limiar": 1978.5,
                        "menor": {
                                    "pergunta": "Digite a quantidade de banheiros: ",
                                    "limiar": 1.25,
                                    "menor": "Acima da média!",
                                    "maior": "Abaixo da média!"
                                 },
                        "maior": "Dentro da média!"
                     },
         }


   print("Caso queira encerrar, digite: '-1' ")
   while True: 
      resposta = int(input(tree["pergunta"]))
      if resposta == -1:
         break
          
      if resposta > tree["limiar"]:
         tree = tree["maior"]
      else:
         tree = tree["menor"]
      if isinstance(tree, str):
         print(tree)
            
         print("----------------------------------")
         break
   if resposta == -1:
      print("----------fim------------")
      break