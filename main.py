
import tkinter as tk 

Ventana = tk.Tk()
Ventana.geometry('800x640')

Ingreso1 = tk.Entry(Ventana, text ='0')
Ingreso1.pack()

Ingreso2 = tk.Entry(Ventana, text= '1')
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

botonPr = tk.Button(Ventana, text = 'Ingrese masa', command = Formula)
botonPr.pack()

foto = tk.PhotoImage(file = 'fondo.gif')
l = tk.Label(image=foto)
l.pack()


Ventana.mainloop()

