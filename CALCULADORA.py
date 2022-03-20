"""
PROJETO CALCULADORA
"""
from tkinter import *
from tkinter import ttk

resultado = 0   #variável criada para executar a função fatorial
todo_valor = '' #variável que vai receber os botões clicados e irá mostrar na tela a operação que está sendo construida

def entrar_valores(event):
    """
    Essa função irá receber os clickes (eventos) e irá armazena-los como uma string para poder ser executado posteriormente
    o comando desejado pelo usuário.
    """
    global todo_valor
    todo_valor += str(event)    #cada evento será transformado em string

    valor_texto.set(todo_valor) #serve para receber e mostrar no display o resultado

def calcular():
    """
    essa função calcula todas as funções básicas como soma, multiplicação, divisão, subtração
    porém não calcula o fatorial, sendo necessário outra função para isso
    """
    global todo_valor,  resultado
    resultado = eval(todo_valor)

    valor_texto.set(str(resultado))

def limpaTela():
    """
    Como o próprio nome diz, essa função tem como objetivo limpar a tela e as variáveis para que novas contas sejam feitas

    """
    global todo_valor, resultado
    todo_valor = ''
    resultado = 0
    valor_texto.set('')

def fatorial():
    """
    Essa função irá fazer a fatoraçao de um número.
    """
    global todo_valor,resultado
    if resultado == 0:      #para iniciar dando um número apenas, resultado tem que ser 0 (ou seja, o sinal de igual não foi pressionado),
        # assim não terá ocorrido nenhuma função anterior
        a = int(todo_valor)
        b = a - 1
        while b != 0:
            a = a * b
            b -= 1
        fatora = str(a)
        valor_texto.set(fatora)
    elif resultado != 0:    #para entrar nessa condicional o usuário já deve ter feito alguma conta/função e
        # então será feito o fatorial do resultado dessa conta
        a = int(resultado)
        b = a - 1
        while b != 0:
            a = a * b
            b -= 1
        fatora = str(a)
        valor_texto.set(fatora)

# cores usadas
cor1 = "#3b3b3b" #cor preta
cor2 = "#feffff" #cor branca
cor3 = "#38576b" #azul
cor4 = "#c7c2bb" #cor cinza
cor5 = "#e69109" #laranja

# Construindo a interface
janela = Tk()
janela.title("Calculadora")
janela.geometry('240x330')  #por tentativa e erro encontrei o que parece ser um bom tamanho
janela.configure(bg='black')

frame_display = Frame(janela, width= 240, height = 70,bg= cor3)
frame_display.grid(column= 0, row =0)

frame_corpo = Frame(janela, width= 240, height = 280)
frame_corpo.grid(row =1, column= 0)

#criando o label que irá aparecer no display.
valor_texto = StringVar()   #variável que será demonstrada no display

app_label = Label(frame_display, textvariable= valor_texto, width=16,height=2, padx=7, pady=10, relief='flat',
                  anchor='e',justify= RIGHT,font=('Ivy 18'), bg=cor3)
app_label.place(x = 0, y=0)


#----------------------------------------------------------
# CONSTRUINDO OS BOTÕES
#----------------------------------------------------------

# construindo os botões da primeira fila
b1 = Button(frame_corpo, command = limpaTela, text="C", width=11, height=2,
            bg= cor5, font=('Ivy 12 bold'), relief="raised", overrelief= RIDGE)
b1.place(x=0,y=0)
b2 = Button(frame_corpo, command = fatorial,text = "!", width= 5, height=2,
            bg= cor5,font=('Ivy 12 bold'), relief="raised", overrelief= RIDGE)
b2.place(x=120,y=0)
b3 = Button(frame_corpo, command = lambda: entrar_valores('*'),text = "x", width= 5, height=2,
            bg =cor5,font=('Ivy 12 bold'), relief="raised", overrelief= RIDGE)
