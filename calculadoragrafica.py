import tkinter
import sympy as sym
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

ventana = tkinter.Tk()
ventana.title('Calculadora Cientifica')
ventana.geometry("800x600")
ventana.resizable(False, False)
ventana.configure(background='gray20')
operador = ''
texto_pantalla = tkinter.StringVar()
pant = tkinter.StringVar()
pant2 = tkinter.StringVar()

pantalla = tkinter.Entry(ventana, font=('arial', 20), width = 23, borderwidth=5, textvariable=texto_pantalla, justify=tkinter.RIGHT)
pantalla.place(x=25, y=25)

pantalla2 = tkinter.Entry(ventana, font=('arial', 20), textvariable=pant, width=24, borderwidth=None)
pantalla2.place(x=410, y=335, relheight=0.26)

pantalla3 = tkinter.Entry(ventana, width=60, borderwidth=None)
pantalla3.place(x=410, y=25, relheight=0.5)

pantalla4 = tkinter.Entry(ventana, font=('arial', 20), textvariable=pant2, width= 24, borderwidth=1)
pantalla4.place(x=410, y=335, relheight=None)

#Funciones
i=0
def AC():
    global operador
    operador = ''
    texto_pantalla.set('')
    pant.set('')
    pant2.set('')

    figura = plt.figure(figsize=(4,3), dpi=100)
    canvas = FigureCanvasTkAgg(figura, master=ventana)
    canvas.get_tk_widget().place(x=25, y=25, relwidth=0.445, relheight=0.44)
    barra_tareas = NavigationToolbar2Tk(canvas, ventana)
    barra_tareas.place(x=410, y=290, relwidth=0.445)
    canvas.get_tk_widget().place(x=410, y=25, relwidth=0.445)

    plt.clf()


def limites():
    pant.set('')
    pant2.set('')

    c=pantalla.get()
    mensaje = 'El valor de la integral definida es: '
    pantalla4.insert(0, mensaje)
    c1 = c.split(',') #Nuestra expresion matematica de limites debe ser expreda de esat forma(expresion,limite inferior, limite superior)
    li = c1[1]
    ls = c1[2]
    inte = c1[0]
    inte1 = sym.sympify(inte)
    res = sym.integrate(inte1,('x',li, ls))
    pantalla2.insert(1,res)

i+=1

def click(n):
    global i 
    pantalla.insert(i, n)
    i+=1

def operaciones(b):
    global i
    long_b = len(b)
    pantalla.insert(i,b)
    i+=long_b

def DEL():
    p = pantalla.get()
    if len(p):
        np = p[:-1]
        AC()
        pantalla.insert(0,np)
    else:
        AC()

def igual():
    estado_P = pantalla.get()
    try:
        global expresion
        expresion = sym.sympify(estado_P)

        AC()
        resultado = expresion.evalf()
        pantalla.insert(0, expresion)
    except:
        AC()

def aprox():
    contenido = pantalla.get()
    aproximacion = (sym.sympify(contenido)).evalf(15)
    AC()
    pantalla.insert(0, aproximacion)

def grafica():
    expresion = pantalla.get()
    expresion1 = sym.sympify(expresion)
    x = sym.Symbol('x')
    v = np.linspace(-15, 15,100, endpoint=True)
    valores = []

    figura = plt.figure(figsize=(4,3), dpi =100)
    canvas = FigureCanvasTkAgg(figura, master=ventana)
    canvas.get_tk_widget().place(x=410, y=25, relwidth=0.445)

    for i in range(len(v)):
        c = ((expresion1).evalf(subs={x:v[i]}))
        valores.append(c)

    figura.add_subplot(111).plot(v, valores, label = '{0}'.format(expresion))
    plt.legend(loc = 'upper left')
    plt.grid()
    canvas.draw()

