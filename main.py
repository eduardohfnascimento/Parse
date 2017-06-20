import extrai
import early

#Imprime a gramatica
def printGramatica(Gramatica):
	print 'G = {V,T,P,S}, onde:\n'
	print 'V = ',Gramatica[0],'\n'
	print 'T = ',Gramatica[1],'\n'
    
	print 'P = {'
	P = Gramatica[2]
	for prod in P:
		producoes = ""
		for simbolo in prod[1:len(prod)-1]:
			producoes=producoes+simbolo+' '
		print prod[0],'>',producoes

	print '  }\nS = ',Gramatica[3],'\n'
	return;


# Pede o nome do arquivo com a gramatica
nome_arq = str(raw_input("Insira o nome do arquivo: "))

if not('.txt' in nome_arq):
    nome_arq = nome_arq + '.txt'
	
gram = extrai.leGramatica(nome_arq)
printGramatica(gram)

laco = True
while laco:
	frase = str(raw_input("\nPor favor, insira uma sentenca com terminais pertencentes a gramatica: "))
	sent = early.terminaisSentenca(frase,gram)
	while sent == -1:
		frase = str(raw_input("Por favor, insira uma sentenca com terminais pertencentes a gramatica: "))
		sent = early.terminaisSentenca(frase,gram)

	aceita=early.early(sent,gram)
	if aceita:
		print 'Faz parte da gramatica!'
	else:
		print 'Nao faz parte da gramatica...'
	
	teste = str(raw_input("Deseja testar nova sentenca? (N para sair)"))
	if teste == 'N' or teste == 'n':
		laco = False