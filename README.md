# 1. KineticEnergyProject
Proyecto programación 

# 2. Descripcion
Este proyecto se basa en calcular la energia  

# 3. Evento para el objetivo
 -
 -
 -
 -
# 4. Programacion
  # Descrpicion de herramientas
    - Python 3.11.2
    - Visual Studio Code 
    - Tkinter
    - Git
   # Guia de instlacion
    - Para instalar la version de python utlizado, se requiere ir al la pagina directa de Python: https://www.python.org/downloads/windows/
       esto descaragara un instalador el cual se debe instalar con su configuracion predeterminada
    - Visual Studio code se instala mediate su pagina web: https://code.visualstudio.com/download. Esto descargara un instalador el 
       cual se debe instalar con su configuracion de defecto
    - 
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


