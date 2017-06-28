import extrai
import early
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
teste = str(raw_input("\nDeseja criar nova sentenca? \n-Pressione enter para criar \n-Escreva exit para sair\n"))
if teste == 'exit':
        laco = False
while laco:
        sentenca = gerador.geraSentenca(gram)
        print 'Nova sentenca:\n'
        print sentenca,'\n\n\n'
        teste = str(raw_input("\nDeseja criar nova sentenca? \n-Pressione enter para criar \n-Escreva input para testar se dada sentenca faz parte da gramatica \n-Escreva check para executar o Algoritmo de Early sobre a ultima sentenca gerada \n-Escreva exit para sair\n"))
        if teste == 'exit':
                laco = False
        if teste == 'check':
                sent = early.terminaisSentenca(sentenca,gram)
                aceita = early.early(sent,gram)
                if aceita:
                        print '\nFaz parte da gramatica!\n\n'
                        teste = str(raw_input("\nDeseja criar nova sentenca? \n-Pressione enter para criar \n-Escreva input para testar se dada sentenca faz parte da gramatica \n-Escreva check para executar o Algoritmo de Early sobre a ultima sentenca gerada \n-Escreva exit para sair\n"))
                        if teste == 'exit':
                                laco = False
        if teste == 'input':
                frase = str(raw_input("\nPor favor, insira uma sentenca com terminais pertencentes a gramatica. \nPara inserir terminais com espaco, utilize aspas(\"\"): "))
                sent = early.terminaisSentenca(frase,gram)
                while sent == -1:
                        frase = str(raw_input("Por favor, insira uma sentenca com terminais pertencentes a gramatica. \nPara inserir terminais com espaco, utilize aspas (\"\"): "))
                        sent = early.terminaisSentenca(frase,gram)
                aceita=early.early(sent,gram)
                if aceita:
                        print '\nFaz parte da gramatica!\n\n'
                else:
                        print '\nNao faz parte...\n\n'
