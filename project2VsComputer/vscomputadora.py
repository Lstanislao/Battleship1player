import random
import colorama
import time
from colorama import Fore, Back, Style
colorama.init(True)

class barcoJugador():
    def __init__(self,tamano):
        self.tamano = tamano

    def __repr__(self):
            return 'B'

    def construirBarcoJugador(self):
        
        valido=False

        if self.tamano==1:
            while valido==False:
                coordenadaX=pedirCoordenadaX('''
                Ingrese la coordenada numerica donde desea colocar el submarino:
                ''',True,self.tamano)
                coordenadaY=pedirCoordenadaY('''
                Ingrese la coordenada letra donde desea colocar el submarino: 
                ''',True,self.tamano)
                coordenadaFinal=[coordenadaX,coordenadaY]
                if comprobarPos(tabla,coordenadaFinal[1],coordenadaFinal[0])==True:
                    valido=True
                else:
                    print('Esas coordenadas no son validas porque interfieren con otro barco')
                    valido=False

        else:
            direccion=pedirDireccion('''
            Ingrese la direccion, 1 para horizontal y 0 para vertical: 
            ''');print('\n')
            while valido==False:
                coordenadaX=pedirCoordenadaX('''
                Ingrese la coordenada numerica donde desea colocar el barco
                ''',True,self.tamano)
                coordenadaY=pedirCoordenadaY('''
                Ingrese la coordenada letra donde desea colocar el barco
                ''',True,self.tamano)
                if direccion==1:
                    if self.tamano==3:
                        coordenadaFinal=[[coordenadaX,coordenadaY],[coordenadaX+1,coordenadaY],[coordenadaX+2,coordenadaY]]
                    elif self.tamano==2:
                        coordenadaFinal=[[coordenadaX,coordenadaY],[coordenadaX+1,coordenadaY]]
                elif direccion==0:
                    if self.tamano==3:
                        coordenadaFinal=[[coordenadaX,coordenadaY],[coordenadaX,coordenadaY+1],[coordenadaX,coordenadaY+2]]
                    elif self.tamano==2:
                        coordenadaFinal=[[coordenadaX,coordenadaY],[coordenadaX,coordenadaY+1]]

                for array in coordenadaFinal:
                    sirve=comprobarPos(tabla,array[1],array[0])
                    if sirve==True:
                        valido=True
                    elif sirve==False:
                        print('Esas coordenadas no son validas porque interfieren con otro barco')
                        break
            
        return coordenadaFinal
    
        


class barco():
    
    def __init__(self,tamano):
        self.tamano = tamano

    
    def posicionBaseBarco (self,matriz):
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
                    sirve=comprobarPos(matriz,array[1],array[0])
                    if sirve==True:
                        valido=True
                    else:
                        break
        return coordenadaFinal

    def __repr__(self):
        return 'O'


    

class portaAvion(barco):
    def __init__(self,tamano):
        barco.__init__(self,tamano)
    
    def habilidad1(self):
        print('''
        ⦿ Porta Avion : este buque de 3 posiciones tiene la capacidad de “aterrizar helicópteros” en él para el transporte de tropas. 1 EN TOTAL EN EL MAPA 
        ''')


class buque(barco):
    def __init__(self,tamano):
        barco.__init__(self,tamano)
    
    def habilidad2(self):
        print('''
        ⦿ Fragata: de 2 posiciones  Tiene la capacidad de comunicarse con tierra y los otros miembros de la flota. 1 EN TOTAL EN EL MAPA 
        ''')
 

class submarino(barco):
    def __init__(self,tamano):
        barco.__init__(self,tamano)
    
    def habilidad3(self):
        print('''
        ⦿ Submarino: de 1 posicion Tiene la capacidad de poder sumergirse y emerger del agua. 4 EN TOTAL EN EL MAPA 
        ''')

    

