#---------Importaciones-------------------------------------------
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from vuelos import vuelos3 as vuelos1
from ListaAsientos import asientos2
import json
from tkinter import DISABLED
import time
from PIL import Image, ImageTk 
#--------------Variables globales--------------------

barra = 0
seleccion = 0
seleccion2 = 0
num2 = 0
barra2= 0
numero = 0
verify = 0
pasajeros = 0
premiumON = 0
num4 = 0
num_pasajeros = 0
prem = 0
codigos_vuelos = 0
ori = 0
des = 0
asientosSC = []
compra5 = 0
ap = 0
nom = 0
codigo_boleto = 0
horaS = 0
fechaV = 0
numero_pasajeros = 0
rangomax = 0
seleccion_asiento = 0
seleccion4 = 0
añadidos = []
codeffff = 0
asiento_elegido = 0
asiento_elegido2 = 0
icono = "FENIX-ARWAYS-02.ico"
botones_generados = 0
codigoV = 0
subir_asiento = []
codigos_vuelos = 0

#--------------Ventana chek in--------------------------#

def chekin():
    global icono
    global subir_asiento
    subir_asiento = []
    window1 = Toplevel()
    window1.title("Fenix Airways")
    window1.resizable(0,0)
    window1.geometry("650x650")
    #-----------Centro de la ventana--------#
    centro = (650-200)//2
    #----------Logo de la aerolinea---------#
    logo = Image.open("FENIX ARWAYS 01.png")
    logo = logo.resize((200, 250), Image.LANCZOS)
    logo1 = ImageTk.PhotoImage(logo)
    window1.logo_image = logo1
    mostrar7 = Label(window1, image=logo1)
    mostrar7.place(x=centro,y=80)
    #--Icono de la aplicacion
    window1.iconbitmap(icono)
    #----------Codigo----------
    code = Label(window1, text="Codigo")
    code.place(x=253,y=370, width=155, height=30)
    code1 = Entry(window1, bg="silver") 
    code1.place(x=249,y=400, width=160, height=30)
    #--------Apellido-----------
    apellido = Label(window1,text="Apellido")
    apellido.place(x=253,y=430, width=155,height=30)
    apellido1 = Entry(window1, bg="silver") #ENTRADA DEL APELLIDO
    apellido1.place(x=249, y=450, width=160,height=30)
    #----------Boton 1------------
    boton1 = Button(window1,text="Presionar", command=lambda:comprobar(comp,apellido1,code1,window1)) #BOTON
    boton1.place(x=253,y=500, width=150,height=40)
    boton1.bind('<Enter>', lambda e: e.widget.config(bg='gray'))
    boton1.bind('<Leave>', lambda e: e.widget.config(bg='white'))

#-------------Resultado chek in--------------------------#

def resultado_checkin(imprimir_datos):
    global icono
    abordaje = Toplevel()
    abordaje.geometry("900x300")
    abordaje.resizable(0,0)
    abordaje.config(bg="silver")
    barra_izquierda = Frame(abordaje,width=90,bg="red")
    barra_izquierda.pack(side="left",fill="y")
    texto1 = Label(barra_izquierda,text="Fenix Arways")
    #--------icono---------#
    abordaje.iconbitmap(icono)
    #--------------------#
    barra_superior = Frame(abordaje,height=70,bg="orange")
    barra_superior.pack(side="top",fill="x")
    deco1 = Label(barra_superior,text="Pase de abordaje",
                  font=("Helvetica",20),fg="white",bg="orange")
    deco1.pack(padx=5,pady=5)
    #------------------Imprimir nombre------------------#
    deco2 = Label(abordaje,text="Nombre pasajero", bg="silver")
    deco2.place(x=158,y=80)
    mostrar1 = Label(abordaje, text=imprimir_datos[0:2],font=50, bg="silver")
    mostrar1.place(x=150,y=100)
    #------------------Origen y destino-----------------#
    #-Origen
    mostrar2 = Label(abordaje,text=imprimir_datos[3],font=("Helvetica",10), bg="silver")
    mostrar2.place(x=150,y=160)
    deco3 = Label(abordaje,text="Ciudad de origen", bg="silver")
    deco3.place(x=150,y=140)
    #-Destino
    mostrar3 = Label(abordaje, text=imprimir_datos[4],font=("Helvetica", 10), bg="silver")
    mostrar3.place(x=150,y=220)
    deco4 = Label(abordaje,text="Ciudad de destino", bg="silver")
    deco4.place(x=150,y=200)
    #-Codigo vuelo
    deco5 = Label(abordaje,text="Codigo del vuelo", bg="silver")
    deco5.place(x=390,y=80)
    mostrar4 = Label(abordaje,text=imprimir_datos[2],font=("Helvetica",10), bg="silver")
    mostrar4.place(x=390,y=100)
    #-Asiento
    deco6 = Label(abordaje,text="Asiento", bg="silver")
    deco6.place(x=390,y=140)
    mostrar5 = Label(abordaje,text=imprimir_datos[7],font=("Helvetica",10), bg="silver")
    mostrar5.place(x=390,y=160)
    #-Fecha
    deco8 = Label(abordaje,text="Fecha del vuelo", bg="silver")
    deco8.place(x=390,y=200)
    mostrar8 = Label(abordaje,text=imprimir_datos[6], font=("Helvetica",10), bg="silver")
    mostrar8.place(x=390,y=220)

