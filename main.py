from tkinter import Tk, Button, Entry
from tkinter import messagebox

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
# root.geometry("400x400")

# Configuración pantalla de salida 
pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

numA = 0
numB = 0
op = ""
punto = False
contPunto = 0
secNum = False

def funcNum(n):
    global numA, numB, secNum, punto, contPunto
    pantalla.insert("end", n)
    if not punto:
            if not secNum:
                numA = numA*10 + n
            else:
                numB = numB*10 + n
    else:
        contPunto += 1
        if not secNum:
            numA += n*10**(-contPunto)
        else:
            numB += n*10**(-contPunto)

def funcPunto():
    global punto
    pantalla.insert("end", ".")
    punto = True

def funcOp(operacion):
    global punto, contPunto
    punto = False
    contPunto = 0
    global op
    global secNum
    secNum = True
    op = operacion
    pantalla.insert("end", operacion)

def funcEq():
    global numA, numB, contPunto
    contPunto = False
    pantalla.delete(0, "end")
    if op == "+":
        pantalla.insert(0,numA+numB)
    if op == "*":
        pantalla.insert(0, numA*numB)
    if op == "-":
        pantalla.insert(0, numA-numB)
    if op == "/":
        pantalla.insert(0, numA/numB)



# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: funcNum(1)).grid(row=1, column=0, padx=0, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: funcNum(2)).grid(row=1, column=1, padx=0, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: funcNum(3)).grid(row=1, column=2, padx=0, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: funcNum(4)).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: funcNum(5)).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: funcNum(6)).grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: funcNum(7)).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: funcNum(8)).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: funcNum(9)).grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2", command= lambda: funcEq()).grid(row=4, column=0, columnspan=2, padx=0, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command = lambda: funcPunto()).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: funcOp("+")).grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: funcOp("-")).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: funcOp("*")).grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command = lambda: funcOp("/")).grid(row=4, column=3, padx=1, pady=1)





root.mainloop()