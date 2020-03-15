import os
import random
import colorama
from colorama import Fore, Back, Style
colorama.init(True)


class barco():#clase padre de barco
    def __init__(self,tamano):
        self.tamano = tamano

    
    def posicionBaseBarco (self,matriz):
        '''Genera las coordenada donde se van posicionar los diferentes barcos '''
        direccion=random.randrange(2) #1 ES HORIZONAL Y 0 ES VERTICAL

        valido=False
        if self.tamano==1:
            while valido==False:
                coordenadaX=random.randint(0,9)
                coordenadaY=random.randint(0,9)
                coordenadaFinal=[coordenadaX,coordenadaY]
                valido=comprobarPos(matriz,coordenadaFinal[1],coordenadaFinal[0])

        else:
            while valido==False:
                if direccion==1:
                    if self.tamano==3:
                        coordenadaX=random.randint(0,7)
                        coordenadaY=random.randint(0,9)
                        coordenadaFinal=[[coordenadaX,coordenadaY],[coordenadaX+1,coordenadaY],[coordenadaX+2,coordenadaY]]
                    elif self.tamano==2:
                        coordenadaX=random.randint(0,8)
                        coordenadaY=random.randint(0,9)
                        coordenadaFinal=[[coordenadaX,coordenadaY],[coordenadaX+1,coordenadaY]]

                elif direccion==0:
                    if self.tamano==3:
                        coordenadaX=random.randint(0,9)
                        coordenadaY=random.randint(0,7)
                        coordenadaFinal=[[coordenadaX,coordenadaY],[coordenadaX,coordenadaY+1],[coordenadaX,coordenadaY+2]]
                    elif self.tamano==2:
                        coordenadaX=random.randint(0,9)
                        coordenadaY=random.randint(0,8)
                        coordenadaFinal=[[coordenadaX,coordenadaY],[coordenadaX,coordenadaY+1]]
    

                for array in coordenadaFinal:
                    #print(direccion)
                    #print(array[1],array[0])
                    #print(comprobarPos(matriz,array[1],array[0]))
                    sirve=comprobarPos(matriz,array[1],array[0])
                    if sirve==True:
                        valido=True
                    else:
                        break
                    
            
        return coordenadaFinal

    def __repr__(self):
        '''Metodo de impresion de los objetos en pantalla'''
        return '0'

class portaAvion(barco):#Clase del barco de 3 posiciones con su respectiva habilidad
    def __init__(self,tamano):
        barco.__init__(self,tamano)
    
    def habilidad1(self):
        print('''
        ⦿ Porta Avion : este buque de 3 posiciones tiene la capacidad de aterrizar helicópteros en él para el transporte de tropas. 1 EN TOTAL EN EL MAPA 
        ''')

class buque(barco):#Clase del barco de 2 posiciones con su respectiva habilidad
    def __init__(self,tamano):
        barco.__init__(self,tamano)
    
    def habilidad2(self):
        print('''
        ⦿ Fragata: de 2 posiciones  Tiene la capacidad de comunicarse con tierra y los otros miembros de la flota. 
        1 EN TOTAL EN EL MAPA 
        ''')

class submarino(barco):#Clase del barco de 1 posicion con su respectiva habilidad
    def __init__(self,tamano):
        barco.__init__(self,tamano)
    
    def habilidad3(self):
        print('''
        ⦿ Submarino: de 1 posicion Tiene la capacidad de poder sumergirse y emerger del agua. 4 EN TOTAL EN EL MAPA 
        ''')
    

def comprobarPos(matriz,x,y):
    '''Comprueba que una coordenada este libre y sus alrededores '''
    libre=True 
    if matriz[x][y]!='O':
        libre=False
        return libre
       
    if x>0:
        #print(matriz[x-1][y])
        if matriz[x-1][y]!='O':
            libre=False
            return libre
    if y>0:
        #print(matriz[x][y-1])
        if matriz[x][y-1]!='O':
            libre=False
            return libre
    if  x<9:
        #print(matriz[x+1][y])
        if matriz[x+1][y]!='O':
            libre=False
            return libre
    if y<9:
        #print(matriz[x][y+1])
        if matriz[x][y+1]!='O':
            libre=False
            return libre

    return libre

def iniciarTablarero(matriz,portaAvion,buque,submarino):
    '''Ubica los barcos en la matriz'''
    for lista in barco(3).posicionBaseBarco(matriz):
        #print(lista)
        matriz[lista[1]][lista[0]]=portaAvion

    for lista in barco(2).posicionBaseBarco(matriz):
        #print(lista)
        matriz[lista[1]][lista[0]]=portaAvion

    for i in range (4):
        pos=barco(1).posicionBaseBarco(matriz)
        #print(pos)
        matriz[pos[1]][pos[0]]=submarino
    return matriz

def pedirCoordenadaX(mesagges):
    '''Pide la componente x de la coordenada donde desea disparar el usuario y la valida'''
    esValido=False
    while not esValido:
        try:
            num=int(input(mesagges))
            if num > 0 and num<=10:
                esValido=True
            else:
                print('Coordenada invalida')
        except ValueError:
            print("Invalido")
    num=num-1
    return num