#--------------Base de datos (codigos) ---------------------------

def comprobar(comp,apellido1,code1,window1):
    global verify
    num = 0
    code2 = code1.get()
    apellido2 = apellido1.get()
    if code2 in datos_pasajeros:
        if apellido2 in datos_pasajeros[code2]:
            print("Funciona")
            imprimir_datos = datos_pasajeros[code2]
            resultado_checkin(imprimir_datos)
        else:
            advertencia4 = messagebox.showwarning("ADVERTENCIA","APELLIDO NO VALIDO")
    else:
        advertencia3 = messagebox.showwarning("ADVERTENCIA","CODIGO NO VALIDO")
    if num == 1:
        pagina_principal.destroy()
        
#-----------Pagina de registro/origen/destino/pasajeros---------------

def programa():
    global icono
    global subir_asiento
    #---Configuraciones ventana---#
    pagina = Toplevel()
    pagina.geometry("1000x650")
    pagina.resizable(0,0)
    pagina.title("Fenix Arways")
    menu1 = Menu(pagina)
    pagina.config(menu=menu1)
    #---Reinicio---#
    subir_asiento = []
    #--------Icono---------#
    pagina.iconbitmap(icono)
    #-----Decoracion-----#
    dec3 = Image.open("banner 01.png")
    dec3 = dec3.resize((1200,200), Image.LANCZOS)
    deco3 = ImageTk.PhotoImage(dec3)
    mostrar10 = Label(pagina,image=deco3)
    mostrar10.image = deco3
    mostrar10.place(x=-150,y=470)
    dec4 = dec3.rotate(180)
    deco4 = ImageTk.PhotoImage(dec4)
    mostrar11 = Label(pagina,image=deco4)
    mostrar11.image = deco4
    mostrar11.place(x=-20,y=0)
    dec5 = Image.open("05.png")
    dec5 = dec5.resize((800,250), Image.LANCZOS)
    deco5 = ImageTk.PhotoImage(dec5)
    mostrar11 = Label(pagina,image=deco5)
    mostrar11.image = deco5
    mostrar11.place(x=100,y=220)
    #--------Menu de destinos-------
    barra = StringVar()
    origen2 = ttk.Combobox(pagina,value=origen, state="readonly", textvariable=barra)
    mensaje2 = Label(pagina, text="Ciudad de origen")
    origen2.config(width=30)
    barra2 = StringVar()
    destinos3 = ttk.Combobox(pagina,value=origen, state="readonly", textvariable=barra2)
    destinos3.config(width=30)
    mensaje13 = Label(pagina,text="Ciudad de destino")
    #---------Numero de pasajeros-------#
    comprobar3 = pagina.register(solo_numeros)
    pasajeros = Entry(pagina,validate="key",validatecommand=(comprobar3,"%S"))
    mensaje14 = Label(pagina,text="Numero de personas")
    #----Boton de filtro-----#
    confirmar = Button(pagina, text='Confirmar',command=lambda: destino1(barra,barra2,pagina,pasajeros,confirmar))
    confirmar.config(width=20,height=2)
    confirmar.place(x=430,y=400)
    #-------Posicion---------#
    origen2.place(x=150,y=300)
    mensaje2.place(x=205,y=275)
    mensaje13.place(x=450,y=275)
    mensaje14.place(x=704,y=230)
    destinos3.place(x=400, y=300)
    pasajeros.place(x=700,y=260)
    
    

def destino1(barra,barra2,pagina,pasajeros,confirmar):
    global num_pasajeros
    global ori
    global des
    seleccion = barra.get()
    seleccion2 = barra2.get()
    ori = barra.get()
    des = barra2.get()
    try:
     num_pasajeros = int(pasajeros.get())
     if num_pasajeros < 72:
         if seleccion == "Bogota":
            seleccion = bogota
            fecha_valor(seleccion,seleccion2,pagina)
         elif seleccion == "Cali":
            seleccion = cali
            fecha_valor(seleccion,seleccion2,pagina)
         elif seleccion == "Cartagena":
            seleccion = cartagena
            fecha_valor(seleccion,seleccion2,pagina)
         elif seleccion == "Santa Marta":
            seleccion = marta
            fecha_valor(seleccion,seleccion2,pagina)
         elif seleccion == "Medellin":
            seleccion = medellin
            fecha_valor(seleccion,seleccion2,pagina)
         else:
             mensaje4 = messagebox.showwarning("ADVERTENCIA","RELLENE TODAS LAS CASILLAS")
         confirmar.destroy()
     else:
         mensaje3 = messagebox.showwarning("Advertencia",
                              "El numero que a ingresado excede el limite de pasajeros")
    except:
        mensaje5 = messagebox.showwarning("ADVERTENCIA","RELLENE TODAS LAS CASILLAS")
    
