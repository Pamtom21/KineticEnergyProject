# Las librerias que se importan
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from tkinter import messagebox

# Funcion principal de la ventana que se genera
Ventana = Tk()

# Ancho y alto de la ventana
Ventana.geometry('900x500')

# Nombre de la ventana 
Ventana.title('Energia Cinetica ')

# Color de la ventana
Ventana.configure(background= 'dark slate blue')

# Una etiqueta de la masa
Label(Ventana, text="Ingrese Masa(kg)").place(x=450,y=170)

# Barra de entrada de datos respecto a la masa
n1 = Entry(Ventana, text ='1', bd=4) 

# La posicion en la ventana en la que coloca en la ventana
n1.place(x=432,y=200)

# Una etiqueta de la velocidad
Label(Ventana, text="Ingrese Velocidad(m/s)").place(x=667,y=170)

# Barra de entrada de datos respecto a la velocidad
n2 = Entry(Ventana, text= '2', bd=4)

# La posicion en la ventana en la que coloca en la ventana
n2.place(x=667,y=200) 
# Etquetas respecto al tiempo
ulala=Label(Ventana, text="Tiempo en Segundos")
Car=Label(Ventana, text="Tiempo en Segundos")

# Etiqueta respecto al posible desplazamiento
li=Label(Ventana, text="Escala en metros")

# Etiqueta de metro entre segundos
ta=Label(Ventana, text="M/S")

# Entradas de datos respecto al tiempo
n3 = Entry(Ventana, text= '3', bd=4) # Tiempo 1
n4 = Entry(Ventana, text='4', bd=4)  # Tiempo 2

# Entrada de datos para la distancia
n5 = Entry(Ventana, text='5', bd=4) #

# Funcion principal de la calculadora
def resolver(*_):
    # Datos ingresado de la masa
    a= n1.get()
    # Datos ingresados de velocidad
    b= n2.get()#

    # Verifca si hubo una entrada de datos
    if not (a:= n1.get()) or not (b:= n2.get()):
        return
    
    # Transfora los datos obtenidoa a decimales
    try:
        a, b = float(a), float(b)

    # Si entran letras
    except ValueError:

        res.set("ERROR")
        # Lo ignora
        pass

        # Genera un error si los datos ingresados son letras
        Cajaemergente= messagebox.showerror('Error', 'Coloque numeros')
        Cajaemergente.pack()

    # El ultimo caso
    else:
        # Impresion de la formula en la ventana
        E = res.set(str(0.5*a*(b**2))) 

# Boton 'tipo casilla'
def opciones():
    
    # si la opcion 1 es activada
    if seleccion.get() == 1:
        texto.place(x=62, y=170)
    
    # si la opcion 1 es Desactivada
    else:
        texto.place_forget()
    
    # si la opcion 2 es activada
    if seleccion.get() == 2:
        texto1.place(x=100, y=150)
    
    # si la opcion 2 es Desactivada
    else:
        texto1.place_forget()
    
    # si la opcion 3 es activada
    if seleccion.get() == 3:
        texto2.place(x=80, y=170)
    
    # si la opcion 3 es Desactivada
    else:
        texto2.place_forget()
    
    # si la opcion 4 es activada
    if seleccion.get() == 4:
        ulala.place(x=150,y=200)
        n3.place(x=143,y=230)
        botonGRAF.place(x=180,y=265)
    
    # si la opcion 4 es Desactivada 
    else:
        ulala.place_forget()
        n3.place_forget()
        ulala.place_forget()
        botonGRAF.place_forget()
    
    # si la opcion 5 es activada
    if seleccion.get() == 5:
        Car.place(x = 75, y = 200)
        n4.place(x = 70,y = 230)
        li.place(x = 250, y = 200)
        n5.place(x = 230,y = 230)
        botonCV.place(x =184.5,y = 315)
        ta.place(x = 312 , y = 270)
        resVelo1.place(x = 145, y = 270)
    
    # si la opcion 5 es Desactivada
    else:
        n4.place_forget()
        Car.place_forget()
        n5.place_forget()
        li.place_forget()
        botonCV.place_forget()
        ta.place_forget()
        resVelo1.place_forget()