def comprobarPos(matriz,x,y):
    '''Comprueba las posiciones contiguas a una coordenada'''
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
    '''Coloca los barcos en tablero de la computadora'''
    for lista in barco(3).posicionBaseBarco(matriz):
        matriz[lista[1]][lista[0]]=portaAvion

    for lista in barco(2).posicionBaseBarco(matriz):
        #print(lista)
        matriz[lista[1]][lista[0]]=portaAvion

    for i in range (4):
        pos=barco(1).posicionBaseBarco(matriz)
        #print(pos)
        matriz[pos[1]][pos[0]]=submarino
    return matriz


def iniciarTableroJugador(matriz,portaAvion,buque,submarino):
    '''Coloca los barcos en tablero del jugador'''
    for lista in barcoJugador(3).construirBarcoJugador():
        matriz[lista[1]][lista[0]]=portaAvion
    imprimirTablero(matriz)


    for lista in barcoJugador(2).construirBarcoJugador():
        #print(lista)
        matriz[lista[1]][lista[0]]=portaAvion
    imprimirTablero(matriz)


    for i in range (4):
        pos=barcoJugador(1).construirBarcoJugador()
        #print(pos)
        matriz[pos[1]][pos[0]]=submarino
        imprimirTablero(matriz)

    return matriz


def pedirCoordenadaX(mesagges,paraTablero=False,pos=1):
    '''Pide la coordenada x para realizar el disparo del jugador'''

    esValido=False
    while not esValido:
            try:
                num=int(input(mesagges))
                if paraTablero==False:
                    if num >= 0 and num<=10:
                        esValido=True
                    else:
                        print('Coordenada invalida')
                if paraTablero==True:
                    if pos==3:
                        if num >= 0 and num<=7:
                            esValido=True
                        else: 
                            print('En esa posicion el barco se saldria del tablero ')
                            esValido=False
                    elif pos==2:
                        if num >= 0 and num<=8:
                            esValido=True
                        else: 
                            print('En esa posicion el barco se saldria del tablero ')
                            esValido=False
                    elif pos==1:
                        esValido=True
                            
            except ValueError:
                print("Invalido")
    num=num-1
    return num

def pedirCoordenadaY(mesagges,paraTablero=False,pos=0):
    '''Pide la coordenada y para realizar el disparo del jugador'''
    esValido=False
    letras={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}
    while not esValido:
        letra=input(mesagges)
        letra=letra.upper()
        if letra in letras:
            esValido=True
            coordenadaY=int(letras[letra])
        else:
            esValido=False
            print('Coordenada Invalida')
        

        if paraTablero==True and esValido==True:
            if pos==3:
                if coordenadaY >= 0 and coordenadaY<=7:
                    esValido=True
                else:
                    esValido=False
                    print('En esa posicion el barco se saldria del tablero ')
            if pos==2:
                if coordenadaY >= 0 and coordenadaY<=8:
                    esValido=True
                else:
                    esValido=False
                    print('En esa posicion el barco se saldria del tablero ')
    return coordenadaY

def pedirDireccion(mesagges):
    '''Pide la dirrecion en la que desea posicionar el barco'''
    esValido=False
    while not esValido:
        try:
            num=int(input(mesagges))
            if num== 0 or num==1:
                esValido=True
            else:
                print('Direccion invalida, Ingrese 1 para horizontal y 0 para vertical')
        except ValueError:
            print('Direccion invalida, Ingrese 1 para horizontal y 0 para vertical')
    return num


