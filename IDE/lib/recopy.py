import os 
#criar um ficheiro sem nome
#copiar os dados do ficheiro para o fichero sem nome
#mudar o nome do ficheiro sem nome para o nome do ficheiro principal
#apagar o ficheiro pricipal

def copiar():
    file = input("copiar ")
    org = "Disc\\" + file
    if org == 'Disc\\':
        pass
    elif os.path.exists(org):
        x = file.split('.')
        y = x[0] + "_copia" + "." + x[1]
        read = open( org , "r")
        dados = read.read()
        ficheiro = "Disc\\" + y  
        abrir = open( ficheiro , "a")
        colar_dados = abrir.write(dados)
        print("O ficheiro ",file," foi copiado")
    else:
        print("ficheiro nao encontrado")

def copy(file):
    org = file
    if org == 'Disc\\':
        pass
    elif os.path.exists(org):
        x = file.split('.')
        y = x[0] + "_copia" + "." + x[1]
        read = open( org , "r")
        dados = read.read()
        ficheiro = y  
        abrir = open( ficheiro , "a")
        colar_dados = abrir.write(dados)
        print("O ficheiro ",file," foi copiado")
    else:
        print("ficheiro nao encontrado")

def copy_main(file):
    org = file
    if org == 'Disc\\':
        pass
    elif os.path.exists(org):
        x = file.split('.')
        y ="main" + "." + x[1]
        read = open( org , "r")
        dados = read.read()
        ficheiro = y  
        abrir = open( ficheiro , "a")
        colar_dados = abrir.write(dados)
        print("O ficheiro ",file," foi copiado")
    else:
        print("ficheiro nao encontrado")

def copy_tmp(file):
    org = file
    if org == 'Disc\\':
        pass
    elif os.path.exists(org):
        x = file.split('.')
        y ="main" + "." + x[1]
        read = open( org , "r")
        dados = read.read()
        ficheiro = "Disc\\tmp\\" + y  
        abrir = open( ficheiro , "a")
        abrir.write(dados)
        print("O ficheiro ",file," foi copiado")
    else:
        print("ficheiro nao encontrado")

def tmp(file):
   
    
    if os.path.exists(file):
        read = open( file , "r")
        dados = read.read()
        ficheiro = "Disc\\apps\\tmp\\main.py"  
        abrir = open( ficheiro , "a")
        abrir.trucate(0)
        abrir.write(dados)
        print("O ficheiro ",file," foi copiado")
    else:
        print("ficheiro nao encontrado")


def copiar_dir():
    file = input("copiar ")
    dire = input("dir ")
    ex = "Disc\\" + file
    exes = "Disc\\"+ dire + "\\" + file
    xe = "Disc\\"+ dire
    print(ex," ",xe)
    if file == 'Disc\\' or dire == 'Disc':
        pass
    elif os.path.exists(ex) and os.path.isdir(xe):
        
        def mover_accao():
            org = "Disc\\" + file
            red = open( org , "r")
            dados = red.read()
            ficheiro = "Disc\\" + "\\" +  dire + "\\" + file 
            abrir = open( ficheiro , "a")
            colar_dados = abrir.write(dados)
            red.close()
            print("O ficheiro ",file," foi copiado para",dire)
    

        if os.path.exists(exes):
            org = "Disc\\" + file
            x = file.split('.')
            y = x[0] + "_copia" + "." + x[1]
            read = open( org , "r")
            dados = read.read()
            ficheiro = "Disc\\" + y  
            abrir = open( ficheiro , "a")
            colar_dados = abrir.write(dados)
            print("O ficheiro ",file," foi copiado")
        else:
             mover_accao()
    else:
        print("ficheiro nao encontrado")




