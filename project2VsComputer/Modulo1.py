import colorama
from colorama import Fore, Back, Style
from Modulo3 import existeTxt
colorama.init(True)

class Usuario:#Clase para cada usuario que se registra
    def __init__(self, username, nombre, edad, sexo, puntaje = 0,disparos=0,partidas=0):
        self.username = username
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.puntaje = puntaje
        self.disparos =disparos
        self.partidas = partidas

    def __str__(self):#Metodo de impresion de los usuarios
        return'Usuario: {}\nNombre completo: {}\nEdad: {}\nSexo: {}\nPuntaje: {}\nDisparos: {} \nPartidas jugadas: {}'.format(self.username, self.nombre, self.edad, self.sexo,self.puntaje,self.disparos,self.partidas)


def pedirUsername ():
    '''Se encarga de pedir el usuario y validarlo'''
    valido=False
    while valido==False:
        username=input('Ingrese su username, no debe contener espacios y debe ser todo en minuscula: ')
        if ' ' not in username and username.islower()==True and len(username)<30 :
            valido=True
        else:
            print('''
            Usuario invalido
            ''')
    return username

def  pedirNombre ():
    '''Se encarga de pedir el nombre y lo valida'''
    valido=False
    while valido == False:
        nombre=input('Ingrese su nombre completo: ')
        nombreValidar=nombre.replace(" ",'')

        if nombreValidar.isalpha()==True:
            valido=True
        else:
            print('''
            Nombre invalido
            ''')    
    return nombre 

def pedirEdadyNum (messages,edad=False,caracteristica=False):
    '''Se encarga de pedir la edad, la caracteristica eleigida en la funcion modificar usuario y de la del menu principal del juego en el main'''
    valido=False
    while valido==False:
        try:
            num=int(input(messages))
            if edad==True: 
                if num >= 5 and num<=100:
                    valido=True
                else:
                    print('''
                Edad invalida
                ''') 
            elif edad==False and caracteristica==False :
                if num >= 1 and num<=7:
                    valido=True
                else:
                    print('''
                Decision invalida
                ''') 
            elif caracteristica==True:
                if num >= 1 and num<=4:
                    valido=True
                else:
                    print('''
                Decision invalida
                ''') 



        except ValueError:
            print('''
            Invalido, lo ingresado no es un numero
            ''') 
    return num

def pedirSexo():
    '''Pide el sexo de la persona y lo valida'''
    valido=False
    while valido==False:
        sexo=input('Ingrese su sexo, M para masculino y F para femenino: ')
        sexo=sexo.lower()
        if sexo=='m' or sexo=='f' or sexo=='n':
            valido=True
        else:
            print('''
            Sexo invalido, a caso prefiere no decirlo? Ingrese N para sexo indefinido
            ''')
    return sexo 



def verificarUsuario(username):
    '''Verifica si el usuario se encuentra en la base de datos'''
    encontrado=False
    try:
        txt = open('./BD.txt', 'r').readlines()# Otra forma de acceder a un archivo
        for usuario in txt:
            perfil = usuario[:-1].split(',') # [:-1] para quitar el salto de linea
            if perfil[0] == username:
                encontrado=True
                return encontrado
            else:
                encontrado=False
        return encontrado
    except FileNotFoundError:
        print('No hay usuarios en la base de datos')
        return False



def buscarUsuario(username,posicion=False,sexo=False):
    '''Busca el usuario en la base de datos y lo devuelve en un objeto o devuelve su posicion en la base de datos'''
    
    txt = open('./BD.txt', 'r').readlines()
    for pos,perfiles in enumerate (txt):
        usuario = perfiles[:-1].split(',')
        if usuario[0] == username:
            if not posicion:
                return Usuario(usuario[0], usuario[1], usuario[2], usuario[3], int(usuario[4]),usuario[5],usuario[6])
            if posicion:
                return pos
            if sexo==True:
                return usuario[3]


def registrarUsuario():
    '''Registra al usuario en el txt'''

    username = pedirUsername()

    if verificarUsuario(username)==True:
        print('''
        El usuario ingresado ya ha sido registrado
        ''')
        print(buscarUsuario(username))
        return False,username

    nombre = pedirNombre()
    edad = pedirEdadyNum('Ingrese su edad ',True)
    sexo = pedirSexo()
    puntaje=0
    disparos=0
    partidas=0
    usuario = Usuario(username, nombre, edad, sexo, puntaje, disparos)
    
    txt = open('./BD.txt', 'a+')
    txt.write("{},{},{},{},{},{},{}\n".format(username, nombre, edad, sexo,puntaje,disparos,partidas))
    print('\n');print('El usuario {} ha sido registrado correctamente'.format(usuario.username).center(120,'-'));print('\n')
    print('''Perfil del usuario
    Username: {}
    Nombre: {}
    Edad: {}
    Sexo: {} 
    Puntaje maximo: {}
    Disparos: {}
    Partidas: {}'''.format(username,nombre,edad,sexo,puntaje,disparos,partidas))
    
    return True,username