def disparar (matriz,x,y):
    '''accion disparar del jugador '''
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
    '''Imprime el tablero aliado'''
    print(Fore.BLUE+'''
   ▄████████  ▄█        ▄█     ▄████████ ████████▄   ▄██████▄  
  ███    ███ ███       ███    ███    ███ ███   ▀███ ███    ███ 
  ███    ███ ███       ███▌   ███    ███ ███    ███ ███    ███ 
  ███    ███ ███       ███▌   ███    ███ ███    ███ ███    ███ 
▀███████████ ███       ███▌ ▀███████████ ███    ███ ███    ███ 
  ███    ███ ███       ███    ███    ███ ███    ███ ███    ███ 
  ███    ███ ███▌    ▄ ███    ███    ███ ███   ▄███ ███    ███ 
  ███    █▀  █████▄▄██ █▀     ███    █▀  ████████▀   ▀██████▀  
             ▀                                                 
        ''')
   
    letras=['A','B','C','D','E','F','G','H','I','J']
    numeros=['1','2','3','4','5','6','7','8','9','10']
    print(Fore.BLUE+'        {}      {}      {}      {}      {}      {}      {}      {}      {}     {}  '.format(*numeros))
    for i,fila in enumerate(matriz,1):
            print('\n')
            print(Fore.BLUE+'{}'.format(letras[i-1]), end='\t')
            for col in fila:
                if col=='F':
                    print(col,end='      ')       
                elif col=='X':
                    print(col,end='      ')
                else:
                    print(col,end='      ') 
    print('\n')


def imprimirTablero2(matriz):
    '''Imprime el tablero enemigo'''
    print(Fore.RED+'''
   ▄████████ ███▄▄▄▄      ▄████████   ▄▄▄▄███▄▄▄▄    ▄█     ▄██████▄   ▄██████▄  
  ███    ███ ███▀▀▀██▄   ███    ███ ▄██▀▀▀███▀▀▀██▄ ███    ███    ███ ███    ███ 
  ███    █▀  ███   ███   ███    █▀  ███   ███   ███ ███▌   ███    █▀  ███    ███ 
 ▄███▄▄▄     ███   ███  ▄███▄▄▄     ███   ███   ███ ███▌  ▄███        ███    ███ 
▀▀███▀▀▀     ███   ███ ▀▀███▀▀▀     ███   ███   ███ ███▌ ▀▀███ ████▄  ███    ███ 
  ███    █▄  ███   ███   ███    █▄  ███   ███   ███ ███    ███    ███ ███    ███ 
  ███    ███ ███   ███   ███    ███ ███   ███   ███ ███    ███    ███ ███    ███ 
  ██████████  ▀█   █▀    ██████████  ▀█   ███   █▀  █▀     ████████▀   ▀██████▀  
                                                                                 
    ''')

    letras=['A','B','C','D','E','F','G','H','I','J']
    numeros=['1','2','3','4','5','6','7','8','9','10']
    print(Fore.RED+'         {}       {}       {}       {}       {}       {}       {}       {}       {}      {}  '.format(*numeros))
    for i,fila in enumerate(matriz,1):
            print('\n')
            print(Fore.RED+'{}'.format(letras[i-1]), end='\t')
            for col in fila:
                if col=='F':
                    print(Fore.CYAN,col,end='      ')       
                elif col=='X':
                    print(Fore.YELLOW,col,end='      ')
                else:
                    print(Fore.RED,col,end='      ') 
    print('\n')

