import os
import time
import msvcrt
contrasenia='1234'
saldo=1000000
j=0
q=0
retiro=0
os.system('cls')
print('-----------------------------------------------------------')
time.sleep(0.5)
print('                        Bienvenido a                       ')
time.sleep(0.5)
print('                       BANCO DE CHILE')
time.sleep(0.5)
print('                     CAJERO AUTOMÁTICO')
time.sleep(0.5)
print('-----------------------------------------------------------')
time.sleep(3)
os.system('cls')
print('Por favor ingrese su tarjeta.')
time.sleep(3)
clave=(input('\n\nIntroduzca la contraseña: '))
time.sleep(2)
os.system('cls')
if len(clave)>4:
    print('\n\n**La contraseña no puede tener más de 4 carateres**')
    time.sleep(2)
    os.system('cls')

elif len(clave)<4:
    print('\n\n**La contraseña no puede tener menos de 4 carateres**')
    time.sleep(2)
    os.system('cls')
else:
    print('...')
    time.sleep(0.5)
    os.system('cls')

if clave==contrasenia:
    print('Contraseña Correcta')
    time.sleep(2)
    os.system('cls')

else:
    intento=2
    while intento==2:
        if intento==2:
            print(f'Contraseña incorrecta intento {intento} de 3')
            time.sleep(1)
            clave=(input('\n\nVuelva a introducir la contraseña: '))
            if len(clave)>4:
                print('\n\n**La contraseña no puede tener más de 4 carateres**')
                time.sleep(2)
                os.system('cls')

            elif len(clave)<4:
                print('\n\n**La contraseña no puede tener menos de 4 carateres**')
                time.sleep(2)
                os.system('cls')
            else:
                print('...')
                time.sleep(0.5)
                os.system('cls')
            intento=intento+1
            time.sleep(2)
            os.system('cls')

            if clave==contrasenia:
                print('Contraseña Correcta')
                time.sleep(2)
                os.system('cls')
                intento=9
            else:
                print(f'Contraseña incorrecta intento {intento} de 3')
                time.sleep(1)
                clave=(input('\n\nVuelva a introducir la contraseña: '))
                if len(clave)>4:
                    print('\n\n**La contraseña no puede tener más de 4 carateres**')
                    time.sleep(2)
                    os.system('cls')

                elif len(clave)<4:
                    print('\n\n**La contraseña no puede tener menos de 4 carateres**')
                    time.sleep(2)
                    os.system('cls')
                else:
                    print('...')
                    time.sleep(0.5)
                    os.system('cls')
                intento=intento+1
                time.sleep(2)
                os.system('cls')

                if clave==contrasenia:
                    print('Contraseña Correcta')
                    time.sleep(2)
                    os.system('cls')
                    intento==9
                
            
                else:
                    print('-----------------------------------------------------------')
                    time.sleep(0.5)
                    print('')
                    time.sleep(0.5)
                    print('        Lo sentimos,se ha bloqueado tu tarjeta. ')
                    time.sleep(0.5)
                    print('')
                    time.sleep(0.5)
                    print('-----------------------------------------------------------')
                    raise SystemExit(0)
                