def derivadas():
    pant.set('')
    pant2.set('')
    d = pantalla.get()
    if 'x' in d:
        d1 = sym.sympify(d)
        r = sym.diff(d1,'x')
        pantalla2.insert(0,r)
        mensaje = 'la derivada es: '
        pantalla4.insert(0, mensaje)
        expresion = pantalla2.get()
        expresion1 = sym.sympify(expresion)
        x = sym.Symbol('x')
        v = np.linspace(-15,15,100, endpoint=True)
        valores = []
        figura = plt.figure(figsize=(4,3), dpi=100)
        ax = figura.add_subplot(111)
        canvas = FigureCanvasTkAgg(figura, master=ventana)
        canvas.get_tk_widget().place(x=25, y=25, relwidth=0.445, relheight=0.44)
        barra_tareas = NavigationToolbar2Tk(canvas, ventana)
        barra_tareas.place(x=410, y=290, relwidth=0.445)
        canvas.get_tk_widget().place(x = 410, y = 25, relwidth=0.445)

        for i in range(len(v)):
            c = ((expresion1).evalf(subs={x: v[i]}))
            valores.append(c)
        ax.clear()
        ax.plot(v, valores, label = '{0}'.format(expresion))
        plt.grid()
        canvas.draw()
        expresion = pantalla.get()
        expresion1 = sym.sympify(expresion)
        x = sym.Symbol('x')
        v = np.linspace(-15,15,100, endpoint=True)
        valores = []
        figura = Figure(figsize=(4,3), dpi=100)
        canvas.get_tk_widget().place(x =25, y=25, relwidth=0.445, relheight=0.44)
        barra_tareas = NavigationToolbar2Tk(canvas, ventana)
        barra_tareas.place(x=410,y=25, relwidth=0.445)
        canvas.get_tk_widget().place(x=410, y=25, relwidth=0.445)
        
        for i in range(len(v)):
            c = ((expresion1).evalf(subs={x: v[i]}))
            valores.append()
        ax.plot(v,valores, label='{0}'.format(expresion))
        plt.legend(loc = 'upper left')
        canvas.draw(c)

    else:
        d1 = sym.sympify(d)
        r = sym.diff(d1, 'y')
        pantalla2.insert(0,r)
        mensaje = 'la derivada es: '
        pantalla4.insert(0, mensaje)
        expresion = pantalla2.get()
        expresion1 = sym.sympify(expresion)
        c = ''
        x = sym.Symbol('y')
        v = np.linspace(-15,15,100, endpoint=True)
        valores = []
        figura = plt.figure(figsize=(4,3), dpi=100)
        ax = figura.add_subplot(111)
        canvas = FigureCanvasTkAgg(figura, master= ventana)
        canvas.get_tk_widget().place(x = 25, y=25, relwidth=0.445,relheight=0.44)
        barra_tareas = NavigationToolbar2Tk(canvas, ventana)
        barra_tareas.place(x=410, y=25, relwidth=0.445)
        canvas.get_tk_widget().place(x=410,y=25, relwidth=0.445)
        for i in range(len(v)):
            c = ((expresion1).evalf(subs={x: v[i]}))
            valores.append(c)
        ax.clear()
        ax.plot(v,valores, label = '{0}'.format(expresion))
        plt.grid()
        canvas.draw()

        expresion = pantalla.get()
        expresion1 = sym.sympify(expresion)
        c = ''
        x = sym.Symbol('y')
        v = np.linspace(-15,15,100, endpoint=True)
        valores = []
        figura = Figure(figsize=(4,3), dpi=100)
        canvas.get_tk_widget().place(x=25, y=25, relwidth=0.445, relheight=0.44)
        barra_tareas = NavigationToolbar2Tk(canvas, ventana)
        barra_tareas.place(x=410, y=290, relwidth = 0.445)
        canvas.get_tk_widget().place(x=410, y = 25, relwidth=0.445)
        for i in range(len(v)):
            c = ((expresion1).evalf(subs={x: v[i]}))
            valores.append(c)
        ax.plot(v,valores, label = '{0}'.format(expresion))
        plt.legend(loc = 'upper left')
        canvas.draw()

