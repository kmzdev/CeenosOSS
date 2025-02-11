from tkinter import *

ver = ' v11x'

historia = '''Um pouco de historia

Em primero lugar quero agradecer a Deus por me conceder a capacidade e inteligencia para eu poder criar esta linguagem de programaçao que apelidei de LM que significa LINGUAGEM MILAGRE ,milagre porque foi um milagree de Deus eu ter consegido criar esta linguagem de programaçao com tao poucos conhecimentos foi necessario muita pesquisa e trabalho para poder cria-la. 

LM e um lingagem de programaçao que tem como objectivo ser simples.

LM de LINGUAGEM MILAGRE
Atualmente LM possui um compilador que compila para Python

Ao criar a LM inspirei-me em linguagens com Pascal,Python e C.
Implementado recursos de cada uma delas para poder criar a LM.

Compilar para Python facilitou muito minha jornada para poder construir um compilador.

Primeiro tentei contruir um compilador v1 que era generico e limitava muito a linguagem

Depois decidi criar um compilador que continuava limitada v3 a v4 ,foi a i que decidi muadar minha frma de programr o compilador edecidi dividir lexer,identer e transpiler ou seja um analisador lexico um identador e um tradutor

O motivo de tanta redundacia foi temosia da minha parte em tentar aprender como realmente funcionava um compilador,depois de mudar o compildor ele mostrou sucesso

Da v1 a v4 as coisas funcionava assim:
- O interpreatador ou compilador tinha uma estrutura predfinida de codigo e por isso o codigo ficava muito limitado principalmente no interpretador onde cada palavra tinha de estar e uma ordem especifica e nao funcinava;
-nao era possivel combinar tokens ou usar um if dentro doutri em diante;

Na v4 as coisas funcianam assim:
0.o codigo e traduzido
1.o codigo e repartido apos o primeiro end e o resto e resto e separado
2.o o codigo e lido de trans pra frente e e identado

Mas essa forma de traducao limitava muito e causava mitos erros e identava tudo depois do primeiro end

Mas agora na v5 as coisas funcianam diferente:
1.o lexer le todo o codigo e cria um lista de toknes e iveis de identacao
2.o transpiler traduz as palavras chaves e outras estruras
3.o identer identa o codigo traduzido com base na lista de identcao criada pelo o lexer.

Essa nova abordagem permite identar e traduzir o codigo em quaiqer codicoes que nao eram possives nas v1 a v4

Sem contar que a primeira versao do compilador e outras antigas foram cridas usando o ChatGPT e esses cdigos tinham erros e limitaçoes e eu nem sabia o que estav fazendo por isso nem consegia resolver esses erros depis nao tive mais acesso ao ChatGPT e decidi largar a IA e tentar fazer sozinho e deu certo.

Uma prova de que podemos fazer tudo que quisermos se tivermos fe e confiar em Deus.
'''
doc = '''Documentação LM

//Palavras-chave e estrutura

// - marcar comentarios
ex:
	//Isto e um comentario


begin - marca inicio de bloco de codigo
end - indica fim de um bloco de codigo


let - serve para definir variaveis do tipo dinamico
ex:
	let -> x = 2


show -  para imprimir texto na tela
ex:
	1.show('Hello World!)

	2. let -> x = 2
	   show(x)
		

if -  para determinar uma condicao
ex:

	if -> x == 2
	begin
	show('x = 2')
	end

elif - caso a condicao de if nao tenha sido satisfeita
ex:
	elif -> x > 2
	begin
	show('x > 2')
	end


else - caso a condicao de if nao seja verdadeira
ex:
	else
	begin
	show('x != 2')
	end

input - recebe uma entrda:
ex:
	input nome = ('Qual e o seu nome')
	
	if -> nome == 'Joao'
	begin
	show('Ola Joao')
	else
	begin 
	show('Voce nao e o Joao')
	end

func - definir funcoes
ex:
	func nova_funcao()
	begin
	show('hello')
	end

until - loop 
ex:
	until -> x == 10
	begin
	x++ 1
	show(x)
	end

wait - esperar em segundos
ex:
    wait(2)//espere 2 segundos
    show("hello")

import - importar bibliotecas
ex:
	import -> minha_biblioteca

//Operadores 

+ - adicao
- - subtracao
* - multiplicaÃ§ao
/ - divisao
> - maoir
= - igual
>= - maior ou igual
< - menr
=< - menor ou igual
sqrt -raiz
!= - diferente
**-exponenciaçao


//Regras

1.O '=' nao pode ser usado em if,elif,while,until e for em vez disso use '==' paras igual 
2.E obrigatorio usar o begin e end ao usar if,elif,while,until para delimitaÃ§ao do bloco de codigo 
3.dar espaco depois de func
4.nao usar as palavras-chave para nomear variaveis
'''

novidades = '''


//Notas da v5

*LM posssui extensao para Notepad++

//Notas da v6

*Agora os arquivos compilados ja nao tem .lm no nome
*Agora a criacao de um directorio para aqrquivos compilados
*criaçoes de funcoes com func
*importacoes com -> 
*Criaçao da LM IDE

//Notas da v7
*Arquivos compilados em directorio especifico
*criaçao da biblioteca padrao lmlib com recursos como wait,raz
*importaçao obrigatoria da biblioteca padrao
'''

def sair():
        docs_window.destroy()
        
docs_window = Tk()
docs_window.title('Docs')
docs_window.geometry('600x400')
docs_window.config(bg='white')
docs_label = Text(docs_window,height=25,wrap="word", undo=True)
docs_label.pack(expand=True,fill=BOTH,side='top')
docs_label.insert('1.0',doc)

frame = Frame(docs_window)
frame.pack(side='bottom',fill='x')
       
docs_button = Button(frame,text='Close',command=sair)
docs_button.pack(side='right')

scroll = Scrollbar(docs_label)
docs_label.config(yscrollcommand=scroll.set)
scroll.config(command=docs_label.yview)
scroll.pack(side="right", fill="y")

docs_window.mainloop()