#-----------filtro de fechas------------------#

def fecha_valor(seleccion,seleccion2,pagina):
    fechas = []
    for i in range(len(seleccion)):
        if seleccion2 == seleccion[i][8]:
            fechas.append(seleccion[i][1])
    barra3 = StringVar()
    fechas2 = ttk.Combobox(pagina,width=20,value=fechas,state="readonly",textvariable=barra3)
    fechas2.place(x=692,y=300)
    buscar = Button(pagina, text= "Buscar vuelo", command=lambda: programa2(pagina,barra3,seleccion,seleccion2))
    buscar.config(width=20,height=2)
    buscar.place(x=430,y=400)

#-----------Segunda pagina-----------------#

def programa2(pagina,barra3,seleccion,seleccion2):
    global icono
    fecha = barra3.get()
    pagina.destroy()
    opciones = []
    pagina2 = Toplevel()
    pagina2.geometry("1000x650")
    pagina2.resizable(0,0)
    pagina2.title("Fenix Arways")
    #---icono---#
    pagina2.iconbitmap(icono)
    #---Decoracion---#
    dec6 = Image.open("banner 02.png")
    dec6 = dec6.resize((1000,200),Image.LANCZOS)
    deco6 = ImageTk.PhotoImage(dec6)
    mostrar15 = Label(pagina2,image=deco6)
    mostrar15.image = deco6
    mostrar15.place(x=0,y=450)
    volver = Button(pagina2, text= "Regresar", command=lambda: boton_volver(pagina2))
    volver.pack()
    for i in range(len(seleccion)):
        if seleccion2 == seleccion[i][8] and fecha == seleccion[i][1]:
            opciones.append(seleccion[i])
    print(opciones)
    generador_botones(opciones,pagina2)



def generador_botones(opciones,pagina2):
    global codigos_vuelos
    global num_pasajeros
    global botones_generados
    botones_generados = []
    num5 = 0
    final = num_pasajeros + len(codigos_vuelos[opciones[0][0]])
    for k in range(len(opciones)):
        if len(codigos_vuelos[opciones[k][0]]) <= 72 and final <= 72:
          
          botons = Button(pagina2, text=f"{opciones[k][1]}-{opciones[k][2]}-{opciones[k][3]}"
                        , command=lambda k=k:precios(opciones,pagina2,k,filtro1,filtro2))
          botons.config(width=50,height=2)
          botons.pack()
          botones_generados.append(botons)

          num5 += 1
        else:
            print("vuelo lleno")
    if num5 == 0:
        mensaje2 = Label(pagina2,text="""NO HAY VUELOS DISPONIBLES 
                     O NO HAY CUPOS SUFICIENTES PARA EL NUMERO DE PASAJEROS INGRESADOS
                         """)
        mensaje2.pack()
    else:
      filtro2 = Button(pagina2,text="Filtrar de mayor a menor precio",command=lambda:state1(opciones,pagina2,filtro1,filtro2))
      filtro1 = Button(pagina2,text="Filtrar de menor a mayor precio",command=lambda:state2(opciones,pagina2,filtro1,filtro2))
      #filtro2.config(state="disabled")
      filtro1.place(x=800,y=100)
      filtro2.place(x=800,y=50)

#-----Define el boton que fue seleccionado-----#

def state1(opciones,pagina2,filtro1,filtro2):
    filtro(opciones,pagina2,filtro1,filtro2,estado=1)



def state2(opciones,pagina2,filtro1,filtro2):
    filtro(opciones,pagina2,filtro1,filtro2,estado=2)

#-----Genera los botones de forma ordenada y de acuerdo al boton presionado----#

def filtro(opciones,pagina2,filtro1,filtro2,estado):
    global botones_generados
    val = []
    tot = []
    for i in range(len(opciones)):
        val.append(opciones[i][4])
    #--define el orden de los vuelos dependiendo del estado
    if estado == 2:
       val = sorted(val)
       filtro1.config(state="disabled")
       filtro2.config(state="normal")
    elif estado == 1:
        val = sorted(val,reverse=True)
        filtro2.config(state="disabled")
        filtro1.config(state="normal")
    print(val)

    for i in range(len(opciones)):
        for k in range(len(val)):
            if val[i] == opciones[k][4]:
                tot.append(opciones[k])
    #----Destruir botones generados---#
    for b in botones_generados:
        b.destroy()
    opciones = tot
    #--Se reinicia la lista de botones--#
    botones_generados = []
    #----Genera los nuevos botones----#
    for k in range(len(opciones)):
        botons = Button(pagina2, text=f"{opciones[k][1]}-{opciones[k][2]}-{opciones[k][3]}"
                        , command=lambda k=k:precios(opciones,pagina2,k,filtro1,filtro2))
        botons.config(width=50,height=2)
        botons.pack()
        botones_generados.append(botons)
    


