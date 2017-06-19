import extrai
import earley

#Imprime a gramatica
def imprimeGramatica(Gramatica):
	print 'G = {V,T,P,S}, onde:\n'
	print 'V = ',Gramatica[0],'\n'
	print 'T = ',Gramatica[1],'\n'
    
	print 'P = {'
	P = Gramatica[2]
	for prod in P:
		producoes = ""
		for simbolo in prod[1:len(prod)]:
			producoes=producoes+simbolo+' '
		print prod[0],'>',producoes

	print '  }\nS = ',Gramatica[3],'\n'
	return;


# Pede o nome do arquivo com a gramatica
nome_arq = str(raw_input("Insira o nome do arquivo: "))

if not('.txt' in nome_arq):
    nome_arq = nome_arq + '.txt'
	
gram = extrai.leGramatica(nome_arq)
imprimeGramatica(gram)

frase = str(raw_input("\nPor favor, insira uma sentenca com terminais pertencentes a gramatica: "))
sent = earley.terminaisSentenca(frase,gram)
while sent == -1:
	frase = str(raw_input("\nPor favor, insira uma sentenca com terminais pertencentes a gramatica: "))
	sent = earley.terminaisSentenca(frase,gram)

#sent possui uma lista com os terminais da sentenca a se determinar se faz parte da gramatica

#d0=earley.etapa1(gram)