# funcion que grafica 
def graficar():
        # Masa   
        a= n1.get()

        # Velocidad
        b= n2.get()
        # Tiempo 1
        t= n3.get()
        # Tiempo 1 de str a int
        t1 = int(t)
        # Ingreso de datos float
        try:
          a, b = float(a), float(b)
        # Si se ingresan letra error
        except ValueError:
            pass
            Cajaemergente= messagebox.showerror('Error', 'Coloque numeros')
            Cajaemergente.pack()
        # Formula
        F = int(0.5*a*(b**2))
        
        # Hace un rango que parte desde el -5 , la varible F y lo escala en 0.05
        x = np.arange(-5,F,0.05)
        # Genera la 'osiclacion' en el grafico
        x2 = np.cos(x)
        # Arreglo que que empieza desde el 0, llega a t1 y se escala con la longitud de x
        y = np.linspace(0, t1, len(x))
        # Hace el grafico
        plt.plot(y,x2)
        # Variable x 
        plt.xlabel("Tiempo")
        # Variable y
        plt.ylabel("Energia cientica")
        plt.title("Gráfico respecto a la Energia C y el tiempo")
        # Muestra el grafico 
        plt.show() 


# Calculadora de velocidad
def CalVelo():
    # Escala de metros (desplazamiento)
    t = n4.get()
    # Tiempo 2
    d = n5.get()
    # Si se ingresan datos
    try:
        d,t = float(d), float(t)
    #  Si se ingresan letras
    except ValueError:
        # Ignorar
        pass
        # mensaje de error
        Cajaemergente= messagebox.showerror('Error', 'Coloque numeros')
        Cajaemergente.pack()
    # Impresion de la formula en la ventana
    g = resVelo.set(str(d/t))
       

# Texto de la opcion 1
texto = Label(Ventana, text='Si se aplica una fuerza y se transfiere energia \n y no hay resistencias \n la energia se transforma en cinetica ', font="Arial 11")
# Texto de la opcion 2
texto1 = Label(Ventana, text= ' Energia cinetica \n1/2 x m x v^2', font='Arial 20')
# Texto de la opcion 3
texto2 = Label(Ventana, text='En un pendulo, en los vehiculos, \n maquinas (de corte, prensas, etc), \n accidentes automovilisticos ', font= "Arial 13")
# Genera botones tipo 'casillas'
seleccion = IntVar()
# Genera el boton de calcular el grafico
botonGRAF = Button(Ventana, text = 'Graficar', command = graficar, bd=5 )
# Hace la etiqueta de las opciones
Label(Ventana, text="Opciones", font='Arial 15').place(x=165,y=35)
# Muestra los botones de tipo 'casilla'
botonPr = Radiobutton(Ventana, text = 'Orígen', value=1, variable=seleccion, command = opciones).place(x=70,y=70)
botonPr = Radiobutton(Ventana, text = 'Fórmula', value=2, variable=seleccion, command =  opciones).place(x=130,y=70)
botonPr = Radiobutton(Ventana, text = 'Aplicaciones', value=3, variable=seleccion, command = opciones ).place(x=200,y=70)
botonPr = Radiobutton(Ventana, text = 'Grafico', value=4, variable=seleccion, command = opciones).place(x=295,y=70)
botonPr = Radiobutton(Ventana, text = 'Velocidad', value=5, variable=seleccion, command = opciones).place(x=170,y= 94)
# Mustra una barra de ingreso pero solo en str
res = StringVar()
resVelo = StringVar()
# Barra de entrada del calculo de la velocidad 
resVelo1 = Entry(Ventana, justify="center", textvariable=resVelo, state="disabled", bd=8)
# Etiquetas
Label(Ventana, text="Calculadora E.C", font= 'Arial 16').place(x=535,y=110)
Label(Ventana, text="La energia cinetica es (Joule) ").place(x=534,y=260)
# Barra de entrada del calculo de la energia cinetica
Entry(Ventana, justify="center", textvariable=res, state="disabled", bd=7).place(x=546,y= 290)
# Boton principal del calculo de la energia cinetica
botonPrC = Button(Ventana, text = 'Calcular', command = resolver, bd=5 ).place(x=585,y=330)
# Boton para calcular la velocidad
botonCV = Button(Ventana, text = 'Calcular', command = CalVelo, bd=6 )

# Muestra todo en pantalla
Ventana.mainloop()
