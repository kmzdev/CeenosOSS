import os
import time
import re

awr = input('> ')

#awr = 'Exemplos\test.lm'

def remover_espacos_inicio(texto):
    linhas = texto.split('\n')  # Dividir o texto em linhas
    linhas_sem_espacos = [linha.lstrip() for linha in linhas]  # Remover espaços à esquerda de cada linha
    texto_sem_espacos = '\n'.join(linhas_sem_espacos)  # Juntar as linhas de volta em um texto
    global fado
    fado =  texto_sem_espacos
    return fado
       
def transpiler(pseudocode):
    
    python_code = ''
    code_lines = pseudocode.split("\n")
    pth = []
    
    for line in code_lines:

        if line.startswith("elif"):
            condi = line.split('elif ')[1]
            python_code += f"elif {condi} :\n"

        elif line.startswith('begin'):
            #python_code += '#begin\n'
            python_code += '\n'
            
        elif line.startswith('end'):
            #python_code += '#end\n'
            python_code += '\n'

        elif line.startswith("if"):
            condition = line.split('if ')[1]
            python_code += f"if {condition}:\n"
            
        elif line.startswith("import"):
            lib = line.split('import ')[1]
            python_code += f"import {lib} \n"
			
        elif line.startswith("uses"):
            lib = line.split('uses ')[1]
            python_code += f"import {lib} \n"

        elif line.startswith("while"):
            co = line.split('while ')[1]
            python_code += f"while {co}:\n"

        elif line.startswith("let"):
            condition = line.split('let ')[1]
            python_code += f"{condition}\n"
			
        elif line.startswith("until"):
            cou = line.split('until ')[1]
            fnu = cou.replace('True','False').replace('False','True').replace('==','<').replace('<','>').replace('>','<').replace('!=','==').replace('>=','=<').replace('<=','>=')
            python_code += f"while {fnu}:\n"
            
        elif line.startswith("func"):
            fnc = line.split('func ')[1]
            python_code += f"def {fnc}:\n"

        elif "input" in line:
            var_inp = line.split('=')[0].replace('input ','')
            inp = line.split('=')[1]
            #print(var_inp,inp)
            python_code += f"{var_inp} = input({inp}) \n"

                 
        elif "++" in line:
            num = line.split('++')[0]
            nume = line.split('++')[1]
            python_code += num + "+=" + nume + "\n"

        elif "//" in line:
            python_code += line.split('//')[0]+'#'+line.split('//')[1]+'\n'

        elif "show" in line:
            output = line.split("(")[1].split(")")[0]
            python_code += f"print({output})\n"

        elif line.startswith("var"):
            var = line.split(":")
            python_code += var[1] + '\n'

        elif line.startswith("else"):
            python_code += "else:\n"
    
        else:
            python_code += line + "\n"

        
    for k in python_code.split('\n'):
        pth.append(k+'\n')
            
    def identer():
            j = ''
            jgf = ''
            n = 0
            ids = 0
            token = []
            line = 0
            ident_level = 0
            id_str = []
            global lop
            lop = ''
            global jp
            jp = ''
            fg = ''

            
            for i in remover_espacos_inicio(pseudocode).split('\n'):
                #print(i)
                 
                line += 1
                
                if i.startswith('begin') or i.startswith('{'):
                       
                        ident_level += 1
                elif i.startswith('end') or i.startswith('}'):
                       
                        ident_level =  ident_level - 1
                else:
                    pass
               
                id_str += str(ident_level)
                        
            idn = '\n' + 'identation_level = ' + str(id_str)
            #print(idn)
   
            for h in id_str :
                    
                fg = pth[n]
                n += 1
                
                for i in range(int(h)):
                    jp += '    '

                # if fg.startswith('begin'):
                    # fg = fg
                # elif fg.startswith('end'):
                    # fg = fg
                # else:
                    # jp += fg

                jp += fg
        
            #print(jp) 
            # for u in jp.split('\n'):
                
                # if u.startswith('begin'):
                    # pass
                # elif u.startswith('end'):
                    # pass
                # elif '{' in u:
                    # pass
                # elif '}' in u:
                    # pass
                # else:
                    # lop += u + '\n'

    identer()
        
    with open('Compiled\\'+script,'w') as run:
        run.truncate(0)
        run.write(jp)
        run.close()

    print('Done!')
    time.sleep(5)
    while True:
        pass

def start():
    if os.path.exists(awr):
        pass
    else:
        print('File Not Found')   
        #os.remove('compiled.txt')  
        start()
        
    if os.path.isdir('Compiled'):
            pass
    else:
        os.mkdir('Compiled')
    
    idh = awr.replace('.lm','')

    global script
    script = idh.split('\\')[-1] +'.py'
    
    with open (awr,'r') as arq:
        code = arq.read()
        arq.close()
        transpiler(remover_espacos_inicio(code))
        
        
start()
