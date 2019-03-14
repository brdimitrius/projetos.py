import sys
import getpass
namepc = getpass.getuser()
name = (namepc.title())
print("Bem-vindo "+name)
print("\nMapa: \n\n   X  X  X  X  X  X  X  X  X  X\n10                             Y\n 9                             Y\n 8                             Y\n 7                             Y\n 6                             Y\n 5              ●(middle)      Y\n 4                             Y\n 3                             Y\n 2                             Y\n 1                             Y\n 0 1  2  3  4  5  6  7  8  9  10\n")
class Robot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getplacex(self):
        x_place_str = str(self.x)
        areax = ("X = %s,"%(x_place_str))
        print(areax)
    def getplacey(self):
        y_place_str = str(self.y)
        areay = ("Y = %s"%(y_place_str))
        print(areay)
    def move_up(self, y):
        if self.y >= 5:
            self.y = (cimaa)
            robot1.getplacey()
        else:
            print("Movimento proibido")
    def move_down(self, y):
        if self.y <= 10:
            self.y = (down_n)
        else:
            print("Movimento proibido")
    def move_right(self, x):
        if self.x == 5:
            self.x = (self.x + direita_1)
        else:
            print("Movimento proibido")
    def move_left(self, x):
        if self.x <= 10:
            self.x = (esquerda_n)
        else:
            print("Movimento proibido")

#Quadro
robot1=Robot(x=5, y=5)
#Subir

subir = input("Voce quer ir para cima (s/n) ? \n")
if subir == "s":
    up = int(input("Digite quantas casas vc quer ir para cima (Max: 5): \n"))
    up_s = str(up)
    if up <= 5:
        cimaa = robot1.y + up
        robot1.move_up(cimaa)
    elif up > 5:
        print("O Limite é de 5 casas para cima e não "+ up_s +  ", encerrando o codigo, " + name + ".")
        sys.exit()
elif subir == "n":
    up = 0
    cimaa = robot1.y + up
    robot1.move_up(cimaa)

#Descer

descer = input("Voce quer descer (s/n) ? \n")
if descer == "s":
    downn = int(input("Digite quantas casas vc quer ir para baixo (Max: 5): \n"))
    down_s = str(downn)
    if downn <= 5:
        down_n = robot1.y - downn
        robot1.move_down(down_n)
    elif downn > 5:
        print("O Limite é de 5 casas para baixo e não "+ down_s +  ", encerrando o codigo, " + name + ".")
        sys.exit()
elif descer == "n":
    downn = 0

#Direita

direita = input("Voce quer ir para a direita (s/n) ? \n")
if direita == "s":
    direita_1 = int(input("Digite quantas casa voce quer ir para a direita ? \n"))
    direita_2 = str(direita_1)
    if direita_1 <= 5:
        direita_n = robot1.x + direita_1
        robot1.move_right(direita_n)
    elif direita_1 > 5:
        print("O Limite é de 5 casas para a direita e não "+ direita_2 +  ", encerrando o codigo, " + name + ".")
        sys.exit()
elif direita == "n":
    direita_1 = 0

#Esquerda

esquerda = input("Voce quer ir para a esqueda (s/n) ? \n")
if esquerda == "s":
    esquerda_1 = int(input("Digite quantas casas voce quer ir para a esquerda? \n"))
    esquerda_2 = str(esquerda_1)
    if esquerda_1 <= 5:
        esquerda_n = robot1.x - esquerda_1
        robot1.move_left(esquerda_n)
    elif esquerda_1 > 5:
        print("O Limite é de 5 casas para a esquerda e não "+ esquerda_2 +  ", encerrando o codigo, " + name + ".")
        sys.exit()
elif esquerda == "n":
    esquerda_1 = 0

#Posição

print("\nMapa: \n\n   X  X  X  X  X  X  X  X  X  X\n10                             Y\n 9                             Y\n 8                             Y\n 7                             Y\n 6                             Y\n 5                             Y\n 4                             Y\n 3                             Y\n 2                             Y\n 1                             Y\n 0 1  2  3  4  5  6  7  8  9  10\n")

Yy = str(robot1.y)
Xx = str(robot1.x)
print("Posiçoẽs: \nArea Vertical ( Y ): " + Yy,"\nArea Horizontal ( X ): " + Xx + "\n")
