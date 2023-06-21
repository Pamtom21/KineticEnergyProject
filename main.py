
import tkinter as tk 



Ventana = tk.Tk()
Ventana.geometry('320x320')
Ventana.title('Energia Cinetica')
Ventana.configure(background= 'dark slate blue')



Ingreso1 = tk.Entry(Ventana, text ='0')
Ingreso1.pack()

Ingreso2 = tk.Entry(Ventana, text= '1')
Ingreso2.pack() 


def Formula():
    try:
        dat1 = float(Ingreso1.get())
        dat2 = float(Ingreso2.get())
        energiaC = (0.5*dat1)*dat2**2
        resultado = tk.Label(Ventana,text= 'La energia es : '+str(energiaC))
        resultado.pack()
        print(energiaC)
    except ValueError:
        pass 

botonPr = tk.Button(Ventana, text = 'Ingrese masa', command = Formula)
botonPr.pack()





Ventana.mainloop()