def mover():
    name = input("mover ")
    file = input("mover de ")
    dire = input("para ")
    ex = "Disc\\" + file
    exes = "Disc\\"+ dire + "\\" + file
    xe = "Disc\\"+ dire
    print(ex," ",xe)
    if file == 'Disc\\' or dire == 'Disc' or name == 'Disc':
        pass
    
    elif os.path.exists(ex) and os.path.isdir(xe):
        
        def mover_accao():
            org = "Disc\\" + file + "\\" + name
            red = open( org , "r")
            dados = red.read()
            ficheiro = "Disc\\" +  dire + "\\" + name
            abrir = open( ficheiro , "a")
            colar_dados = abrir.write(dados)
            red.close()
            os.remove(org)
            print("O ficheiro ",name," foi movido para",dire)
    

        if os.path.exists(exes):
            print("O ficheiro ",file,"ja existe em ",dire)
            while True:
                r = input("Pretende mover mesmo assim? ")
                if r == "s" or r == "sim":
                    mover_accao()
                elif r == "n" or r == "nao":
                   break
                else:
                    print("Resposta invalida")
        else:
             mover_accao()
    else:
        print("ficheiro nao encontrado")

def mover_all():
    file = input("mover de ")
    dire = input("dir ")
    ex = "Disc\\" + file
    exes = "Disc\\"+ dire + "\\" + file
    xe = "Disc\\"+ dire
    print(ex," ",xe)
    if file == 'Disc\\' or dire == 'Disc':
        pass
    elif os.path.exists(ex) and os.path.isdir(xe):
        
        def mover_accao_all():
            lista = os.listdir(ex)
            for arq in lista:
                print(arq)
                org = "Disc\\" + file
                red = open( org , "r")
                dados = red.read()
                ficheiro = "Disc\\" + "\\" +  dire + "\\" + file 
                abrir = open( ficheiro , "a")
                colar_dados = abrir.write(dados)
                red.close()
                os.remove(org)
                print("O ficheiro ",file," foi movido para",dire)
    

        if os.path.exists(exes):
            print("O ficheiro ",file,"ja existe em ",dire)
            while True:
                r = input("Pretende mover mesmo assim? ")
                if r == "s" or r == "sim":
                    mover_accao_all()
                elif r == "n" or r == "nao":
                   break
                else:
                    print("Resposta invalida")
        else:
             mover_accao_all()
    else:
        print("ficheiro nao encontrado")

def conteudo():
    file = input("cont ")
    dire = input("para ")
    org = "Disc\\" + file
    ficheiro = "Disc\\" + dire
    if org == 'Disc\\' or ficheiro == 'Disc':
        pass
    elif os.path.exists(org) and os.path.exists(ficheiro):
        read = open( org , "r")
        dados = read.read()
        abrir = open( ficheiro , "a")
        colar_dados = abrir.write("\n",dados)
        print("O conteudo do ficheiro ",file," foi copiado para",dire)
    else:
        print("ficheiro nao encontrado")
    

def apagar_conteudo(org):
    if org == 'Disc\\':
        pass
    elif os.path.exists(org):
        re = open( org , "a")
        re.write("")
        arquivo.truncate(0)
        print("O conteudo do ficheiro de ",re," foi apagado")
    else:
        print("ficheiro nao encontrado")

def copiar_func(file,dire):

    ex = file
    exes = dire + "\\" + file
    xe = dire
    print(ex," ",xe)
    
    if os.path.exists(ex) and os.path.isdir(xe):
        
        def mover_accao():
            org = file
            red = open( org , "r")
            dados = red.read()
            ficheiro = "Disc\\" + "\\" +  dire + "\\" + file 
            abrir = open( ficheiro , "a")
            colar_dados = abrir.write(dados)
            red.close()
            print("O ficheiro ",file," foi copiado para",dire)
    

        if os.path.exists(exes):
            org = file
            x = file.split('.')
            y = x[0] + "_copia" + "." + x[1]
            read = open( org , "r")
            dados = read.read()
            ficheiro = "Disc\\" + y  
            abrir = open( ficheiro , "a")
            colar_dados = abrir.write(dados)
            print("O ficheiro ",file," foi copiado")
        else:
             mover_accao()
    else:
        print("ficheiro nao encontrado")





 

    
        

    