def ver(Top10 = False):
    '''
    Muestra todos los usuarios registrados en el juego o el top 10 de jugadores
    '''
    if existeTxt():
            
        usuarios = []
        txt = open('./BD.txt', 'r')
        todosUsuarios = txt
        for user in todosUsuarios:
            usuario = user[:-1].split(',') # [:-1] para quitar el salto de linea
            usuarios.append(Usuario(usuario[0], usuario[1], usuario[2], usuario[3],int(usuario[4]),usuario[5],usuario[6]))
        ordenados=[]

        if Top10==True:
            ordenados=sorted(usuarios,key=lambda user: user.puntaje, reverse=True)
            print(Fore.RED+'''
████████╗ ██████╗ ██████╗      ██╗ ██████╗     
╚══██╔══╝██╔═══██╗██╔══██╗    ███║██╔═████╗    
   ██║   ██║   ██║██████╔╝    ╚██║██║██╔██║    
   ██║   ██║   ██║██╔═══╝      ██║████╔╝██║    
   ██║   ╚██████╔╝██║          ██║╚██████╔╝    
   ╚═╝    ╚═════╝ ╚═╝          ╚═╝ ╚═════╝     
             ''')
            for i, user in enumerate(ordenados):
                if i<10:
                    print('========= ',i+1,' =========')
                    print(user.username,'/',user.puntaje,'/',user.disparos)

        else:
            print(Fore.RED+'''
██╗   ██╗███████╗███████╗██████╗ ███████╗
██║   ██║██╔════╝██╔════╝██╔══██╗██╔════╝
██║   ██║███████╗█████╗  ██████╔╝███████╗
██║   ██║╚════██║██╔══╝  ██╔══██╗╚════██║
╚██████╔╝███████║███████╗██║  ██║███████║
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝                              
            ''')
            print(
            '''
            Estos son los usuarios registrados actualmente:
            ''')
            for i, user in enumerate(usuarios):
                print('========= ',i+1,' =========')
                print(user)



def modificarUsuario(username,pos):
    '''Modifica cualquiera de las caracteristicas de un usuario registrado'''
    
    if verificarUsuario(username)==True:
        print('''
        ¿Cual caracteristica desea modificar?
        1 - Username
        2 - Nombre
        3 - Edad
        4 - Sexo
        ''')

        caracteristica = pedirEdadyNum('Ingrese la caracteristica que desea modificar',False,True)

        txt = open('./BD.txt', 'r')
        todosUsuarios= txt.readlines()
        usuario = todosUsuarios[pos][:-1].split(',')
        if caracteristica==1:
            usuario[caracteristica - 1]=pedirUsername()
        elif  caracteristica==2:
            usuario[caracteristica - 1]=pedirNombre()
        elif caracteristica==3:
            usuario[caracteristica - 1]=str(pedirEdadyNum('Ingrese la edad: ',True))
        elif caracteristica==4:
            usuario[caracteristica - 1]=pedirSexo()
        modificado = ''
        for i in range(len(usuario)):
            if i != len(usuario) -1:
                modificado = modificado+usuario[i]+','
            else:
                modificado = modificado+usuario[i] + '\n'
        todosUsuarios[pos] = modificado
        with open("./BD.txt", "w") as bd:
            bd.writelines(todosUsuarios)


def editarTxT(username,disparos,puntaje):
    '''Ediata el txt despues del juego escribiendo el puntaje, disparos y suma las partidas jugadas'''
    txt = open('./BD.txt', 'r')
    todosUsuarios= txt.readlines()
    pos=buscarUsuario(username,True,False)
    usuario = todosUsuarios[pos][:-1].split(',')
    
    usuario[4]=str(int(usuario[4])+puntaje)
    usuario[5]=str(int(usuario[5])+disparos)
    usuario[6]=str(int(usuario[6])+1)
    
    modificado=''
    for i in range(len(usuario)):
        if i != len(usuario) -1:
            modificado = modificado+usuario[i]+','
        else:
            modificado = modificado+usuario[i]+'\n' 
    todosUsuarios[pos] = modificado
    with open("./BD.txt", "w") as bd:
        bd.writelines(todosUsuarios)  
        


    




    