def precios(opciones,pagina2,k,filtro1,filtro2):
    global botones_generados
    #---Decoracion fondo---#
    dec7 = Image.open("fondo texto.jpg")
    dec7 = dec7.resize((180,170),Image.LANCZOS)
    deco7 = ImageTk.PhotoImage(dec7)
    #------Precios del vuelo (min,med,max)------------#
    seleccion3 = opciones[k]
    precio1 = Button(pagina2, text="Seleccionar",command= lambda:aluminio(seleccion3,pagina2))
    precio1_1 = Label(pagina2,image=deco7, text=f"""
    Aluminio
  Precio:{opciones[k][4]}
  1 articulo personal(bolso)
  1 equipaje de mano(10kg)
  [Desde $195.100 COP]
  Equipaje de bodega(23kg)
  [Desde $175.600 COP]
  Asiento Economy
  (Aleatorio-Aluminio)
                      """
                      ,fg="white",compound="center")
    #----------------------------------------#
    precio2 = Button(pagina2, text=f"Seleccionar",command= lambda:compra(seleccion3,pagina2))
    precio2_2 = Label(pagina2,image=deco7, text=f"""
    Diamante
   Precio:{opciones[k][5]}
   1 articulo personal(bolso)
   1 equipaje de bodega(23kg)
   1 equipaje de mano(10kg)
   Asienyo Economy
  (Filas especificas disponibles
   de manera aleatoria)
                      """
                      ,fg="white",compound="center")
    #-----------------------------------------#
    precio3 = Button(pagina2, text=f"Seleccionar",command=lambda:premium(seleccion3,pagina2))

    precio3_3 = Label(pagina2,image=deco7,text=f"""
    Premium: {opciones[k][6]}
   1 articulo personal(bolso)
   1 equipaje de mano(10kg)
   1 equipaje de bodega(23kg)
   Asiento Plus
                      """
                      ,fg="white",compound="center")
    precio3_3.image = deco7
    #------Tamaño---------#
    precio1.config(width=20,height=2)
    precio1_1.config(width=180,height=170)
    #--------------------#
    precio2.config(width=20,height=2)
    precio2_2.config(width=180,height=170)
    #--------------------#
    precio3.config(width=20,height=2)
    precio3_3.config(width=180,height=170)
    #------Posicion-------#
    precio1.place(x=220,y=250)
    precio1_1.place(x=200,y=300)
    #---------------------#
    precio2.place(x=420,y=250)
    precio2_2.place(x=400,y=300)
    #---------------------#
    precio3.place(x=620,y=250)
    precio3_3.place(x=600,y=300)
    #----Desactivar filtros---#
    filtro1.config(state="disabled")
    filtro2.config(state="disabled")
    #----Regreso----#
    precios_lista = [precio1,precio1_1,precio2,precio2_2,precio3,precio3_3]
    for b in botones_generados:
        b.config(state="disabled")
    regreso3 = Button(pagina2,text="Regresar",command=lambda:boton_regreso2(precios_lista,regreso3,filtro1,filtro2))
    regreso3.place(x=450,y=500)



def boton_regreso2(presios_lista,regreso3,filtro1,filtro2):
    global botones_generados
    for i in presios_lista:
        i.destroy()
    regreso3.destroy()
    for b in botones_generados:
        b.config(state="normal")
    filtro1.config(state="normal")
    filtro2.config(state="normal")



def compra(seleccion3,pagina2):
    global premiumON
    global prem
    global ori
    global des
    global compra5
    global horaS
    global fechaV
    global rangomax
    global seleccion4
    global codeffff
    global icono
    global subir_asiento
    print(subir_asiento)
    seleccion4 = seleccion3
    print(f"Error:  {seleccion4} ")
    compra1 = Toplevel()
    compra1.geometry("750x400")
    compra1.resizable(0,0)
    compra1.title("Fenix Arways")
    #-------Icono---------#
    compra1.iconbitmap(icono)
    #---------------------#
    pagina2.destroy()
    if premiumON == 1:
        prem = Button(compra1,text="Seleccionar asiento",bg="gold",command= lambda:pag_asientos(seleccion3))
        prem.place(x=317,y=310)
        precio = seleccion3[4]
    elif premiumON == 2:
        mensaje3 = Label(compra1,text="No puede elegir asiento")
        mensaje3.pack()
        rangomax = asientos2[0:4]
        precio = seleccion3[4]
    else:
        mensaje3 = Label(compra1,text="No puede elegir asiento")
        mensaje3.pack()
        rangomax = asientos2[4:8]
        precio = seleccion3[5]
    compra5 = f"""

Hora salida           Hora llegada
                               {seleccion3[2]}-----------{seleccion3[3]}        Precio: {precio*num_pasajeros}
{ori}                    {des}  

 """
    mensaje4 = Label(compra1,text=compra5, bg="silver")
    mensaje4.config(width=50,height=3)
    mensaje4.pack()
    confirmar2 = Button(compra1,text="Seleccionar",command=lambda:registro(compra1))
    centro = Frame(compra1)
    centro.pack(expand=True)
    confirmar2.pack(side=BOTTOM, pady=20)  
    centro.pack_propagate(False)
    centro.config(width=800)
    horaS = seleccion3[2]
    fechaV = seleccion3[1]
    codeffff = seleccion3[0]



