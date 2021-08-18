import random

def get():
    jokes = ["Doutor, como eu faço para emagrecer? Basta a senhora mover a cabeça da esquerda para a direita e da direita para a esquerda. Quantas vezes, doutor? Todas as vezes que lhe oferecerem comida.", "Dois amigos se encontram depois de muitos anos. Casei, separei e já fizemos a partilha dos bens. E as crianças? O juiz decidiu que ficariam com aquele que mais bens recebeu. Então ficaram com a mãe? Não, ficaram com nosso advogado."]
    return jokes[random.randrange(0, len(jokes))]
