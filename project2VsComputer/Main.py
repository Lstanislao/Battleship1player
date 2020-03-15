from vscomputadora import jugar
from Modulo3 import estadisticas, existeTxt
from Modulo1 import*

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

def main():
    print(Fore.BLUE +'''
▀█████████▄     ▄████████     ███         ███      ▄█          ▄████████    ▄████████    ▄█    █▄     ▄█     ▄███████▄ 
  ███    ███   ███    ███ ▀█████████▄ ▀█████████▄ ███         ███    ███   ███    ███   ███    ███   ███    ███    ███ 
  ███    ███   ███    ███    ▀███▀▀██    ▀███▀▀██ ███         ███    █▀    ███    █▀    ███    ███   ███▌   ███    ███ 
 ▄███▄▄▄██▀    ███    ███     ███   ▀     ███   ▀ ███        ▄███▄▄▄       ███         ▄███▄▄▄▄███▄▄ ███▌   ███    ███ 
▀▀███▀▀▀██▄  ▀███████████     ███         ███     ███       ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀▀███▀  ███▌ ▀█████████▀  
  ███    ██▄   ███    ███     ███         ███     ███         ███    █▄           ███   ███    ███   ███    ███        
  ███    ███   ███    ███     ███         ███     ███▌    ▄   ███    ███    ▄█    ███   ███    ███   ███    ███        
▄█████████▀    ███    █▀     ▄████▀      ▄████▀   █████▄▄██   ██████████  ▄████████▀    ███    █▀    █▀    ▄████▀      
                                                  ▀                                                                     ''')
    seguir=True 
    while seguir==True:
        print('  Menu de Inicio  '.center(120,'█'));print('\n')
        print('1- Registrar usuario e iniciar partida '.center(120,' '))
        print('2- Iniciar partida con usuario registrado'.center(120,' '))
        print('3- Editar Usuario'.center(120,' '))
        print('4- Ver usuarios registrados'.center(120,' '))
        print('5- Ver top 10 de jugadores'.center(120,' '))
        print('6- Ver estadisticas'.center(120,' '))
        print('7- Salir'.center(120,' '));print('\n')
        print ('█'.center(120,'█'));print('\n')
        decision=pedirEdadyNum('Ingrese una de las opciones: ',False);print('\n'); print ('█'.center(120,'█'));print('\n')

        if decision==1:
            hacer=registrarUsuario()
            username=hacer[1]
            registrado=hacer[0]
            if registrado==True:
                resultados=jugar(tabla)
                disparos=resultados[0]
                puntaje=resultados[1]
                editarTxT(username,disparos,puntaje)
                print(buscarUsuario(username))
                
        if decision==2:
            username=pedirUsername();print('\n')
            if verificarUsuario(username)==True:
                print('Perfil del usuario ingresado:');print('\n')
                print(buscarUsuario(username))
                resultados=jugar(tabla)
                disparos=resultados[0]
                puntaje=resultados[1]
                editarTxT(username,disparos,puntaje)
                print(buscarUsuario(username))
            else:
                print('''
                Ese usuario no ha sido registrado o lo ha escrito mal, a continuacion ingrese la opcion 1 para registrar el usuario 
                    ''')
        if decision==3:
            if existeTxt():
                username=pedirUsername()
                pos=buscarUsuario(username,True)
                print('El usuario a modificar es ')
                print(buscarUsuario(username))
                modificarUsuario(username,pos)
        if decision==4:
            ver()
        if decision==5:
            ver(True)
        if decision==6:
            estadisticas()
        if decision==7:
            print('Gracias por jugar, vuelva pronto'.center(120,' '))
            seguir=False

main()





            


