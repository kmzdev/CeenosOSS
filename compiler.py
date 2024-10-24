import os
import time



def nothing():
    with open ('trans.txt','r') as aq:
            yt = aq.read()
    #print(yt)
    with open (script,'w') as aq:
        aq.truncate(0)
        aq.write(yt)
    #print(yt)
    os.remove('trans.txt')
    os.remove('ident.txt')
    os.remove('prev.txt')
    os.remove('new.txt')
    os.remove('compiled.txt')
    os.remove('final.txt')
    print('Done!')
    time.sleep(5)
    



            

def transpiler(pseudocode):
    good = False
    python_code = ""
    code_lines = pseudocode.split("\n")
    
    
    for line in code_lines:
        
        
       
        if line.startswith("if"):
            condition = line.split('->')[1]
            python_code += f"if {condition} :\n"

        elif line.startswith("begin"):
            good = True
            python_code += "begin\n"
            
        

        elif line.startswith("x ++"):
            python_code += "x += 1\n"

        elif line.startswith("show"):
            output = line.split("(")[1].split(")")[0]
            python_code += f"print({output})\n"

        elif line.startswith("else"):
            python_code += "else:\n"

        else:
            python_code += line + "\n"
    #print(python_code)
    
            
    with open('trans.txt','r+') as klo:
        klo.truncate(0)
        klo.write(python_code)
        toread = klo.readlines()
        #print(toread)
    

    
    rs = ''

    for h in toread:
        rs += h
        
    #print('ya')

   
        

    if good == True:
        print('Pass')
    else:
        print('Pass')
        nothing()
        
            
            
    global total
    total = 1
        
    for t in code_lines:
        total += 1

    #print('total ' ,total)
    global c
    c = 1
         

    for line in code_lines:
        if 'begin' in line:
            #print(c)
            again()
            break
         
        else:
            c += 1
            #print(c)

def again():
        n = ''
        d = 1
        
        with open ('trans.txt','r') as arq:
            z = arq.readlines()
            

        for i in z:
                if c != d:
                    
                    n += i
                    d += 1
                else:
                    pass
        #print(d,'\n',n)

        with open ('new.txt','w') as arq:
            arq.write(n)
        
        f = 1
        global k
        k = ''

        gh = total - c

        with open ('trans.txt','r') as aq:
            q = aq.readlines()[::-1]

        for i in q:
                if f != gh:
                    
                    k += i
                    f += 1
                else:
                    pass
        #print(k)
        gas = ''
        with open ('prev.txt','r+') as aq:
            aq.truncate(0)
            aq.write(k)
        with open ('prev.txt','r+') as aq:
            data = aq.readlines()[::-1]
            #print(data)
            for i in data:
                gas += i
        
        with open ('final.txt','r+') as fq:
            fq.truncate(0)
            fq.write(gas)
                
        #print(gas)
    
        with open ('final.txt','r+') as aq:
            dtf = aq.readlines()
            sz = ''
            for i in dtf:
                if i.startswith('if'):
                    sz += i
                elif i.startswith('else'):
                    sz += i
                elif i.startswith('end'):
                    #print('case')
                    pass
                elif i.startswith('begin'):
                    #print('case')
                    pass
                else:
                    sz  += "    " + i 
            #print(sz)

        with open ('ident.txt','r+') as aq:
            aq.truncate(0)
            aq.write(sz)
        with open ('compiled.txt','r+') as aq:
            global final_code
            final_code = n + sz
            aq.truncate(0)
            aq.write(final_code)
            #print(final_code)
            
        with open(script,'w') as run:
            run.truncate(0)
            run.write(final_code)
        os.remove('trans.txt')
        os.remove('ident.txt')
        os.remove('prev.txt')
        os.remove('new.txt')
        os.remove('compiled.txt')
        os.remove('final.txt')
        
        print('Done!')
        time.sleep(5)
    
        
        

                

##        with open ('f.txt','r+') as aq:
##                aq.truncate(0)
##                aq.write(_code)
##        
##                    
            
            
        
    
pseudocod = """
show('x')
x = 1
if -> x > 2 
begin
x ++ 1
if -> x == 3
begin
show(x)
end
end
else
begin
show("maior")
show("ei")
end

"""

awr = input('> ')

if os.path.exists(awr):
    pass
else:
    print('File Not Found')
    os.remove('trans.txt')
    os.remove('ident.txt')
    os.remove('prev.txt')
    os.remove('new.txt')
    os.remove('compiled.txt')
    os.remove('final.txt')
    time.sleep(5)
    exit()

with open ('trans.txt','w') as arq:
    pass
with open ('ident.txt','w') as arq:
    pass
with open ('prev.txt','w') as arq:
    pass
with open ('new.txt','w') as arq:
    pass
with open ('compiled.txt','w') as arq:
    pass
with open ('final.txt','w') as arq:
    pass
    
script = awr +'.py'
with open (script,'w') as arq:
    pass

with open (awr,'r') as arq:
    pseudocode = arq.read()

python_code = transpiler(pseudocode)
#print(python_code)
#exec(python_code)



