import extrai
import gerador

#Imprime a gramatica
def printGramatica(Gramatica):
	print 'G = {V,T,P,S}, onde:\n'
	print 'V = ',Gramatica[0],'\n'
	print 'T = ',Gramatica[1],'\n'
    
	print 'P = {'
	P = Gramatica[2]
	for prod in P:
		producoes = ""
		for ind in range(1,len(prod[0])-1):
			producoes=producoes+prod[0][ind]+' '
		print prod[0][0],'>',producoes

	print '  }\nS = ',Gramatica[3],'\n'
	return;


# Pede o nome do arquivo com a gramatica
nome_arq = str(raw_input("Insira o nome do arquivo: "))

if not('.txt' in nome_arq):
    nome_arq = nome_arq + '.txt'
	
gram = extrai.leGramatica(nome_arq)
#printGramatica(gram)




laco = True
while laco:
        print gerador.geraSentenca(gram),'\n\n\n'
        teste = str(raw_input("Deseja criar nova sentenca? (Pressione enter para criar, escreva qualquer coisa e pressione enter para sair)"))
        if teste != '':
                laco = False
