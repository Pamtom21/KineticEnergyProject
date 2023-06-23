import tkinter as tk

Ventana = tk.Tk()
Ventana.geometry('320x320')
Ventana.title('Energia Cinetica')
Ventana.configure(background= 'dark slate blue')


n1 = tk.Entry(Ventana, text ='1')#masa
n1.place(x=92,y=40)


n2 = tk.Entry(Ventana, text= '2')#velocidad
n2.place(x=92,y=90) 


def resolver(*_):
    a= n1.get()#masa
    b= n2.get()#velocidad

    if not (a:= n1.get()) or not (b:= n2.get()):
        return
    try:
        a, b = float(a), float(b)

    except ValueError:
        res.set("ERROR")
    else: res.set(str(0.5*a*(b**2))+' '+'Joule')
    
res = tk. StringVar()
botonPr = tk.Button(Ventana, text = 'CALCULAR', command = resolver ).place(x=110,y=250)
tk.Label(Ventana, text="\nIngrese Masa(kg)").place(x=92,y=5)
tk.Label(Ventana, text="\nIngrese Velocidad(m/s)").place(x=92,y=55)
tk.Label(Ventana, text="\nLa energia cinetica es: ").place(x=92,y=130)
tk.Entry(
    Ventana, justify="center", textvariable=res, state="disabled"
    ).place(x=92,y= 170)

Ventana.mainloop()
