# criar um jovo com resultados finais
# cenario: cenário de guerra com dois lados: time1 e time2, um dos lados pode guanhar, conseguindo assim a vitoria
# pois as respostas corretas te leva a vitoria



class JogoDeAventura:
    def _init_(self):
       self.pergunta1 = 'voce nasceu no norte no ou sul? (norte / sul)'# norte = ladoA, sul = ladoB
       self.pergunta2 = 'voce prefere escudo ou espada? (escudo/espada)'  # espada = lado1, armadura =lado2
       self.pergunta3 = 'prefere linha de frente, ou ataque lateral? (french/lado)'  # linha de frente = lado1, lateral=lado2
       self.finalHistoria1 = 'você será um heroi na linha de frente'
       self.finalHistoria2 = 'você será um heroi nas defesa'
       self.finalHistoria3 = 'você vai se sacrificar na batalha'
       self.finalHistoria4 = 'você não foi capaz de lutar essa batalha'
    def welcome(self):
       self.pergunta1 = 'voce nasceu no norte no ou sul? (norte / sul)'# norte = ladoA, sul = ladoB
       self.pergunta2 = 'voce prefere escudo ou espada? (escudo/espada)'  # espada = lado1, armadura =lado2
       self.pergunta3 = 'prefere linha de frente, ou ataque lateral? (french/lado)'  # linha de frente = lado1, lateral=lado2
       self.finalHistoria1 = 'você será um heroi na linha de frente'
       self.finalHistoria2 = 'você será um heroi nas defesa'
       self.finalHistoria3 = 'você vai se sacrificar na batalha'
       self.finalHistoria4 = 'você não foi capaz de lutar essa batalha'
       resposta1 = input(self.pergunta1)
       if resposta1 == 'norte':
            resposta1B = input(self.pergunta2)

            if resposta1B == 'espada':
                print(self.finalHistoria1)
            if resposta1B == 'escudo':
                print(self.finalHistoria2)
       if resposta1 == 'sul':
            resposta1B = input(self.perguntas3)
            if resposta1B == 'linha de frente':
                print()
            if resposta1B == 'ataque lateral':
                print(self.finalHistoria4)


jogo = JogoDeAventura()
jogo.welcome()