def asignacion_aleatoria():
    global num_pasajeros
    global codigo_boleto
    global rangomax
    global seleccion4
    global asiento_elegido
    global subir_asiento
    codigo_boleto = seleccion4[0]
    codigoB = seleccion4[0]
    selec = []
    while True:
        asientoR = random.choice(rangomax)
        asientoF = random.choice(asientoR)
        if asientoF in selec:
            print("repetir")
        else:
            selec.append(asientoF)
            subir_asiento.append(asientoF)
            break
        print(asientoF)
    
    asiento_elegido = asientoF

#-----------Rango Aluminio------------#

def aluminio(seleccion3,pagina2):
    global premiumON
    premiumON = 2
    compra(seleccion3,pagina2)

#------------Rango premium------------#

def premium(seleccion3,pagina2):
    global premiumON
    premiumON = 1
    compra(seleccion3,pagina2)

#--------------Boton de regreso---------------#

def boton_volver(pagina2):
    pagina2.destroy()
    programa()

#--------------Destinos-----------------------#

def destinos2():
    bogota = []
    cali = []
    marta = []
    cartagena = []
    medellin = []
    a9 = []
    for i in range(0,len(vuelos1)):
        if vuelos1[i][7] == 'Bogota':
            bogota.append(vuelos1[i])
        elif vuelos1[i][7] == 'Cali':
            cali.append(vuelos1[i])
        elif vuelos1[i][7] == 'Cartagena':
            cartagena.append(vuelos1[i])
        elif vuelos1[i][7] == 'Medellin':
            medellin.append(vuelos1[i])
        elif vuelos1[i][7] == 'Santa Marta':
            marta.append(vuelos1[i])
        else:
            a9.append(vuelos1[i])
            
#--------------Registrarse-----------------

def registro(compra1):
    global icono
    compra1.destroy()
    registro1 = Toplevel()
    registro1.geometry("500x600")
    registro1.resizable(0,0)
    registro1.title("Fenix Arways")
    #--------Icono---------#
    registro1.iconbitmap(icono)
    #---Decoracion---#
    dec23 = Image.open("01.png")
    dec23 = dec23.resize((530,150),Image.LANCZOS)
    deco23 = ImageTk.PhotoImage(dec23)
    mostrar25 = Label(registro1,image=deco23)
    mostrar25.image = deco23
    mostrar25.place(x=-20,y=0)
    #--
    dec24 = dec23.rotate(180)
    deco24 = ImageTk.PhotoImage(dec24)
    mostrar26 = Label(registro1,image=deco24)
    mostrar26.image = deco24
    mostrar26.place(x=-20,y=450)
    #--
    dec25 = Image.open("05.png")
    dec25 = dec25.resize((480,300),Image.LANCZOS)
    deco25 = ImageTk.PhotoImage(dec25)
    mostrar26 = Label(registro1,image=deco25)
    mostrar26.image = deco25
    mostrar26.place(x=10,y=150)
    #-------Seleccionar genero------------
    gn = ["Hombre","Mujer","Otro"]
    generos = StringVar()
    genero = OptionMenu(registro1, generos, *gn)
    genero.place(x=50,y=193)
    m1 = Label(registro1, text="Genero")
    m1.place(x=51,y=170)
    #-------Leer nombre y apellido------------#
    nombre = Entry(registro1, bg="silver")
    nombre.place(x=150,y=200)
    m2 = Label(registro1,text="Primer nombre")
    m2.place(x=155,y=177)
    apellido_1 = Entry(registro1, bg="silver")
    apellido_1.place(x=300,y=200)
    m3 = Label(registro1,text="Primer apellido")
    m3.place(x=305,y=177)
    #-------Nacionalidad-----------------#
    nacionalidad = Entry(registro1, bg="silver")
    nacionalidad.place(x=300,y=250)
    m4 = Label(registro1,text="Nacionalidad")
    m4.place(x=305,y=227)
    #-------fecha de nacimiento----------#
    dia = []
    dia1 = StringVar()
    mes = []
    mes1 = StringVar()
    año = []
    año1 = StringVar()
    for i in range(1,31+1):
        dia.append(i)
    for i in range(1,12+1):
        mes.append(i)
    for i in range(1924,2024):
        año.append(i)
    #----------Boton de dias---------#
    selec_dia = ttk.Combobox(registro1, width=16,values=dia,state="readonly",textvariable=dia1)
    selec_dia.place(x=20,y=350)
    m5 = Label(registro1,text="Dia de nacimiento")
    m5.place(x=22,y=327)
    #----------Boton meses-----------#
    selec_mes = ttk.Combobox(registro1, width=16,values=mes,state="readonly",textvariable=mes1)
    selec_mes.place(x=155,y=350)
    m6 = Label(registro1,text="Mes de nacimiento")
    m6.place(x=160,y=327)
    #----------Años------------------#
    selec_año = ttk.Combobox(registro1, width=16,values=año,state="readonly",textvariable=año1)
    selec_año.place(x=305,y=350)
    m7 = Label(registro1,text="Año de nacimiento")
    m7.place(x=310,y=327)
    #-----------Telefono-----------------#
    comprobar2 = registro1.register(solo_numeros)
    telefono = Entry(registro1,validate="key",validatecommand=(comprobar2,"%S"))
    telefono.place(x=150,y=300)
    m8 = Label(registro1,text="Telefono")
    m8.place(x=155,y=277)
    #-----------Correo electronico-----------#
    correo = Entry(registro1)
    correo.place(x=300,y=300)
    m9 = Label(registro1,text="Correo electronico")
    m9.place(x=305,y=277)
    #-----Identificacion-----#
    identificacion = Entry(registro1,validate="key",validatecommand=(comprobar2,"%S"))
    identificacion.config(width=43)
    identificacion.place(x=20,y=250)
    m10 = Label(registro1,text="Numero de identificacion")
    m10.place(x=50,y=225)
    #------------Asistencia?-----------------#
    boleano = ["Si","No"]
    opciones = StringVar()
    asistencia = ttk.Combobox(registro1,width=16,values=boleano,state="readonly",textvariable=opciones)
    asistencia.place(x=20,y=300)
    m11 = Label(registro1,text="Necesita asistencia?")
    m11.place(x=22,y=277)
    #-----------Verificar datos---------------#
    verificar = Button(registro1,text="Confirmar",command=lambda:datosVF(nombre,apellido_1,telefono,correo,registro1,compra1))
    verificar.place(x=210,y=400)



