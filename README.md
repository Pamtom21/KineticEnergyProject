# 1. KineticEnergyProject
Proyecto programación 

# 2. Descripcion
Este proyecto se basa en calcular la energia cinetica

# 3. Evento para el objetivo
 # origen 
    -
 # Formulas a usar
    - La primera formula a usar es:
         Energia Cinetica = 0.5 * masa[Kg] * Velocidad[m/s]
 # Resolucion
    - La manera a reslover el problema es apilicar la formula que se utlizo para poder calcular la energia cinetica,
      
 # aplicaciones
    - 
 
 
 
# 4. Programacion
  # Descrpicion de herramientas
    - Python 3.11.2
    - Visual Studio Code 
    - Tkinter
    - Git
    - Git Hub
   # Guia de instlacion
    - Para instalar la version de python utlizado, se requiere ir al la pagina directa de Python: https://www.python.org/downloads/windows/
       esto descaragara un instalador el cual se debe instalar con su configuracion predeterminada
    - Visual Studio code, se instala mediate su pagina web: https://code.visualstudio.com/download. Esto descargara un instalador el 
       cual se debe instalar con su configuracion de defecto
    - Tkinter, esta libreria se instala en el mismo instalador de Python el cual lo tiene agregado
    - Git, es la aplicacion para poder anexar el contenido hecho por los administradores del repocitorio
    - Git Hub, para poder usar git se debe crear una cuenta con la cual se muestra los datos editados por los usuarios 



#---subi un archivo main 

import tkinter as tk 

Ventana = tk.Tk()
Ventana.geometry('800x640')

Ingreso1 = tk.Entry(Ventana, text ='0')
Ingreso1.pack()

Ingreso2 = tk.Entry(Ventana, text= '0')
Ingreso2.pack() 


def Formula():
    try:
        dat1 = float(Ingreso1.get())
        dat2 = float(Ingreso2.get())
        energiaC = (0.5*dat1)
        energiaC1= energiaC*dat2**2
        print(energiaC1)
    except ValueError:
        pass 

botonPr = tk.Button(Ventana, text = 'Calcular', command = Formula)
botonPr.pack()

foto = tk.PhotoImage(file = 'fondo.gif')
l = tk.Label(image=foto)
l.pack()


Ventana.mainloop()
#--- problema al genererar la ventana y escribir algo en la caja de texto, la entrada se duplica

# edite el archivo en la el archivo
#--- arregle el archivo exactamente en la parte de los ingresos

Ingreso1 = tk.Entry(Ventana, text ='0')
Ingreso1.pack()

Ingreso2 = tk.Entry(Ventana, text= '1')
Ingreso2.pack() 

#--- se duplicaba porque tenia el mismo valor