def integralindef():
    pant.set('')
    pant2.set('')
    inte = pantalla.get()
    inte1 = sym.sympify(inte)
    res = sym.integrate(inte1,('x', None, None))
    pantalla2.insert(0,res)
    expresion = pantalla2.get()
    expresion1 = sym.sympify(expresion)
    mensaje = 'la integral indefinida es: '
    pantalla4.insert(0, mensaje)
    x = sym.Symbol('x')
    v = np.linspace(-15,15,100, endpoint=True)
    valores = []

    figura = plt.figure(figsize=(4,3), dpi=100)
    ax = figura.add_subplot(111)
    canvas = FigureCanvasTkAgg(figura, master=ventana)
    canvas.get_tk_widget().place(x=25,y=25, relwidth=0.445, relheight=0.44)
    barra_tareas = NavigationToolbar2Tk(canvas, ventana)
    canvas.get_tk_widget().place(x=410, y = 25, relwidth=0.445)


    for i in range(len(v)):
        c = ((expresion).evalf(subs={x: [i]}))
        valores.append(c)
        ax.plot(v, valores, label = '{0}'.format(expresion))
        plt.legend(loc = 'upper left')
        canvas.draw()

def CDF():
    pant.set('')
    pant2.set('')
    mensaje = 'Las raices son: '
    pantalla4.insert(0, mensaje)
    cdf = pantalla.get()
    cdf1 = sym.sympify(cdf)
    t1 = sym.roots(cdf1, multiple=True)

    raiz = t1[0]
    rd = (raiz).evalf(5)
    pantalla2.insert(0,rd)

    expresion = pantalla.get()
    expresion1 = sym.sympify(expresion)
    x = sym.sympify('x')
    v = np.linspace(-15,15,100, endpoint=True)
    valores = []

    figura = plt.figure(figsize=(4,3),dpi=100)
    canvas = FigureCanvasTkAgg(figura, master=ventana)
    canvas.get_tk_widget().place(x = 410, y = 25, relwidth=0.445, relheight=0.44)
    barra_tareas = NavigationToolbar2Tk(canvas, ventana)
    barra_tareas.place(x = 410, y = 290, relwidth = 0.445)
    canvas.get_tk_widget().place(x=410, y=25, relwidth=0.445)

    for i in range(len(v)):
        c = ((expresion1).evalf(subs={x: v[i]}))
        valores.append(c)
    for j in range(len(t1)):
        figura.add_subplot(111).plot(v, valores, label = '{0}'.format(expresion))
        if j==0:
            plt.legend(loc = 'upper left')
        plt.annotate('x={0}'.format(t1[j]), xy = (int(t1[j]),0), xytext=(1*(j)**0.5,1*(j)**0.5), fontsize = 8, arrowprops=dict(arrowstyle="->", connectionstyle = "arc3, rad"))

    plt.grid()
    canvas.draw()


#Botones de la calculadora

button11=tkinter.Button(ventana, text='x', bd=10, bg='darkgray', width=6, height=2, command=lambda:operaciones('x')).place(x=25, y=100)
button12=tkinter.Button(ventana, text='y', bd=10, bg='darkgray', width=6, height=2, command=lambda:operaciones('y')).place(x=117, y=100)
button13=tkinter.Button(ventana, text='x^', bd=10, bg='darkgray', width=6, height=2, command=lambda:operaciones('**')).place(x=210, y=100)
button14=tkinter.Button(ventana, text='sin', bd=10, bg='darkgray', width=6, height=2, command=lambda:operaciones('sin')).place(x=301, y=100)

button21=tkinter.Button(ventana, text='π', bd=10, bg='darkgray', width=6, height=2, command=lambda:click('pi')).place(x=25, y=150)
button22=tkinter.Button(ventana, text='e', bd=10, bg='darkgray', width=6, height=2, command=lambda:operaciones('E')).place(x=117, y=150)
button23=tkinter.Button(ventana, text='√', bd=10, bg='darkgray', width=6, height=2, command=lambda:operaciones('sqrt')).place(x=209, y=150)
button24=tkinter.Button(ventana, text='cos', bd=10, bg='darkgray', width=6, height=2, command=lambda:operaciones('cos')).place(x=301, y=150)

button31=tkinter.Button(ventana, text=',', bd=10, bg='darkgray', width=6, height=2, command=lambda:click(',')).place(x=25, y=200)
button32=tkinter.Button(ventana, text='(', bd=10, bg='darkgray', width=6, height=2, command=lambda:operaciones('(')).place(x=117, y=200)
button33=tkinter.Button(ventana, text=')', bd=10, bg='darkgray', width=6, height=2, command=lambda:operaciones(')')).place(x=209, y=200)
button34=tkinter.Button(ventana, text='tan', bd=10, bg='darkgray', width=6, height=2, command=lambda:operaciones('tan')).place(x=301, y=200)