def solo_numeros(char):
    return char.isdigit()



def datosVF(nombre,apellido_1,telefono,correo,registro1,compra1):
    global ap
    global nom
    global numero_pasajeros
    global premiumON
    global seleccion_asiento
    global subir_asiento
    if len(nombre.get()) > 0 and len(apellido_1.get()) > 0:
     val1 = 0
     valT = 0
     errores = []
     codigosCOL = ["300","301","302","303",
                  "304","320","321","322",
                  "310","311","312","313",
                  "314","315","316","318",
                  "319","350","351"]
     codigo2 = ""
     numeroCOL = telefono.get()
     contador = 0
     for i in numeroCOL:
         codigo2 += i
         contador += 1 
         if contador == 3:
             break
     if codigo2 in codigosCOL and len(numeroCOL) == 10:
         val1 += 2
     if val1 == 2:
         valT += 1
     else:
         errores.append("Numero telefonico invalido")
     correo1 = correo.get()
     dominios = ["@gmail.com","@hotmail.com","@outlook.com",
                "@yahoo.com","@icloud.com","@mac.com","@me.com",
                "@live.com","@msn.com","@protonmail.com","@pm.me",
                "@zoho.com","@aol.com","@mail.com","@email.com",
                "@yandex.com","@gmx.com","@tutanota.com","@fastmail.com",
                "@hushmail.com",
                ]
     correoV = ["cuenta:"]
     for i in range(len(correo1)):
         if correo1[i] == "@":
             correoV[0] = correo1[i:]
     if correoV[0] in dominios:
         valT += 1
    #---Registra los datos y verifica si todo esta correcto---#
     ap = apellido_1.get()
     nom = nombre.get()
     if valT == 2:
          registro1.destroy()
          boleto()
          if seleccion_asiento == 0:
            asignacion_aleatoria()
          numero_pasajeros += 1
          if numero_pasajeros == num_pasajeros:
              datos_tarjeta()
          else:
              registro(compra1)
     else:
         advertencia2 = messagebox.showwarning("ADVERTENCIA","CORREO O TELEFONO NO VALIDO")
    else:
        mensaje20 = messagebox.showwarning("ADVERTENCIA","RELLENE TODOS LOS ESPACIOS")

#----------Datos de la targeta----------#

def datos_tarjeta(): #Pagina donde se deben ingresar los datos de la tarjeta
    global compra5
    global icono
    datos = Toplevel()
    datos.geometry("500x500")
    datos.resizable(0,0)
    datos.title("Fenix Arways")
    #---------icono-------#
    datos.iconbitmap(icono)
    #-----Decoracion----#
    dec11 = Image.open("03.png")
    dec11 = dec11.resize((520,150),Image.LANCZOS)
    deco11 = ImageTk.PhotoImage(dec11)
    mostrar21 = Label(datos,image=deco11)
    mostrar21.image = deco11
    mostrar21.place(x=0,y=0)
    dec12 = Image.open("banner 01.png")
    dec12 = dec12.resize((550,150),Image.LANCZOS)
    deco12 = ImageTk.PhotoImage(dec12)
    mostrar22 = Label(datos,image=deco12)
    mostrar22.image = deco12
    mostrar22.place(x=-60,y=350)
    #---------------------#
    m17 = Label(datos,text="Numero de tarjeta")
    m17.place(x=100,y=177)
    tarjeta = Entry(datos,width=20)
    ccvE = StringVar()
    maxL = 3
    ccvE.trace("w",lambda *args: limite(ccvE,maxL,*args))
    ccv = Entry(datos,width=5,textvariable=ccvE)
    m18 = Label(datos,text="CCV")
    m18.place(x=300,y=223)
    ccv.place(x=300,y=250)
    tarjeta.place(x=100,y=200)
    m19 = Label(datos,text="Nombre titular")
    m19.place(x=100,y=123)
    nombreT = Entry(datos,bg="silver")
    nombreT.place(x=100,y=150)
    mesEX = []
    añoEX = []
    añoS = StringVar()
    mesS = StringVar()
    for i in range(1,12+1):
        mesEX.append(i)
    for i in range(2024,2050):
        añoEX.append(i)
    selecA = ttk.Combobox(datos,width=10,values=añoEX,state="readonly",textvariable=añoS)
    selecM = ttk.Combobox(datos,width=10,values=mesEX,state="readonly",textvariable=mesS)
    selecA.place(x=100,y=250)
    selecM.place(x=200,y=250)
    m20 = Label(datos,text="Fecha de caducidad")
    m20.place(x=130,y=225)
    compraF = Label(datos,text=compra5,bg="silver")
    compraF.config(width=50,height=3)
    compraF.place(x=100,y=300)
    pagar = Button(datos,text="Pagar",command=lambda:pago(tarjeta,datos,ccv))
    pagar.config(width=20,height=2)
    pagar.place(x=200,y=400)
    
