import tkinter
from tkinter import *
import math

def window_exit():
    sair()
        

def sair():    
    window.destroy()

default = '#ebebeb'
fg_default = 'white'


class Win():
       
    def Window(self,texto,size):
        def minv():
            window.geometry(size)
            

        def maxv():
        # getting screen's height in pixels
            height = window.winfo_screenheight()
 
        # getting screen's width in pixels
            width = window.winfo_screenwidth()
            resol =  str(width) + 'x' + str(height)
            window.geometry('+0+0')
            window.geometry(resol)
            #window.overrideredirect(False)
            #window.attributes('-fullscreen',True)
        
       
        global window
        #antes windows era = types agora  windows = Toplevel() para centralizar apps nat tela para nao desaparecer

        window = Tk()#types#Toplevel()
        #print(types)
        window.geometry(size)
        window.title(texto)
        #window.grab_set()
        
        

    def new_button(local,texti,comand):

            global button
            button = Frame(local,highlightbackground = 'black',highlightthickness=1,bd=0)
            global btn
            btn = Button(button,text=texti,command= comand,bd=0,highlightthickness=1,bg='white')
            btn.pack()
    
        
    def stay(self):
        window.mainloop()
        
    def local(self,place):
        window.geometry(place)
        
    

    def bg(self,photo):
        if '.png' in photo:
            bg = PhotoImage(file = photo)
            img = Label(window,image= bg)
            img.place(x=0,y=0)
        elif photo == 'default':
            window.config(bg='#ebebeb')
        else:
            window.config(bg=photo)

    def resize(self,val):
        if val == False:
            window.resizable(False,False)
        elif val == True:
            pass
        else:
           print('err0r')
           
    def min_max(self,val):
        if val == False:
            window.attributes('-toolwindow',True)
        elif val == True:
            pass
        else:
           print('err0r')

    def fix(self,val):
        if val == True:
            window.grab_set()
        elif val == False:
            pass
        else:
           print('err0r')
           
    def move(self,val):
        if val == True:
            window.geometry('+0+0')
        elif val == False:
            pass
        else:
           print('err0r')

    def over(self,val):
        if val == True:
            window.overrideredirect(True)
        elif val == False:
            pass
        else:
           print('err0r')
           
    def fullscreen(self,val):
        if val == True:
            window.attributes('-fullscreen',True)
        elif val == False:
            pass
        else:
           print('err0r')
    

    def transperecy(self,val,ev):
        if val == True:
            x = ev/100
            window.attributes('-alpha',x)
        elif val == False:
            pass
        else:
           print('err0r')

def Dialog(message=''):
    xs = 200
    ys = 100
    xd = 0
    
    for i in message:
        xd = 5
        xs += 10
        ys += 1
        

    res = str(xs) + 'x' + str(ys)
    Win.Window(Toplevel(),res,'Aviso!','off')
    Win.bg('default')
    
    tbar = Frame(window,bg=default)
    tbar.config(height=5)
    tbar.pack(side='top')
    
    boton = Label(window,text=message,bg=default)
    boton.pack(side='top')
    
    bar = Frame(window,bg=default)
    bar.config(height=15)
    bar.pack(side='bottom')
    
            
    Win.new_button(window,'  OK  ',window_exit)
    button.pack(side='bottom')

            
    Win.stay()

