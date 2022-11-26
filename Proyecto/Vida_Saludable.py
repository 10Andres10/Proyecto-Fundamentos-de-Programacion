from tkinter import *
from tkinter import messagebox

def validar():
    if Button.get()=="Andr":
        abrir_ventana2()
    else:
        messagebox.showwarning("Cuidado","Pasword incorrecto")

def abrir_ventana2():
    root.whithdraw()
    win = Toplevel()
    win.geometry("500x500+1900+1000")
    win.configure(background="cadetblue1")
    e3=Label(win,text="Información",bg="pink",fg="black")
    e3.place(x=50,y=50,fill=X)
    boton2= Button(win,text="ok", command=win.destroy)
    boton2.pack(side=TOP)

def cerrar_ventana():
    root.destroy()






# Ventana principal
root = Tk()
root.geometry("650x570")
root.title("Vida Saludable")
root.config(bg="cadetblue1")
root.resizable(False, False)

# Texto indicativo en forma de Label
Label1 = Label(text="Digite sus datos para continuar")
Label2 = Label(text="Nombre")
Label3 = Label(text="Edad(años)")
Label4 = Label(text="Peso(kilogramos)")
Label5 = Label(text="Altura(centímetros)")

#Configuración de los Label; tipo, tamaño y color de letra
Label1.config(fg="gray30", bg="cadetblue1", font=("Comic Sans MS",22))
Label2.config(fg="gray30", bg="cadetblue1", font=("Comic Sans MS",22))
Label3.config(fg="gray30", bg="cadetblue1", font=("Comic Sans MS",22))
Label4.config(fg="gray30", bg="cadetblue1", font=("Comic Sans MS",22))
Label5.config(fg="gray30", bg="cadetblue1", font=("Comic Sans MS",22))

# Ubicación de los Label
Label1.place(x=100, y=40)
Label2.place(x=40, y=150)
Label3.place(x=40, y=230)
Label4.place(x=40, y=310)
Label5.place(x=40, y=390)

# Entradas de texto
entrada1 = Entry() #"Nombre"
entrada2 = Entry() #"Edad(años)"
entrada3 = Entry() #"Peso(kilogramos)"
entrada4 = Entry() #"Altura(centímetros)"

#Foco de digitar texto en los entry
entrada1.focus_set()

#Configuración de las entradas; tipo, tamaño y color de letra
entrada1.config(bg="turquoise1", fg="steel blue", font=("Comic Sans MS",22))
entrada2.config(bg="turquoise1", fg="steel blue", font=("Comic Sans MS",22))
entrada3.config(bg="turquoise1", fg="steel blue", font=("Comic Sans MS",22))
entrada4.config(bg="turquoise1", fg="steel blue", font=("Comic Sans MS",22))

# Ubicación de las entradas de texto y ajustes de tamaños de las mismas
entrada1.place(x=350, y=150, width=260,height=40)
entrada2.place(x=350, y=230, width=260,height=40)
entrada3.place(x=350, y=310, width=260,height=40)
entrada4.place(x=350, y=390, width=260,height=40)

# Botón de aceptar
boton_aceptar = Button(text="Aceptar",command=abrir_ventana2)

# Ubicación del Botón aceptar
boton_aceptar.place(x=275,y=490, width=100,height=40)



root.mainloop()