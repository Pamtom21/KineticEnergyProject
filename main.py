#aqui se subira todo
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from tkinter import messagebox

Ventana = Tk()
Ventana.geometry('900x500')
Ventana.title('Energia Cinetica')
Ventana.configure(background= 'dark slate blue')

Label(Ventana, text="Ingrese Masa(kg)").place(x=450,y=170)
n1 = Entry(Ventana, text ='1', bd=4)#masa
n1.place(x=432,y=200)

Label(Ventana, text="Ingrese Velocidad(m/s)").place(x=667,y=170)
n2 = Entry(Ventana, text= '2', bd=4)#velocidad
n2.place(x=667,y=200) 
ulala=Label(Ventana, text="Tiempo s")
n3 = Entry(Ventana, text= '3', bd=4)#tiempo



def resolver(*_):
    a= n1.get()#masa
    b= n2.get()#velocidad

    if not (a:= n1.get()) or not (b:= n2.get()):
        return
    try:
        a, b = float(a), float(b)

    except ValueError:
        res.set("ERROR")
        pass
        Cajaemergente= messagebox.showerror('Error', 'Coloque numeros')
        Cajaemergente.pack()
    else: 
        E = res.set(str(0.5*a*(b**2))) 


def opciones():
    if seleccion.get() == 1:
        texto.place(x=100, y=150)
    else:
        texto.place_forget()

    if seleccion.get() == 2:
        texto1.place(x=100, y=150)
    else:
        texto1.place_forget()

    if seleccion.get() == 3:
        texto2.place(x=100, y=150)
    else:
        texto2.place_forget()
    
    if seleccion.get() == 4:
        ulala.place(x=100,y=200)
        n3.place(x=100,y=230)
        botonGRAF.place(x=100,y=330) 
    else:
        texto2.place_forget()
        n3.place_forget()
        ulala.place_forget()
        botonGRAF.place_forget()

def graficar():
        a= n1.get()#masa
        b= n2.get()#velocidad
        t= n3.get()
        t1 = int(t)
        try:
          a, b = float(a), float(b)
        except ValueError:
            pass
            Cajaemergente= messagebox.showerror('Error', 'Coloque numeros')
            Cajaemergente.pack()
        F = int(0.5*a*(b**2))
        x = np.arange(-5,F,3)
        x2 = np.cos(x)
        y = np.linspace(0, t1, len(x))
        plt.plot(y,x2)
        plt.show() 
       


texto = Label(Ventana, text='')
texto1 = Label(Ventana, text= 'Energia cinetica \n 1/2 x m x v^2', font='Arial 20')
texto2 = Label(Ventana, text='')
seleccion = IntVar()
botonGRAF = Button(Ventana, text = 'Graficar', command = graficar, bd=5 )
Label(Ventana, text="Opciones", font='Arial 15').place(x=165,y=35)
botonPr = Radiobutton(Ventana, text = 'Orígen', value=1, variable=seleccion, command = opciones).place(x=70,y=70)
botonPr = Radiobutton(Ventana, text = 'Fórmula', value=2, variable=seleccion, command =  opciones).place(x=130,y=70)
botonPr = Radiobutton(Ventana, text = 'Aplicaciones', value=3, variable=seleccion, command = opciones ).place(x=200,y=70)
botonPr = Radiobutton(Ventana, text = 'Grafico', value=4, variable=seleccion, command = opciones).place(x=295,y=70)
res = StringVar()
Label(Ventana, text="Calculadora E.C", font= 'Arial 16').place(x=535,y=110)
Label(Ventana, text="La energia cinetica es: ").place(x=553,y=260)
Entry(Ventana, justify="center", textvariable=res, state="disabled", bd=7).place(x=546,y= 290)
botonPrC = Button(Ventana, text = 'CALCULAR', command = resolver, bd=5 ).place(x=577,y=330)

Ventana.mainloop()