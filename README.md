# 1. KineticEnergyProject
Proyecto programación 

# 2. Descripcion
En este proyecto es comnprobar el uso de la energia cinetica y como esta esta afecta a la vida cotidiana,
por ende decidimos crear un preogrma que calcule esta incognita de manera simple y ordenada para todo el publico

# 3. Evento para el objetivo
 # origen 
    - 
 # Formulas a usar
    - La primera formula a usar es:
         Energia Cinetica = 0.5 * masa[Kg] * Velocidad[m/s]^2
 # Resolucion
    - En la formula ingresar los datos de la masa y la velocidades en la formula.
    - La masa de dividra en 2 
    - Al resultado anterior se mutiplicara por el cuadrado de la velocidad 
    - eso dara la energia cinetica aplicada
 # aplicaciones
    - se puede usar para:
       - Transporte: La energía cinética se utiliza en el transporte en forma de vehículos en movimiento. 
                     Por ejemplo, los automóviles, trenes, aviones y bicicletas usan energía cinética para moverse.
                     
       - Industria: En la industria, la energía cinética se utiliza en máquinas y equipos para realizar tareas específicas. 
                    Por ejemplo, en la fabricación, 
                    las máquinas de corte, prensas y robots utilizan la energía cinética para llevar a cabo procesos de producción.
                    
       - Impacto y colisiones: La energía cinética también juega un papel en situaciones de impacto y colisiones. 
                               Por ejemplo, en la ingeniería automotriz, 
                               se estudia la energía cinética para diseñar sistemas de seguridad que minimicen los daños en caso de accidente.
 
 
# 4. Programacion
  # Descrpicion de herramientas
    - Python 3.11.2, es un leguaje de preogramacion
    - Visual Studio Code, es el interprete del lenguaje de programacion 
    - Tkinter, libreria relacionada con el ingreso de datos
    - Git, un repositorio de datos 
    - Git Hub, la pagina web que sirve ver los repocitorios  
   # Guia de instlacion
    - Python 3.11.2: https://www.python.org/downloads/windows/
       - Esto descaragara un instalador el instalador se debe instalar
       - Configuracion predeterminada
    - Visual Studio code: https://code.visualstudio.com/download. 
       - Esto descargara un instalador  
       - Instalar visual studio code
       - Configuracion de defecto
    - Tkinter
       - Esta libreria esta se instala de forma predeterminada en python (no rqwuiere descarga
    - Git
       - Se descargar el instalador 
       - Se instala 
       - Configuracion de defecto
    - Git Hub
       - Se busca git hub en buscador de preferencia
       - se ingresa en el link y se 



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