button41=tkinter.Button(ventana, text='7', bd=10, bg='darkgray', width=6, height=2, command=lambda:click(7)).place(x=25, y=300)
button42=tkinter.Button(ventana, text='8', bd=10, bg='darkgray', width=6, height=2, command=lambda:click(8)).place(x=97, y=300)
button43=tkinter.Button(ventana, text='9', bd=10, bg='darkgray', width=6, height=2, command=lambda:click(9)).place(x=169, y=300)
button44=tkinter.Button(ventana, text='DEL', bd=10, bg='darkgray', width=6, height=2, command=lambda:DEL()).place(x=241, y=300)
button45=tkinter.Button(ventana, text='AC', bd=10, bg='darkgray', width=6, height=2, command=lambda:AC()).place(x=313, y=300)

button51=tkinter.Button(ventana, text='4', bd=10, bg='darkgray', width=6, height=2, command=lambda:click(4)).place(x=25, y=370)
button52=tkinter.Button(ventana, text='5', bd=10, bg='darkgray', width=6, height=2, command=lambda:click(5)).place(x=97, y=370)
button53=tkinter.Button(ventana, text='6', bd=10, bg='darkgray', width=6, height=2, command=lambda:click(6)).place(x=169, y=370)
button54=tkinter.Button(ventana, text='×', bd=10, bg='darkgray', width=6, height=2, command=lambda:operaciones('*')).place(x=241, y=370)
button55=tkinter.Button(ventana, text='÷', bd=10, bg='darkgray', width=6, height=2, command=lambda:operaciones('/')).place(x=313, y=370)

button61=tkinter.Button(ventana, text='1', bd=10, bg='darkgray', width=6, height=2, command=lambda:click(1)).place(x=25, y=440)
button62=tkinter.Button(ventana, text='2', bd=10, bg='darkgray', width=6, height=2, command=lambda:click(2)).place(x=97, y=440)
button63=tkinter.Button(ventana, text='3', bd=10, bg='darkgray', width=6, height=2, command=lambda:click(3)).place(x=169, y=440)
button64=tkinter.Button(ventana, text='+', bd=10, bg='darkgray', width=6, height=2, command=lambda:operaciones('+')).place(x=241, y=440)
button65=tkinter.Button(ventana, text='-', bd=10, bg='darkgray', width=6, height=2, command=lambda:operaciones('-')).place(x=313, y=440)

button71=tkinter.Button(ventana, text='0', bd=10, bg='darkgray', width=6, height=2, command=lambda:click(0)).place(x=25, y=510)
button72=tkinter.Button(ventana, text='.', bd=10, bg='darkgray', width=6, height=2, command=lambda:operaciones('.')).place(x=97, y=510)
button73=tkinter.Button(ventana, text='GRAF', bd=10, bg='darkgray', width=6, height=2, command=lambda:grafica()).place(x=169, y=510)
button74=tkinter.Button(ventana, text='APROX', bd=10, bg='darkgray', width=6, height=2, command=lambda:aprox()).place(x=241, y=510)
button75=tkinter.Button(ventana, text='=', bd=10, bg='darkgray', width=6, height=2, command=lambda:igual()).place(x=313, y=510)

#Botones para calculo 

button1 = tkinter.Button(ventana, text='f\'(x)', bd=10, bg='darkgray', font=('arial', 20), width=6,height=1, command=lambda:derivadas()).place(x=412, y=510)

button2 = tkinter.Button(ventana, text='∫', bd=10, bg='darkgray', font=('arial', 20), width=2,height=1, command=lambda:integralindef()).place(x=535.5, y=510)

button3 = tkinter.Button(ventana, text='∫ab', bd=10, bg='darkgray', font=('arial', 20), width=2,height=1, command=lambda:limites()).place(x=595, y=510)

button4 = tkinter.Button(ventana, text='Cero de funciones', bd=10, bg='darkgray', font=('arial', 10), width=13,height=3, command=lambda:CDF()).place(x=660, y=510)


ventana.mainloop()