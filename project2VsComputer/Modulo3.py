import colorama
from colorama import Fore, Back, Style




def extraerUsuarios():
    '''Extrae los usuarios de txt y los vacia en un arreglo'''
    todoslosUsuarios=[]
    with open("./BD.txt", "r") as bd:
        todo= bd.readlines()
    for dato in todo:
        perfil = dato[:-1].split(',')
        todoslosUsuarios.append((perfil[0],perfil[1],perfil[2],perfil[3],perfil[4],perfil[5],perfil[6]))
    return todoslosUsuarios



def edadUusuarios():
    '''Saca el rango de edad que se encuentra los usuarios que mas han jugado'''
    todoslosUsuarios=extraerUsuarios()
    rangoEdad=[[5,18,0],[19,45,0],[46,60,0],[61,100,0]]
    for usuario in todoslosUsuarios :
        edad=int(usuario[2])
        for rango in rangoEdad:
            mayor= rango[1]
            menor= rango[0]
            if edad>=menor and edad <= mayor:
                rango[2]=rango[2]+1
                break
    
    lista=sorted(rangoEdad, key=lambda edad:edad[2])  

    if lista[3][2]==lista[2][2]:
        print('''
    ⦿ Los rango de edad en el que estan los usuarios que mas juegan son entre {} - {} anos  y {} - {} anos con un total de {} jugadores
        '''.format(lista[2][0],lista[2][1],lista[3][0],lista[3][1],lista[3][2]))
    else:
        print('''
    ⦿ El rango de edad en el que se encuentran los usuarios que mas juegan es {} y {} anos con un total de {} jugadores
        '''.format(lista[3][0],lista[3][1],lista[3][2]))

        
def puntosXgenero ():
    '''Saca el total de puntos de cada sexo'''
    todoslosUsuarios=extraerUsuarios()
    puntosM=0
    puntosF=0
    for usuario in todoslosUsuarios:
        if usuario[3]=='m':
            puntosM=puntosM+int(usuario[4])
        elif usuario[3]=='f':
            puntosF=puntosF+int(usuario[4])
    print('''
    ⦿ Los puntos de todos los usuarios masculinos del juego es {}
    '''.format(puntosM))
    print('''
    ⦿ Los puntos de todos los usuarios femeninos del juego es {}
    '''.format(puntosF))

def proDisparos():
    '''Saca todos los disparos realizados por los jugadores y las partidas jugadas para obtener el promedio de disparos por partida '''
    todoslosUsuarios=extraerUsuarios()
    disparostotales=0
    partidasJugadas=0
    for usuario in todoslosUsuarios:
        disparostotales=disparostotales+int(usuario[5])
        partidasJugadas=partidasJugadas+int(usuario[6])
        if partidasJugadas==0:
            partidasJugadas=1

    promedio=disparostotales/partidasJugadas
    print('''
    ⦿ El promedio de disparos por partidas es {}
    '''.format(promedio))

def existeTxt():
    '''Verifica que el txt este creado de lo contrario arroja un mensaje'''
    try:
        txt = open('./BD.txt', 'r').readlines()
        existe=True
    except FileNotFoundError:
        print('No hay usuarios en la base de datos')
        existe=False
    return existe



def estadisticas():
    '''Muestra todas las estadisticas del modulo se hace para unificar el llamado en el main'''
    #print ('█'.center(120,'█'));print('\n')
    if existeTxt():
        print(Fore.RED+'''
███████╗███████╗████████╗ █████╗ ██████╗ ██╗███████╗████████╗██╗ ██████╗ █████╗ ███████╗    
██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝██║██╔════╝██╔══██╗██╔════╝    
█████╗  ███████╗   ██║   ███████║██║  ██║██║███████╗   ██║   ██║██║     ███████║███████╗    
██╔══╝  ╚════██║   ██║   ██╔══██║██║  ██║██║╚════██║   ██║   ██║██║     ██╔══██║╚════██║    
███████╗███████║   ██║   ██║  ██║██████╔╝██║███████║   ██║   ██║╚██████╗██║  ██║███████║    
╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝                                                                                                                                                                                    
    ''')
        edadUusuarios()
        puntosXgenero()
        proDisparos()