#-----Limite de numeros en el ccv-------#

def limite(ccvE,maxL,*args):
    limiteC = ccvE.get()
    if len(limiteC) > maxL:
        ccvE.set(limiteC[:maxL])

#-----------Verificar pago y generar codigo check in----------#

def pago(tarjeta,datos,ccv):
    global añadidos
    global asiento_elegido2
    global codigoV
    global subir_asiento
    global codigos_vuelos
    print(subir_asiento)
    for i in range(len(subir_asiento)):
        codigos_vuelos[codigoV].append(subir_asiento[i])
    num_t = tarjeta.get()
    num_c = ccv.get()
    if len(num_t) == 16 and len(num_c) == 3:
        datos.destroy()
        with open(comp3, 'w') as dats:
          json.dump(datos_pasajeros, dats, indent=4)
    #--------------Guardar asientos-------------------#
        with open(comp2, 'w') as codes:
          json.dump(codigos_vuelos, codes, indent=4)
        codigos_mostrar = Toplevel()
        codigos_mostrar.geometry("500x500")
        codigos_mostrar.resizable(0,0)
        codigos_mostrar.title("Fenix Arways")
        for i in range(len(añadidos)):
            mensaje5 = Label(codigos_mostrar,text=añadidos[i])
            mensaje5.pack()
    else:
        advertencia = messagebox.showwarning("ADVERTENCIA","TARJETA O CCV NO VALIDO")

#-----------------Codigo check in---------------#

def boleto():
    global codeffff
    global ap
    global nom
    global ori
    global des
    global horaS
    global fechaV
    global añadidos
    global asiento_elegido
    global numero_pasajeros
    global subir_asiento
    print(codeffff)
    if premiumON == 1:
        asiento_elegido = subir_asiento[numero_pasajeros]
    #--------------Codigo alfanumerico------------#
    inicial = ""
    codigoalf = ""
    for i in nom:
        inicial += i.upper()
        break
    letras = ["A","B","C","D","E","F","G",
              "H","I","J","K","L","M","N",
              "O","P","Q","R","S","T","U",
              "V","W","X","Y","Z"]
    numeros = ["1","2","3","4","5","6","7","8","9","0"]
    cod = [letras,numeros]
    validacion = ["L","N"]
    #Valida que el codigo alfanumerico tenga letras y numeros 
    #y que el codigo no exista anteriormente en la base de datos
    while True:
        for i in range(0,6):
          d1 = random.choice(cod)
          d2 = random.choice(d1)
          codigoalf += d2 
        for i in codigoalf:
            if i in letras:
                validacion[0] = "Hay letras"
            elif i in numeros:
                validacion[1] = "Hay numeros"
        if validacion[0] == "Hay letras" and validacion[1] == "Hay numeros":
            codigo_final = f"{inicial}-{codigoalf}"
            if codigo_final in datos_pasajeros:
                print("repetir")
            else:
                break
        else:
            print("repetir")
    #-----------------Diseño del ticket----------------------#
    datos_pasajero = []
    datos_añadir = [nom,ap,codeffff,ori,des,horaS,fechaV,asiento_elegido]
    datos_pasajeros[codigo_final] = datos_añadir
    añadidos.append(f"Nombre: {nom} {ap}   Codigo de reserva: {codigo_final}")
    
#--------------Seleccion de asientos-------------#