print('Espere un momento...')
time.sleep(2)
print('\n\nCALCULANDO DATOS DE LA TARJETA...')
time.sleep(4)
print('\n*** PRESIONE CUALQUIER TECLA PARA CONTINUAR ***')
msvcrt.getch()
os.system('cls')
opcion=0
while opcion==0:
    print('Seleccione una opcion (1-5)')
    print('1.Consultar saldo\n2.Giro\n3.Depósito\n4.Transferencia\n5.Salir')
    opcion=int(input())
    if opcion==1:
        opcion=0
        tipo=0
        os.system('cls')
        print('Espere un momento...')
        time.sleep(2)
        while tipo==0:
            os.system('cls')
            print('Seleccione el tipo de cuenta que está operando (1-4):')
            print('1.Cuenta corriente\n2.Cuenta de ahorro\n3.Cuenta vista\n4.Cuenta rut')
            tipo=int(input())

            if tipo==1:
                
                os.system('cls')
                cuenta='Cuenta corriente'
                os.system('cls')
                print('Espere un momento...')
                time.sleep(2)
                os.system('cls')
            elif tipo==2:
                
                os.system('cls')
                cuenta='Cuenta de ahorro'
                os.system('cls')
                print('Espere un momento...')
                time.sleep(2)
                os.system('cls')
                
            elif tipo==3:
                
                os.system('cls')
                cuenta='Cuenta vista'
                os.system('cls')
                print('Espere un momento...')
                time.sleep(2)
                os.system('cls')
            elif tipo==4:
            
                os.system('cls')
                cuenta='Cuenta rut'
                os.system('cls')
                print('Espere un momento...')
                time.sleep(2)
                os.system('cls')
            else:
                tipo=0
                os.system('cls')
                print('**Opción inválida**')
                time.sleep(0.5)
                print('Vuelva a intentarlo')
                time.sleep(0.7)
                os.system('cls')        
        os.system('cls')
        print(f'Su saldo disponible es de ${saldo} pesos ')
        time.sleep(2)
        siono=0
        while siono==0:
            print('\n\n¿Quiere imprimir un comprobante?:')
            print('Seleccione una opción (1-2)')
            print('1.SI\n2.NO')
            siono=int(input())
            if siono==1:
                os.system('cls')
                print('Espere un momento')
                time.sleep(1)
                print('IMPRIMIENDO BOLETA...')
                time.sleep(4)
                print('-------------------------------------------------------')
                time.sleep(0.5)
                print('')
                time.sleep(0.5)
                print('                   BANCO DE CHILE')
                time.sleep(0.5)
                print('')
                time.sleep(0.5)
                print('-------------------------------------------------------')
                time.sleep(0.5)
                print('Fecha          Hora     Cajero      N° Transacción')
                time.sleep(0.5)
                print('30/04/2019     20:00    A2SH6621     2789')
                time.sleep(0.5)
                print('')
                time.sleep(0.5)
                print('NÚMERO DE CUENTA: XXXXXXX2745')
                time.sleep(0.5)
                print(f'{cuenta}')
                time.sleep(0.5)
                print('')
                time.sleep(0.5)
                print(f'SALDO DISPONIBLE: ${saldo}')
                time.sleep(0.5)
                print(f'ÚLTIMO GIRO: ${retiro}')
                time.sleep(0.5)
                print(f'ÚLTIMO DEPÓSITO: ${q}')
                time.sleep(0.5)
                print(f'ÚLTIMA TRANSFERENCIA: ${j}')
                time.sleep(0.5)
                print('')
                time.sleep(0.5)
                print('')
                time.sleep(0.5)
                print('')
                time.sleep(0.5)
                print('-------------------------------------------------------')
                time.sleep(0.5)
                print('')
                time.sleep(0.5)
                print('-------------------------------------------------------')

                time.sleep(3)
                print('*** PRESIONE CUALQUIER TECLA PARA CONTINUAR ***')
                msvcrt.getch()
                os.system('cls')
            elif siono==2:
                os.system('cls')
                print('Espere un momento...')
                time.sleep(1)
                os.system('cls')    
            else:
                siono=0
                os.system('cls')
                print('**Opción inválida**')
                time.sleep(0.5)
                print('Vuelva a intentarlo')
                time.sleep(0.7)
                os.system('cls')



    elif opcion==2:

        opcion=0
        tipo=0
        os.system('cls')
        print('Espere un momento...')
        time.sleep(2)
        while tipo==0:
            os.system('cls')
            print('Seleccione el tipo de cuenta que está operando (1-4):')
            print('1.Cuenta corriente\n2.Cuenta de ahorro\n3.Cuenta vista\n4.Cuenta rut')
            tipo=int(input())

            if tipo==1:
                
                os.system('cls')
                cuenta='Cuenta corriente'
                os.system('cls')
                print('Espere un momento...')
                time.sleep(2)
                os.system('cls')
            elif tipo==2:
                
                os.system('cls')
                cuenta='Cuenta de ahorro'
                os.system('cls')
                print('Espere un momento...')
                time.sleep(2)
                os.system('cls')
                
            elif tipo==3:
                
                os.system('cls')
                cuenta='Cuenta vista'
                os.system('cls')
                print('Espere un momento...')
                time.sleep(2)
                os.system('cls')
            elif tipo==4:
            
                os.system('cls')
                cuenta='Cuenta rut'
                os.system('cls')
                print('Espere un momento...')
                time.sleep(2)
                os.system('cls')
            else:
                tipo=0
                os.system('cls')
                print('**Opción inválida**')
                time.sleep(0.5)
                print('Vuelva a intentarlo')
                time.sleep(0.7)
                os.system('cls')
        giro=''
        retiro=0
        while giro!='9':
            os.system('cls')
            print('Giro automático:')
            print('Seleccione un monto (1-6)')
            print('1.$10.000\n2.$20.000\n3.$30.000\n4.$40.000\n5.$50.000\n6.Otro')
            print('\n\nSeleccione (9) para volver.')
            giro=input()
            if giro in ('1','2','3','4','5','6','9'):

                if giro=='1':
                    retiro=10000
                    saldo_final=saldo-retiro
                    if saldo<retiro:
                        os.system('cls')
                        print('NO SE PUEDE REALIZAR EL GIRO')
                        print('Saldo insuficiente.')
                        time.sleep(2)
                        os.system('cls')
                    else:
                        os.system('cls')
                        print(f'se ha realizado el giro de ${retiro} pesos correctamente.\nsu nuevo saldo disponible es de ${saldo_final} pesos')
                        saldo=saldo_final
                        time.sleep(2)   
                        os.system('cls') 
                elif giro=='2':
                    retiro=20000
                    saldo_final=saldo-retiro
                    if saldo<retiro:
                        os.system('cls')
                        print('NO SE PUEDE REALIZAR EL GIRO')
                        print('Saldo insuficiente.')
                        time.sleep(2)
                        os.system('cls')
                    else:
                        os.system('cls')
                        print(f'se ha realizado el giro de ${retiro} pesos correctamente.\nsu nuevo saldo disponible es de ${saldo_final} pesos')
                        saldo=saldo_final
                        time.sleep(2)
                        os.system('cls')
                elif giro=='3':
                    retiro=30000
                    saldo_final=saldo-retiro
                    if saldo<retiro:
                        os.system('cls')
                        print('NO SE PUEDE REALIZAR EL GIRO')
                        print('Saldo insuficiente.')
                        time.sleep(2)
                        os.system('cls')
                    else:
                        os.system('cls')
                        print(f'se ha realizado el giro de ${retiro} pesos correctamente.\nsu nuevo saldo disponible es de ${saldo_final} pesos')
                        saldo=saldo_final
                        time.sleep(2)
                        os.system('cls')
                elif giro=='4':
                    retiro=40000
                    saldo_final=saldo-retiro
                    if saldo<retiro:
                        os.system('cls')
                        print('NO SE PUEDE REALIZAR EL GIRO')
                        print('Saldo insuficiente.')
                        time.sleep(2)
                        os.system('cls')
                    else:
                        os.system('cls')
                        print(f'se ha realizado el giro de ${retiro} pesos correctamente.\nsu nuevo saldo disponible es de ${saldo_final} pesos')
                        saldo=saldo_final
                        time.sleep(2)
                        os.system('cls')
                elif giro=='5':
                    retiro=50000
                    saldo_final=saldo-retiro
                    if saldo<retiro:
                        os.system('cls')
                        print('NO SE PUEDE REALIZAR EL GIRO')
                        print('Saldo insuficiente.')
                        time.sleep(2)
                        os.system('cls')
                    else:
                        os.system('cls')
                        print(f'se ha realizado el giro de ${retiro} pesos correctamente.\nsu nuevo saldo disponible es de ${saldo_final} pesos')
                        saldo=saldo_final
                        time.sleep(2)
                        os.system('cls')
                elif giro=='6':
                    print('INGRESE LA CANTIDAD QUE DESEA RETIRAR: ')   
                            #retiro = list(range(10000,210000,10000))
                    retiro=int(input('$'))
                    if retiro in (10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000, 160000, 170000, 180000,190000, 200000):
                        saldo_final=saldo-retiro
                        if saldo<retiro:
                            os.system('cls')
                            print('NO SE PUEDE REALIZAR EL GIRO')
                            print('Saldo insuficiente.')
                            time.sleep(2)
                            os.system('cls')
                        else:
                            os.system('cls')
                            print(f'se ha realizado el giro de ${retiro} pesos correctamente.\nsu nuevo saldo disponible es de ${saldo_final} pesos')
                            saldo=saldo_final
                            time.sleep(2)
                            os.system('cls')        
                    elif retiro<10000:
                        os.system('cls')
                        print('El retiro mínimo es de $10.000 pesos')
                        time.sleep(2)
                        os.system('cls')
                        print('Por favor vuelva a intentarlo.')
                        time.sleep(2)
                        os.system('cls')
                    elif retiro>200000:
                        os.system('cls')
                        print('El retiro máximo es de $200.000 pesos')
                        time.sleep(2)
                        os.system('cls')
                        print('Por favor vuelva a intentarlo.')
                        time.sleep(2)
                        os.system('cls')
                    else:
                        os.system('cls')
                        print('Ingrese cantidades de múltiplos de $10.000 pesos')
                        time.sleep(2)
                        os.system('cls')
                        print('Por favor vuelva a intentarlo.')
                        time.sleep(2)
                        os.system('cls')
                else:
                    os.system('cls')
                    print('Espere un momento...')
                    time.sleep(2)
                    os.system('cls')     
                        
            else:
                giro=7
                os.system('cls')
                print('**OPCIÓN NO VALIDA**')
                print('Por favor vuelva a intentarlo.')
                time.sleep(2)
                os.system('cls')
    

    elif opcion==3:
        opcion=0
        tipo=0
        os.system('cls')
        print('Espere un momento...')
        time.sleep(2)
        while tipo==0:
            os.system('cls')
            print('Seleccione el tipo de cuenta que está operando (1-4):')
            print('1.Cuenta corriente\n2.Cuenta de ahorro\n3.Cuenta vista\n4.Cuenta rut')
            tipo=int(input())

            if tipo==1:
                
                os.system('cls')
                cuenta='Cuenta corriente'
                os.system('cls')
                print('Espere un momento...')
                time.sleep(2)
                os.system('cls')
            elif tipo==2:
                
                os.system('cls')
                cuenta='Cuenta de ahorro'
                os.system('cls')
                print('Espere un momento...')
                time.sleep(2)
                os.system('cls')
                
            elif tipo==3:
                
                os.system('cls')
                cuenta='Cuenta vista'
                os.system('cls')
                print('Espere un momento...')
                time.sleep(2)
                os.system('cls')
            elif tipo==4:
            
                os.system('cls')
                cuenta='Cuenta rut'
                os.system('cls')
                print('Espere un momento...')
                time.sleep(2)
                os.system('cls')
            else:
                tipo=0
                os.system('cls')
                print('**Opción inválida**')
                time.sleep(0.5)
                print('Vuelva a intentarlo')
                time.sleep(0.7)
                os.system('cls')        

        d=''
        q=0
        while d!='9':
            os.system('cls')
            print('Depósito automático:')
            print('Seleccione un monto (1-6)')
            print('1.$10.000\n2.$20.000\n3.$30.000\n4.$40.000\n5.$50.000\n6.Otro')
            print('\n\nSeleccione (9) para volver.')
            d=input()
            if d in ('1','2','3','4','5','6','9'):

                if d=='1':
                    q=10000
                    saldo_final=saldo-q
                    if saldo<q:
                        os.system('cls')
                        print('NO SE PUEDE REALIZAR EL DEPÓSITO')
                        print('Saldo insuficiente.')
                        time.sleep(2)
                        os.system('cls')
                    else:
                        os.system('cls')
                        print(f'se ha realizado el depósito de ${q} pesos correctamente.\nsu nuevo saldo disponible es de ${saldo_final} pesos')
                        saldo=saldo_final
                        time.sleep(2)   
                        os.system('cls') 
                elif d=='2':
                    q=20000
                    saldo_final=saldo-q
                    if saldo<q:
                        os.system('cls')
                        print('NO SE PUEDE REALIZAR EL DEPÓSITO')
                        print('Saldo insuficiente.')
                        time.sleep(2)
                        os.system('cls')
                    else:
                        os.system('cls')
                        print(f'se ha realizado el depósito de ${q} pesos correctamente.\nsu nuevo saldo disponible es de ${saldo_final} pesos')
                        saldo=saldo_final
                        time.sleep(2)
                        os.system('cls')
                elif d=='3':
                    q=30000
                    saldo_final=saldo-q
                    if saldo<q:
                        os.system('cls')
                        print('NO SE PUEDE REALIZAR EL DEPÓSITO')
                        print('Saldo insuficiente.')
                        time.sleep(2)
                        os.system('cls')
                    else:
                        os.system('cls')
                        print(f'se ha realizado el depósito de ${q} pesos correctamente.\nsu nuevo saldo disponible es de ${saldo_final} pesos')
                        saldo=saldo_final
                        time.sleep(2)
                        os.system('cls')
                elif d=='4':
                    q=40000
                    saldo_final=saldo-q
                    if saldo<q:
                        os.system('cls')
                        print('NO SE PUEDE REALIZAR EL DEPÓSITO')
                        print('Saldo insuficiente.')
                        time.sleep(2)
                        os.system('cls')
                    else:
                        os.system('cls')
                        print(f'se ha realizado el depósito de ${q} pesos correctamente.\nsu nuevo saldo disponible es de ${saldo_final} pesos')
                        saldo=saldo_final
                        time.sleep(2)
                        os.system('cls')
                elif d=='5':
                    q=50000
                    saldo_final=saldo-q
                    if saldo<q:
                        os.system('cls')
                        print('NO SE PUEDE REALIZAR EL DEPÓSITO')
                        print('Saldo insuficiente.')
                        time.sleep(2)
                        os.system('cls')
                    else:
                        os.system('cls')
                        print(f'se ha realizado el depósito de ${q} pesos correctamente.\nsu nuevo saldo disponible es de ${saldo_final} pesos')
                        saldo=saldo_final
                        time.sleep(2)
                        os.system('cls')
                elif d=='6':
                    print('INGRESE LA CANTIDAD QUE DESEA DEPOSITAR: ')   
                            #retiro = list(range(10000,210000,10000))
                    q=int(input('$'))
                    if q in (10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000, 160000, 170000, 180000,190000, 200000):
                        saldo_final=saldo-q
                        if saldo<q:
                            os.system('cls')
                            print('NO SE PUEDE REALIZAR EL DEPÓSITO')
                            print('Saldo insuficiente.')
                            time.sleep(2)
                            os.system('cls')
                        else:
                            os.system('cls')
                            print(f'se ha realizado el depósito de ${q} pesos correctamente.\nsu nuevo saldo disponible es de ${saldo_final} pesos')
                            saldo=saldo_final
                            time.sleep(2)
                            os.system('cls')        
                    elif q<10000:
                        os.system('cls')
                        print('El depósito mínimo es de $10.000 pesos')
                        time.sleep(2)
                        os.system('cls')
                        print('Por favor vuelva a intentarlo.')
                        time.sleep(2)
                        os.system('cls')
                    elif q>200000:
                        os.system('cls')
                        print('El depósito máximo es de $200.000 pesos')
                        time.sleep(2)
                        os.system('cls')
                        print('Por favor vuelva a intentarlo.')
                        time.sleep(2)
                        os.system('cls')
                    else:
                        os.system('cls')
                        print('Ingrese cantidades de múltiplos de $10.000 pesos')
                        time.sleep(2)
                        os.system('cls')
                        print('Por favor vuelva a intentarlo.')
                        time.sleep(2)
                        os.system('cls')
                else:
                    os.system('cls')
                    print('Espere un momento...')
                    time.sleep(2)
                    os.system('cls')     
                        
            else:
                d=7
                os.system('cls')
                print('**OPCIÓN NO VALIDA**')
                print('Por favor vuelva a intentarlo.')
                time.sleep(2)
                os.system('cls')
        

    elif opcion==4:
        opcion=0
        tipo=0
        os.system('cls')
        print('Espere un momento...')
        time.sleep(2)
        while tipo==0:
            os.system('cls')
            print('Seleccione el tipo de cuenta que está operando (1-4):')
            print('1.Cuenta corriente\n2.Cuenta de ahorro\n3.Cuenta vista\n4.Cuenta rut')
            tipo=int(input())

            if tipo==1:
                
                os.system('cls')
                cuenta='Cuenta corriente'
                os.system('cls')
                print('Espere un momento...')
                time.sleep(2)
                os.system('cls')
            elif tipo==2:
                
                os.system('cls')
                cuenta='Cuenta de ahorro'
                os.system('cls')
                print('Espere un momento...')
                time.sleep(2)
                os.system('cls')
                
            elif tipo==3:
                
                os.system('cls')
                cuenta='Cuenta vista'
                os.system('cls')
                print('Espere un momento...')
                time.sleep(2)
                os.system('cls')
            elif tipo==4:
            
                os.system('cls')
                cuenta='Cuenta rut'
                os.system('cls')
                print('Espere un momento...')
                time.sleep(2)
                os.system('cls')
            else:
                tipo=0
                os.system('cls')
                print('**Opción inválida**')
                time.sleep(0.5)
                print('Vuelva a intentarlo')
                time.sleep(0.7)
                os.system('cls')        
        nombre=''
        apellido=''
        rut =''
        correo=''
        codigo_cuenta='                                                          '
        while len(nombre)<3:
            print('\n--------------TRANSFERENCIA---------------')
            nombre=input('\nINGRESE EL NOMBRE: ')
            os.system('cls')
            if len(nombre)<3:
                print('El nombre no puede tener menos de 3 carácteres')
                time.sleep(2)
                os.system('cls')
        while len(apellido)<3:
            print('\n--------------TRANSFERENCIA---------------')
            apellido=input('\nINGRESE EL APELLIDO: ')

            os.system('cls')
            if len(apellido)<3:
                print('El apellido no puede tener menos de 3 carácteres')
                time.sleep(2)
                os.system('cls')
        while len(rut)<8 or len(rut)>9:
            print('\n--------------TRANSFERENCIA---------------')
            rut=input('\nINGRESE EL RUT: ')
            os.system('cls')
            if len(rut)<8:
                os.system('cls')
                print('El rut no puede tener menos de 8 carácteres')
                time.sleep(2)
                os.system('cls')
            elif len(rut)>9:
                os.system('cls')
                print('El rut no puede tener más de 9 carácteres')
                time.sleep(2)
                os.system('cls')
            else:
                print('')
        print('--------------TRANSFERENCIA---------------')

        banco=input('\nINGRESE EL NOMBRE DEL BANCO: ')
        os.system('cls')
        while len(correo)<6:
            print('\n--------------TRANSFERENCIA---------------')
            correo=input('\nINGRESE EL CORREO ELECTRÓNICO: ')
            os.system('cls')
            if len(correo)<6:
                print('El correo no puede tener menos de 6 carácteres')
                time.sleep(2)
                os.system('cls')
        print('\n--------------TRANSFERENCIA---------------')
        tipo_cuenta=input('\nINGRESE EL TIPO DE CUENTA: ')
        os.system('cls')
        while len(codigo_cuenta)>11:
            print('\n--------------TRANSFERENCIA---------------')
            codigo_cuenta=input('\nINGRESE EL NÚMERO DE CUENTA: ')
            os.system('cls')
            if len(codigo_cuenta)>11:
                print('El número de cuenta no puede tener más de 11 carácteres')
                time.sleep(2)
                os.system('cls')
        t=''
        j=0
        while t!='9':
            os.system('cls')
            print('Transferencia automática:')
            print('Seleccione un monto (1-6)')
            print('1.$10.000\n2.$20.000\n3.$30.000\n4.$40.000\n5.$50.000\n6.Otro')
            print('\n\nSeleccione (9) para volver.')
            t=input()
            if t in ('1','2','3','4','5','6','9'):

                if t=='1':
                    j=10000
                    saldo_final=saldo-j
                    if saldo<j:
                        os.system('cls')
                        print('NO SE PUEDE REALIZAR LA TRANSFERENCIA')
                        print('Saldo insuficiente.')
                        time.sleep(2)
                        os.system('cls')
                    else:
                        os.system('cls')
                        print(f'se ha realizado la transferencia de ${j} pesos correctamente.\nsu nuevo saldo disponible es de ${saldo_final} pesos')
                        saldo=saldo_final
                        time.sleep(2)   
                        os.system('cls') 
                elif t=='2':
                    j=20000
                    saldo_final=saldo-j
                    if saldo<j:
                        os.system('cls')
                        print('NO SE PUEDE REALIZAR LA TRANSFERENCIA')
                        print('Saldo insuficiente.')
                        time.sleep(2)
                        os.system('cls')
                    else:
                        os.system('cls')
                        print(f'se ha realizado la transferencia de ${j} pesos correctamente.\nsu nuevo saldo disponible es de ${saldo_final} pesos')
                        saldo=saldo_final
                        time.sleep(2)
                        os.system('cls')
                elif t=='3':
                    j=30000
                    saldo_final=saldo-j
                    if saldo<j:
                        os.system('cls')
                        print('NO SE PUEDE REALIZAR LA TRANSFERENCIA')
                        print('Saldo insuficiente.')
                        time.sleep(2)
                        os.system('cls')
                    else:
                        os.system('cls')
                        print(f'se ha realizado la transferencia de ${j} pesos correctamente.\nsu nuevo saldo disponible es de ${saldo_final} pesos')
                        saldo=saldo_final
                        time.sleep(2)
                        os.system('cls')
                elif t=='4':
                    j=40000
                    saldo_final=saldo-j
                    if saldo<j:
                        os.system('cls')
                        print('NO SE PUEDE REALIZAR LA TRANSFERENCIA')
                        print('Saldo insuficiente.')
                        time.sleep(2)
                        os.system('cls')
                    else:
                        os.system('cls')
                        print(f'se ha realizado la transferencia de ${j} pesos correctamente.\nsu nuevo saldo disponible es de ${saldo_final} pesos')
                        saldo=saldo_final
                        time.sleep(2)
                        os.system('cls')
                elif t=='5':
                    j=50000
                    saldo_final=saldo-j
                    if saldo<j:
                        os.system('cls')
                        print('NO SE PUEDE REALIZAR LA TRANSFERENCIA')
                        print('Saldo insuficiente.')
                        time.sleep(2)
                        os.system('cls')
                    else:
                        os.system('cls')
                        print(f'se ha realizado la transferencia de ${j} pesos correctamente.\nsu nuevo saldo disponible es de ${saldo_final} pesos')
                        saldo=saldo_final
                        time.sleep(2)
                        os.system('cls')
                elif t=='6':
                    print('INGRESE LA CANTIDAD QUE DESEA TRANSFERIR: ')   
                            #retiro = list(range(10000,210000,10000))
                    j=int(input('$'))
                    if j in (10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000, 160000, 170000, 180000,190000, 200000):
                        saldo_final=saldo-j
                        if saldo<j:
                            os.system('cls')
                            print('NO SE PUEDE REALIZAR LA TRANSFERENCIA')
                            print('Saldo insuficiente.')
                            time.sleep(2)
                            os.system('cls')
                        else:
                            os.system('cls')
                            print(f'se ha realizado la transferencia de ${j} pesos correctamente.\nsu nuevo saldo disponible es de ${saldo_final} pesos')
                            saldo=saldo_final
                            time.sleep(2)
                            os.system('cls')        
                    elif j<10000:
                        os.system('cls')
                        print('La transferencia mínima es de $10.000 pesos')
                        time.sleep(2)
                        os.system('cls')
                        print('Por favor vuelva a intentarlo.')
                        time.sleep(2)
                        os.system('cls')
                    elif j>200000:
                        os.system('cls')
                        print('La transferencia máxima es de $200.000 pesos')
                        time.sleep(2)
                        os.system('cls')
                        print('Por favor vuelva a intentarlo.')
                        time.sleep(2)
                        os.system('cls')
                    else:
                        os.system('cls')
                        print('Ingrese cantidades de múltiplos de $10.000 pesos')
                        time.sleep(2)
                        os.system('cls')
                        print('Por favor vuelva a intentarlo.')
                        time.sleep(2)
                        os.system('cls')
                else:
                    os.system('cls')
                    print('Espere un momento...')
                    time.sleep(2)
                    os.system('cls')     
                            
            else:
                t=7
                os.system('cls')
                print('**OPCIÓN NO VALIDA**')
                print('Por favor vuelva a intentarlo.')
                time.sleep(2)
                os.system('cls')
        

        

    elif opcion==5:
        os.system('cls')
        print('Usted a finalizado la operación.')
        time.sleep(2)
        os.system('cls')
        print('\n\nPorfavor retire su tarjeta.')
        time.sleep(3)
        os.system('cls')
        print('-----------------------------------')
        time.sleep(0.5)
        print('                                   ')
        time.sleep(0.5)
        print('         ¡Vuelva pronto!           ')
        time.sleep(0.5)
        print('                                   ')
        time.sleep(0.5)
        print('-----------------------------------')
        time.sleep(2)
        os.system('cls')
        raise SystemExit(0)

    else:
        opcion=0
        print('Introduzca una opción valida')
        time.sleep(2)
        os.system('cls')




        