def pedirCoordenadaY(mesagges):
    '''Pide la componente y de la coordenada donde desea disparar el usuario y la valida'''
    esValido=False
    letras={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}
    while not esValido:
        letra=input(mesagges)
        letra=letra.upper()
        if letra in letras:
            esValido=True
        else:
            esValido=False
            print('Coordenada Invalida')
    coordenadaY=int(letras[letra])
    return coordenadaY

def disparar (matriz,x,y):
    '''recibe las coordenas y ejecuta el disparo en la matriz y lo refleja '''
    acertado=False
    tiroInvalido=False
    if matriz[y][x]=='O':
        matriz[y][x]='X'

    elif matriz[y][x]=='F' or matriz[y][x]=='X':
        tiroInvalido=True 

    elif matriz[y][x]!='X' and matriz[y][x]!='O' and matriz[y][x]!='F':

        acertado=True
        matriz[y][x]='F'
    array=[matriz,acertado,tiroInvalido]
    return array
    
def imprimirTablero (matriz):
    '''Imprime con formato la matriz del tablero '''
    letras=['A','B','C','D','E','F','G','H','I','J']
    numeros=['1','2','3','4','5','6','7','8','9','10']
    print(Fore.BLUE+'        {}      {}      {}      {}      {}      {}      {}      {}      {}     {}  '.format(*numeros))
    for i,fila in enumerate(matriz,1):
            print('\n')
            print(Fore.BLUE+'{}'.format(letras[i-1]), end='\t')
            for col in fila:
                if col=='F':
                    print(Fore.CYAN+col,end='      ')       
                elif col=='X':
                    print(Fore.RED+col,end='      ')
                else:
                    print(col,end='      ') 


'''======================================================================================================='''

        
def jugar ():
    '''Funcion que genera la parte operativa del juego'''
    matriz=[
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]
    PortaAvion=portaAvion(3)
    Buque=buque(2)
    Submarino=submarino(1)

    print('\n');print('A continuacion se muestran las instrucciones y las habilidades de los barcos situados en el mapa '.center(120,' '));print('\n')
    
    print('⦿ El juego le pedira la coordenada numerica del tablero primero y luego un tipo de coordenada alfabetica para poder asi  completar la coordenada donde usted mi capitan del navio desea disparar, espero que tenga mucha suerte en alta mar!!!'.center(120,' '));print('\n')
    PortaAvion.habilidad1()
    Buque.habilidad2()
    Submarino.habilidad3()
    print('\n')

    iniciarTablarero(matriz,PortaAvion,Buque,Submarino)
    imprimirTablero(matriz)
    print('\n')
    

    hundido=0
    repetido=0
    movimientos=0
    puntaje=0

    while hundido!=9:
        print('\n')
        coordenadaX= pedirCoordenadaX('Ingrese la coordenada en X a la cual desea disparar (coordenada numerica): ')
        coordenadaY=pedirCoordenadaY('Ingrese la coordenada en Y a la cual desea disparar (coordenada letra): ')
        datosDisparo=disparar(matriz,coordenadaX,coordenadaY)
        matriz=datosDisparo[0]
        print('\n')
        imprimirTablero(matriz)
        print('\n')
        if datosDisparo[2]==True:
            repetido=repetido+1
            print('Tiro invalido')
            print('Su puntaje es ',puntaje)
        elif datosDisparo[1] == True:
            hundido=hundido+1
            print('Tiro acertado')
            puntaje=puntaje+10
            print('Su puntaje es ',puntaje)
        else:
            print('Fallaste')
            if puntaje>=2:
                puntaje=puntaje-2
            print('Su puntaje es ',puntaje)
        movimientos=movimientos+1

        

    print ('█'.center(120,'█'));print('\n')
    print(Fore.BLUE+'''
                            ██████╗  █████╗ ███╗   ██╗ █████╗ ███████╗████████╗███████╗
                            ██╔════╝ ██╔══██╗████╗  ██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝
                            ██║  ███╗███████║██╔██╗ ██║███████║███████╗   ██║   █████╗  
                            ██║   ██║██╔══██║██║╚██╗██║██╔══██║╚════██║   ██║   ██╔══╝  
                            ╚██████╔╝██║  ██║██║ ╚████║██║  ██║███████║   ██║   ███████╗
                            ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝
                                                            ''')


    if movimientos==9:
        print('¿Eres un Robot? lo que acabas de hacer es poco probable ...'.center(120,' '))
    elif movimientos<45:
        print('Excelente estrategia'.center(120,' '))
    elif movimientos>=45 and movimientos<=70:
        print('Buena estrategia pero hay que mejorar'.center(120,' '))
    elif movimientos>70:
        print('Considerese perdedor, tiene que mejorar notablemente'.center(120,' '))

    print('⦿ Total de puntos obtenidos {} '.format(puntaje).center(120,' '))
    print('⦿ Total de disparos {} '.format(movimientos).center(120,' '))
    print('⦿ Total de disparos repetidos {} '.format(repetido).center(120,' '))
    
    



    return movimientos,puntaje
        
        