def pag_asientos(seleccion3):
    global seleccion_asiento
    global codigoV
    global codigos_vuelos
    global icono
    codigoV = seleccion3[0]
    pagina3 = Toplevel()
    pagina3.geometry("400x430")
    pagina3.resizable(0,0)
    pagina3.title("Fenix Arways")
    #---icono---#
    pagina3.iconbitmap(icono)
    #---Decoracion---#
    dec9 = Image.open("banner 05.png")
    dec9 = dec9.resize((400,430),Image.LANCZOS)
    deco9 = ImageTk.PhotoImage(dec9)
    mostrar17 = Label(pagina3,image=deco9)
    mostrar17.image = deco9
    mostrar17.place(x=0,y=0)
    #---Labels---#
    l1 = Label()
    for r in range(0,len(asientos2)):
        print(asientos2[r])
        for a in range(len(asientos2[r])):
            if asientos2[r][a] in codigos_vuelos[codigoV]:
                asiento = Button(pagina3,text=f"{asientos2[r][a]}",command=asiento_ocupado)
                asiento.config(width= 2,height=1,bg="red")
                asiento.grid(row=r, column=a, padx=5, pady=5)
            else:
              ast = asientos2[r][a]
              asiento = Button(pagina3,text=f"{asientos2[r][a]}")
              asiento.config(width= 2,height=1)
              asiento["command"] = lambda ast=ast, asiento=asiento: obtener_asiento(ast, pagina3, asiento)
              asiento.grid(row=r, column=a, padx=5, pady=5)
    seleccion_asiento = 5
    
            

def obtener_asiento(ast,pagina3,asiento):
    global num4
    global num_pasajeros
    global prem
    global asientosSC
    global asiento_elegido2
    global subir_asiento
    num4 += 1
    num5 = int(num_pasajeros)
    subir_asiento.append(ast)
    print(ast)
    asiento.config(state=DISABLED)
    asiento_elegido2 = ast
    if num4 == num5:
        pagina3.destroy()
        prem.destroy()
    


def asiento_ocupado():
    print("asiento ocupado")



def regreso2(seleccion3):
    global asientosSC
    global codigos_vuelos
    codigoD = seleccion3[0]
    for i in range(0,len(codigos_vuelos[codigoD])):
        if codigos_vuelos[codigoD][i] in asientosSC:
            codigos_vuelos[codigoD].remove(i)

#--------------Entry point--------------------

if __name__=='__main__':
    num = 0
    #---------Archivos txt------------#
    comp = fr"datos1.txt"
    comp2 = fr"codigos_vuelos.json"
    comp3 = fr"datos_pasajeros.json"
    #---------------------------------#
    pagina_principal = Tk()
    pagina_principal.geometry("1200x600")
    pagina_principal.resizable(0,0)
    pagina_principal.title("Fenix Arways")
    #-------Logo-------#
    logo2 = Image.open("FENIX ARWAYS 01.png")
    logo2 = logo2.resize((200, 250), Image.LANCZOS)
    logo3 = ImageTk.PhotoImage(logo2)
    pagina_principal.logo2_image = logo3
    mostrar7 = Label(pagina_principal, image=logo3)
    mostrar7.place(x=500,y=40)
    #---------Icono---------#
    pagina_principal.iconbitmap(icono)
    #---------Decoraciones de la ventana-----#
    #---Barra de abajo---#
    dec1 = Image.open("01.png")
    dec1 = dec1.rotate(180)
    dec1 = dec1.resize((1220,250), Image.LANCZOS)
    deco1 = ImageTk.PhotoImage(dec1)
    mostrar8 = Label(pagina_principal, image=deco1)
    mostrar8.image = deco1
    mostrar8.place(x=-10,y=350)
    #---Barra de arriba---#
    dec2 = Image.open("02.png")
    dec2 = dec2.rotate(180)
    deco2 = ImageTk.PhotoImage(dec2)
    mostrar9 = Label(pagina_principal,image=deco2)
    mostrar9.place(x=-250,y=-30)
    #---------Boton de registro------------#
    boton_registro = Button(pagina_principal,text="Registrarse",command=programa)
    boton_registro.configure(width=20, height= 2)
    boton_registro.place(x=450,y=300)
    #---------Boton chek in----------------#
    boton_chekin = Button(pagina_principal,text="Check in",command=chekin)
    boton_chekin.configure(width=20, height= 2)
    boton_chekin.place(x=600,y=300)
    #-----------Destinos-------------------#
    bogota = []
    cali = []
    marta = []
    cartagena = []
    medellin = []
    a9 = []
    for i in range(0,len(vuelos1)):
        if vuelos1[i][7] == 'Bogota':
            bogota.append(vuelos1[i])
        elif vuelos1[i][7] == 'Cali':
            cali.append(vuelos1[i])
        elif vuelos1[i][7] == 'Cartagena':
            cartagena.append(vuelos1[i])
        elif vuelos1[i][7] == 'Medellin':
            medellin.append(vuelos1[i])
        elif vuelos1[i][7] == 'Santa Marta':
            marta.append(vuelos1[i])
        else:
            a9.append(vuelos1[i])
    origen = ["Bogota","Cali","Cartagena","Medellin","Santa Marta"]
    #--------------Lista de vuelos y acientos ocupados------------------#
    with open(comp2, "r") as codes:
        codigos_vuelos = json.load(codes)
    print(type(codigos_vuelos))
    #------------------------------------#
    with open(comp3,"r") as dats:
        datos_pasajeros = json.load(dats)
    #-----------------------------------#
    pagina_principal.mainloop()