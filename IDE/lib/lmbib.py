import os 
import time
import random as rm

#wait()
#until()
#raiz(n,indice)
#run()
#write()
#integer


def wait(tim):
	time.sleep(tim)

def raz(n,indice):
        global raiz
        raiz = n ** float(1/indice)
	
        return raiz

def run(file_name):
	os.startfile(file_name)
	exit()
	
def clear_screen():
        if os.name == 'nt':
                os.system('cls')
        else:
                os.system('clear')


def read_archive(file):

        fl = open(file,'r+')
        global read_text
        read_text = fl.read()
        return read_text
        
        
def clear_archive(file):
        with open(file,'r+') as fl:
                fl.truncate(0)
                fl.close()

def write(file,data):
         with open(file,'r+') as fl:
                fl.write(data)
                fl.close()

def potc(num,exp):
    return num ** exp

def random():
    return rm.random()

def chosee(a,b):
    rm.choice(a,b)
    
##print('ya')
##clear_archive('f.txt')
##wait(1)
##clear_screen()
##wait(1)
##print('bra')
##write_in('f.txt','hello from lmbib')
##print(raz(4,2))
##print(read_archive('f.txt'))
##raz(4,2)
##print(raiz)
#print(potc(2,3))
#print(random())

