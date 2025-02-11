from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename
from tkinter import messagebox
import subprocess
import os
import time

lmout = 'LM<IDE 2024 © Copyright  version 1.0 Build 7 \n>LM Output Window ' + time.strftime('%d/%m/%Y %H:%M:%S') + '\n'

about_lm = '''
LM IDE

version 1.0
Complier version : 1.0
Compiler Build :'''+'''
Created by Klit Zets(CFZ)


You are Welcome !

The LM code editor !


'''
def sairg():
        if os.path.exists('runtime/code.flm'):
                        os.remove('runtime/code.flm')
        if os.path.exists('runtime/path.flm'):
                        os.remove('path.run')
        exit()

def help():
        def sair():
                help_window.destroy()
                
        help_window = Toplevel()
        help_window.title('Help')
        help_window.geometry('600x400')
        help_window.config(bg='white')
        help_label = Text(help_window,height=25,wrap="word", undo=True)
        help_label.pack(side='top')
        help_label.insert('1.0',dcl.doc)

def about():
        def novw():
                
                def sair():
                        nov.destroy()
                        
                nov = Toplevel(compiler)
                nov.title('Novidades')
                nov.geometry('300x300')
                #about_window.config(expand= False)
                nov_label = Label(nov,text='Aqui aparecerao as novidades!')
                nov_label.pack()
                
        def sair():
                about_window.destroy()
                
        about_window = Toplevel(compiler)
        about_window.title('About')
        about_window.geometry('300x300')
        #about_window.config(expand= False)
        about_label = Label(about_window,text=about_lm)
        about_label.pack()
        frame = Frame(about_window)
        frame.pack(side='bottom',fill='x') 
        about_button = Button(frame,text='Close',command=sair)
        about_button.pack(side='right')
        about_button = Button(about_window,text='News',command=novw)
        about_button.pack(side='bottom')

def docs():
    os.startfile('resources/documentaçao_lm.py')
        
         

'''Based on Programming Hero 'https://www.youtube.com/watch?v=f1u3me4GYmw'''

compiler = Tk()
compiler.title('LM<IDE')
img = PhotoImage(file='resources/logo.png')
compiler.iconphoto(False,img)
editor = Text()
editor.pack(fill=BOTH,expand=True)

# global code_output
# code_output = Text(height=5,state='disabled')
# code_output.pack(fill=BOTH,expand=True)


dir_label = Text(height=1,state='disabled')
dir_label.pack(fill=BOTH,side='top')


file_path = ''

lmcompiler = ['compilers.py','lm.py','lm.py']

def restart():
        os.startfile('LM IDE.pyw')
        exit()

def set_file_path(path):
        global file_path
        file_path = path
        dir_label.config(state='normal')
        dir_label.delete('1.0',END)
        dir_label.insert('1.0',file_path)
        dir_label.config(state='disabled')
        


def comp():
        with open('runtime/path.flm','w') as flm:
                
                flm.truncate(0)
                flm.write(file_path)
        

def open_file():
        
        
        path = askopenfilename(filetypes=[('LM','*.lm'),('Python','*.py')])
##        if file_path == '':
##                return
        with open(path,'r') as file:
                code = file.read()
                editor.delete('1.0',END)
                editor.insert('1.0',code)
        

        set_file_path(path)
        comp()
                

def save_as():
        if file_path == '':
                path = asksaveasfilename(filetypes=[('LM','*.lm'),('Python','*.py')])
        else:
                path = file_path
        with open(path,'w') as file:
                code = editor.get('1.0',END)
                file.truncate(0)
                file.write(code)
        comp()


def compile_run():
        if file_path == '':
                messagebox.showinfo(title='Compile Error',message='Please save your code')
                return
        if file_path.endswith('.py'):
                messagebox.showinfo(title='Compile Error',message="You can't compile python code")
                return
        if file_path.endswith('.lm') == False:
                messagebox.showinfo(title='Compile Error',message="This is not a lm file \n You can't compile this code")
                return
        with open(file_path,'w') as file:
                code = editor.get('1.0',END)
                file.truncate(0)
                file.write(code)
        os.startfile('lm.py')
        
def compiled():
        if file_path == '':
                messagebox.showinfo(title='Compile Error',message='Please save your code')
                return
        if file_path.endswith('.py'):
                messagebox.showinfo(title='Compile Error',message="You can't compile python code")
                return
        if file_path.endswith('.lm') == False:
                messagebox.showinfo(title='Compile Error',message="This is not a lm file \n You can't compile this code")
                return
        with open(file_path,'w') as file:
                code = editor.get('1.0',END)
                file.truncate(0)
                file.write(code)
        os.startfile('lm.py')
        
       
                


def run():
        
        if file_path == '':
                messagebox.showinfo(title='Run Error',message='Please save your code')
                return
        if file_path.endswith('.py'):
                code_output = Text(height=5,state='disabled')
                code_output.pack(fill=BOTH,expand=True)
                command = f'python {file_path}'
                process = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
                output,error = process.communicate()
                code_output.config(state='normal')
                code_output.insert(END,lmout)
                code_output.insert(END,output)
                code_output.insert('end-1c',error)
                code_output.insert(END,'Done!')
                code_output.config(state='disabled')
                
        elif file_path.endswith('.lm'):
                
                
                with open('runtime/code.flm','w') as file:
                        code = editor.get('1.0',END)
                        file.truncate(0)
                        file.write(code)
               
                        
                os.startfile('lm.py')
                with open('compiled/compiled.txt','r') as file:
                        codein = file.read()
                        
                
                # code_output.config(state='normal')
                # code_output.insert(END,codein)
        else:
             messagebox.showinfo(title='Run Error',message="This is not a lm file \n You can't run this code")
        

##        code = editor.get('1.0',END)
##        exec(code)
        

menu_bar = Menu(compiler)

file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_command(label='Open',command=open_file)
file_menu.add_command(label='Save',command=save_as)
file_menu.add_command(label='Save As',command=save_as)
file_menu.add_command(label='Restart',command=restart)
file_menu.add_command(label='Exit',command=sairg)
menu_bar.add_cascade(label='File',menu=file_menu)

run_bar = Menu(menu_bar,tearoff=0)
run_bar.add_command(label='Run',command=run)
run_bar.add_command(label='Compile',command=compiled)
run_bar.add_command(label='Compile and Run',command=compile_run)
menu_bar.add_cascade(label='Run',menu=run_bar)

run_bar = Menu(menu_bar,tearoff=0)
run_bar.add_command(label='About',command=about)
run_bar.add_separator()
run_bar.add_command(label='LM Docs',command=docs)
menu_bar.add_cascade(label='Help',menu=run_bar)



compiler.config(menu=menu_bar)

compiler.mainloop()



