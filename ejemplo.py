import asyncio
import math
from operator import truediv
from ejemplo2 import ejemplo as raizCuadrada
# Interpretado, y no ejecutado( más lento C#, Java, C++, C)
# Todo es un objeto
# tipos de datos(int, float, complex, str)
# using, import, import/required

# C# List<string> list = new List<string>;
#List, add, remove, index, pop, insert , ordenada e iterable, se puede modificar
list_ = [1,2,3,1.5,99003.32, "jksalj"]

# Tuplas, ordenadas e iterables, pero no se puede modificar
tupla_ = (1,2,3,4,5,"jdskal","jdklas",120.93)
print(tupla_)
tupla2 =  list(tupla_)
print(math.pi)

# Diccionario
dict_ =  {"hola":"mundo", "como":"estas"}

# Bucles Loops
# While, for, no existe el do while

for i,j in dict_.items():
    print(i,j)

raizCuadrada(8,90)
# C#, Prueba (Prueba), TypeScript, constructor, (Js C# / this) = self
# Class POO
# Herencia, Java, Js, c#, C++...., Herencia Multiple
# C# --> Interfaces, TypeScript
# C#(Base), TyPeScript, Java Super

class Humano:
    ojos = 2
    nariz = True
    boca = True
    
    def __init__(self, color):
        self.color = color
    
    def prueba(self, hola):
        print(hola)
        

class Indigena(Humano):
    flechas = True
    pintura = True
    
    def __init__(self, cama, color):
        super().__init__(color)
        self.cama =cama
        
    def prueba(self, hola):
        super().prueba(hola)
        print("robert y daniela")
        

wayuu = Indigena(10, "negro")
print(wayuu.ojos)
print(wayuu.cama)
print(wayuu.color)
print(wayuu.prueba("hola"))
