
tree = {"pergunta": "Digite a quantidade de quartos: ", 
        "limiar": 3.5, 
        "maior":    {
                        "pergunta": "Digite a quatidade de piso (andares): ", 
                        "limiar": 1.25,
                        "maior": {
                                    "pergunta": "Digite o ano de construção da casa que deseja: ",
                                    "limiar": 2002.5,
                                    "maior": "Abaixo da média!",
                                    "menor": "Dentro da média!"

                                 },
                        "menor": "Abaixo da média!"
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

while True: 
   resposta = int(input(tree["pergunta"])) 
   if resposta > tree["limiar"]:
      tree = tree["maior"]
   else:
      tree = tree["menor"]
   if isinstance(tree, str):
      print(tree)
      break
   

   

