# importante bibliotecas
import random
from os import system,name

# criando funcao para limpar a tela 
def limpa_tela():
    # Verifica o sistema operacional
    if name == 'nt':  # Windows
        _ = system('cls')
    else:  # Linux, Mac, etc.
        _ = system('clear')

# board do hangman
board = ["""

"""]

class hangman:
    # metodo contrutor 
    def __init__(self, palavra):
        self.palavra = palavra
        self.letra_errada=[]
        self.letra_escolhida=[]
        
    # metodo advinha 
    def guess(self, letra):
        if letra in self.palavra and letra not in self.letra_escolhida:
            self.letra_escolhida.append(letra)

        elif letra not in self.palavra and letra not in self.letra_errada:
            self.letra_errada.append(letra)

        else:
            return False
        
        return True
    
    # metodo para verificar se o jogo terminou 
    def hangman_over ( self):
        return self.hangman_won() or (len(self.letra_errada)== 6)
    
    # metodo para ver se o jogador venceu
    def hangman_won(self):
        if "_" not in self.hide_palavra():
            return True
        return False
    
    # metodo para nao mostrar a letra no board
    def hide_palavra(self):
            rtn =""

            for letra in self.palavra:
                 if letra not in self.letra_escolhida:
                    rtn += "_"
                 else: 
                     rtn += letra
                 return rtn
            

        
    