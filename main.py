
import tkinter as tk
from tkinter import messagebox

Ventana = tk.Tk()
Ventana.geometry('320x320')
Ventana.title('Energia Cinetica')
Ventana.configure(background= 'dark slate blue')


Ingreso1 = tk.Entry(Ventana, text ='1')#
Ingreso1.place(x=92,y=40)


Ingreso2 = tk.Entry(Ventana, text= '2')#.place(x=92,y=40)
Ingreso2.place(x=92,y=90) 


def Formula():
    try:
        dat1 = float(Ingreso1.get())
        dat2 = float(Ingreso2.get())
        energiaC = (0.5*dat1)*dat2**2
        resultado = tk.Label(Ventana,text= 'La energia es : '+str(energiaC)+' Joule')#.place(x=92,y=170)
    
        print(energiaC)
    except ValueError:
        pass
        Cajaemergente= messagebox.showerror('Error', 'Coloque numeros')
        Cajaemergente.pack()

botonPr = tk.Button(Ventana, text = 'Ingrese masa', command = Formula).place(x=110,y=130)
#botonPr.pack()
#if botonPr == True:
#    resultado.replace(x=92,y=170)





Ventana.mainloop()

