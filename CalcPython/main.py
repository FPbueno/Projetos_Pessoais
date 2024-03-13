#usando a biblioteca do tkinter para criar uma interface de calculadora em python
from tkinter import *
from tkinter import ttk

#colors
color1 = "#212121" #cor que utilizaremos no aplicativo preto
color2 = "#feffff" #branco
color3 = "#38576b" #azul
color4 = "#ECEFF1" #cinza
color5 = "#FFAB40" #laranja


#creating window
window = Tk() #chamando a função do tkinter que cria uma janela flutuante
window.title("Calculator") #colocando o nome dessa janela
window.geometry("235x311") #definindo a largura e a altura da janela
window.config(bg=color1) #chamamos o .config para configurar a cor de fundo esse metodo é utilizado para configurar a janela

#creating frames
frame_window = Frame(window, width=235, height=50, bg=color1) #criando valores para dividir a tela
frame_window.grid(row=0, column=0) #aplicamos grid na tela para fazer a divisão visual utilizando os valores definidos acima

frame_body= Frame(window, width=235, height=268) 
frame_body.grid(row=1, column=0)

#variavel todos valores
all_values = ''

value_text = StringVar() #ele recebe o valor que é passado dentro da string text do botao

#creating logic using eval
#eval nos permite executar expressões algebricas para fazer a logica

def inputValue(event):
    global all_values
    all_values += str(event)

    #passando o label que criamos para dentro da função e imprimindo o valor na tela
    value_text.set(all_values)

#função para calcular os valores
    
def calculator():
    global all_values
    result = eval(all_values)
    
    value_text.set(str(result))

#função clear para limpar a tela
def clear():
    global all_values
    all_values = ''
    value_text.set('')

#creating labels

app_label = Label(frame_window, textvariable=(value_text), width=16, height=2, padx=7, relief=FLAT, anchor="e",justify=RIGHT,font=('Ivy 18'), bg=color1 , fg=color2)
app_label.place(x=0,y=0)

#creating buttons
bt1 = Button(frame_body, command=clear,text="C", width=11, height=2, bg=color4 , font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt1.place(x=0, y=0)
bt2 = Button(frame_body, command = lambda:inputValue('%'),text="%", width=5,height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt2.place(x=118, y=0)
bt3 = Button(frame_body, command = lambda:inputValue('/'),text="/", width=5,height=2, bg=color5 , fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt3.place(x=177, y=0)

bt4 = Button(frame_body, command = lambda:inputValue('7'),text="7", width=5,height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt4.place(x=0, y=52)
bt5 = Button(frame_body, command = lambda:inputValue('8'),text="8", width=5,height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt5.place(x=59, y=52)
bt6 = Button(frame_body, command = lambda:inputValue('9'),text="9", width=5,height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt6.place(x=118, y=52)
bt7 = Button(frame_body, command = lambda:inputValue('*'),text="*", width=5,height=2, bg=color5 , fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt7.place(x=177, y=52)

bt8 = Button(frame_body, command = lambda:inputValue('4'),text="4", width=5,height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt8.place(x=0, y=104)
bt9 = Button(frame_body, command = lambda:inputValue('5'),text="5", width=5,height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt9.place(x=59, y=104)
bt10 = Button(frame_body, command = lambda:inputValue('6'),text="6", width=5,height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt10.place(x=118, y=104)
bt11 = Button(frame_body, command = lambda:inputValue('-'),text="-", width=5,height=2, bg=color5 , fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt11.place(x=177, y=104)

bt12 = Button(frame_body, command = lambda:inputValue('1'),text="1", width=5,height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt12.place(x=0, y=156)
bt13 = Button(frame_body, command = lambda:inputValue('2'),text="2", width=5,height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt13.place(x=59, y=156)
bt14 = Button(frame_body, command = lambda:inputValue('3'),text="3", width=5,height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt14.place(x=118, y=156)
bt15 = Button(frame_body, command = lambda:inputValue('+'),text="+", width=5,height=2, bg=color5 , fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt15.place(x=177, y=156)

bt16 = Button(frame_body, command = lambda:inputValue('0'),text="0", width=11, height=2, bg=color4 , font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt16.place(x=0, y=208)
bt17 = Button(frame_body, command = lambda:inputValue('.'),text=".", width=5,height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt17.place(x=118, y=208)
bt18 = Button(frame_body, command = calculator,text="=", width=5,height=2, bg=color5 , fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bt18.place(x=177, y=208)

window.mainloop() #codigo para rodar a aplicação