b3.place(x=180,y=0)

# construindo os botões da segunda fila
b4 = Button(frame_corpo, command = lambda: entrar_valores('7'),text="7", width=5, height=2,
            bg= cor4,font=('Ivy 12 bold'), relief="raised", overrelief= RIDGE)
b4.place(x=0,y=52)
b5 = Button(frame_corpo, command = lambda: entrar_valores('8'),text = "8", width= 5, height=2,
            bg= cor4,font=('Ivy 12 bold'), relief="raised", overrelief= RIDGE)
b5.place(x=60,y=52)
b5 = Button(frame_corpo, command = lambda: entrar_valores('9'),text = "9", width= 5, height=2,
            bg= cor4,font=('Ivy 12 bold'), relief="raised", overrelief= RIDGE)
b5.place(x=120,y=52)
b7 = Button(frame_corpo, command = lambda: entrar_valores('/'),text = "/", width= 5, height=2,
            bg =cor5,font=('Ivy 12 bold'), relief="raised", overrelief= RIDGE)
b7.place(x=180,y=52)

# construindo os botões da terceira fila
b8 = Button(frame_corpo, command = lambda: entrar_valores('4'),text="4", width=5, height=2,
            bg= cor4,font=('Ivy 12 bold'), relief="raised", overrelief= RIDGE)
b8.place(x=0,y=104)
b9 = Button(frame_corpo, command = lambda: entrar_valores('5'),text = "5", width= 5, height=2,
            bg= cor4,font=('Ivy 12 bold'), relief="raised", overrelief= RIDGE)
b9.place(x=60,y=104)
b10 = Button(frame_corpo, command = lambda: entrar_valores('6'),text = "6", width= 5, height=2,
             bg= cor4,font=('Ivy 12 bold'), relief="raised", overrelief= RIDGE)
b10.place(x=120,y=104)
b11 = Button(frame_corpo, command = lambda: entrar_valores('+'),text = "+", width= 5, height=2,
             bg =cor5,font=('Ivy 12 bold'), relief="raised", overrelief= RIDGE)
b11.place(x=180,y=104)

# construindo os botões da quarta fila
b8 = Button(frame_corpo, command = lambda: entrar_valores('1'),text="1", width=5, height=2,
            bg= cor4,font=('Ivy 12 bold'), relief="raised", overrelief= RIDGE)
b8.place(x=0,y=156)
b9 = Button(frame_corpo, command = lambda: entrar_valores('2'),text = "2", width= 5, height=2,
            bg= cor4,font=('Ivy 12 bold'), relief="raised", overrelief= RIDGE)
b9.place(x=60,y=156)
b10 = Button(frame_corpo, command = lambda: entrar_valores('3'),text = "3", width= 5, height=2,
             bg= cor4,font=('Ivy 12 bold'), relief="raised", overrelief= RIDGE)
b10.place(x=120,y=156)
b11 = Button(frame_corpo, command = lambda: entrar_valores('-'),text = "-", width= 5, height=2,
             bg =cor5,font=('Ivy 12 bold'), relief="raised", overrelief= RIDGE)
b11.place(x=180,y=156)

# construindo os botões da quinta fila
b12 = Button(frame_corpo, command = lambda: entrar_valores('0'),text="0", width=11, height=2,
             bg= cor4, font=('Ivy 12 bold'), relief="raised", overrelief= RIDGE)
b12.place(x=0,y=208)
b13 = Button(frame_corpo, command = lambda: entrar_valores('.'),text = ".", width= 5, height=2,
             bg= cor4,font=('Ivy 12 bold'), relief="raised", overrelief= RIDGE)
b13.place(x=120,y=208)
b14 = Button(frame_corpo, command = calcular, text= "=", width= 5, height=2, bg =cor5,font=('Ivy 12 bold'),
             relief="raised", overrelief= RIDGE)
b14.place(x=180,y=208)


janela.mainloop()