tabla=[
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

'''======================================================================================================='''




def verificarTiros(matriz,x,y):
    '''auxiliar para que la computadora cuales son sus proximos disparos'''
    seguir=True 
    proximosDisparos=[]
    if x>0:
        #print(matriz[x-1][y])
        if  matriz[x-1][y]!='X' and matriz[x-1][y]!='F':

            seguir=False
            proximosDisparos.append([y,x-1])
    if y>0:
        #print(matriz[x][y-1])
        if  matriz[x][y-1]!='X' and matriz[x][y-1]!='F':
            seguir=False
            proximosDisparos.append([y-1,x])
    if  x<9:
        #print(matriz[x+1][y])
        if  matriz[x+1][y]!='X' and matriz[x+1][y]!='F':
            seguir=False
            proximosDisparos.append([y,x+1])
    if y<9:
        #print(matriz[x][y+1])
        if  matriz[x][y+1]!='X' and matriz[x][y+1]!='F':

            seguir=False
            proximosDisparos.append([y+1,x])

    
    return seguir,proximosDisparos


                

def dispararComputadora (matriz,arregloDeDisparos):
    '''La pseudo inteligencia que le meti a la computadora'''
    acertado = False
    for posLista,lista in enumerate (matriz):
            oriana = False #Oriana es una falsa gabo
            for posElemento,elemento in enumerate (lista):
                if elemento=='F':
                    resultados=verificarTiros(matriz,posLista,posElemento)
                    if resultados[0]==False:
                        disparo=random.choice(resultados[1])
                        y=disparo[1]
                        x=disparo[0]
                        oriana = True
                        break
            if oriana:
                break

         
    if oriana==False:
            valido=False
            while valido==False:
                x=random.randint(0,9)
                y=random.randint(0,9)
                coordenadaFinal=[y,x]
                if coordenadaFinal not in arregloDeDisparos:
                    valido = True

                
            


    if matriz[y][x]=='O':
        matriz[y][x]='X'
    elif matriz[y][x]!='X' and matriz[y][x]!='O' and matriz[y][x]!='F':
        matriz[y][x]='F'
        acertado=True
    arregloDeDisparos.append([y,x])
 
    return matriz,arregloDeDisparos,acertado





    
    
    
    
    
    
    






'''======================================================================================================='''

        
def jugar (tabla):
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



    PortaAvion1=barcoJugador(3)
    Buque1=barcoJugador(2)
    Submarino1=barcoJugador(1)

    print('\n');print('A continuacion se muestran las habilidades de los barcos situados en el mapa '.center(120,' '));print('\n')
    
    PortaAvion.habilidad1()
    Buque.habilidad2()
    Submarino.habilidad3()

   

    hundido=0
    repetido=0
    movimientos=0
    puntaje=0
    hundidoComputadora=0
    arregloDeDisparos=[]

    print('A continuacion se presenta su tablarero do   nde pocisionara los barcos');print('\n')
    imprimirTablero(matriz);print('\n')
    print('Los barcos se colocan contiguos hacia la derecha o hacia abajo de la poscion base que elija Nota un barco no se puede colocar contiguo a otro');print('\n')

    

    print(Fore.YELLOW+'IMPORTANTE: el tablero sobre el que disparara es el de color rojo,en cual el enemigo posiciono sus barcos y este le dispara a usted sobre el tablero azul donde  posicionara sus barcos a continucacion , se le pedira la orietacion o dirreccion y luego la coordenada base')
    
    
    


    iniciarTableroJugador(tabla,PortaAvion1,Buque1,Submarino1)
    print('\n')


    iniciarTablarero(matriz,PortaAvion,Buque,Submarino)
    imprimirTablero2(matriz)
    print('\n')


    

    while hundido!=9 and hundidoComputadora!=9:
       
        coordenadaX= pedirCoordenadaX('''
        Ingrese la coordenada en X a la cual desea disparar (coordenada numerica): 
        ''')
        coordenadaY=pedirCoordenadaY('''
        Ingrese la coordenada en Y a la cual desea disparar (coordenada letra): 
        ''')


        datosDisparo=disparar(matriz,coordenadaX,coordenadaY)
        matriz=datosDisparo[0]
        imprimirTablero2(matriz)
        
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

        
        result=dispararComputadora(tabla,arregloDeDisparos)
        tabla=result[0]
        arregloDeDisparos=result[1]
        if result[2]==True:
            hundidoComputadora=hundidoComputadora+1
            print(hundidoComputadora,'--------------')
        imprimirTablero(tabla)




    if hundido==9:
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
    else:
        print ('█'.center(120,'█'));print('\n')
        print(Fore.RED+'''
 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗     
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗    
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝    
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗    
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║    
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝                                                                                                                                  
        ''')
    print('⦿ Total de puntos obtenidos {} '.format(puntaje).center(120,' '))
    print('⦿ Total de disparos {} '.format(movimientos).center(120,' '))
    



    return movimientos,puntaje


