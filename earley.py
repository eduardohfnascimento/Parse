import string

#Dada uma sentenca, retorna uma lista com os terminais da gramatica presentes na sentenca, em ordem
#Ignora espacos em branco adicionais entre os terminais
#Caso na sentenca haja um terminal nao pertencente a gramatica, retorna -1
def terminaisSentenca(sent,gram):
	sentenca=[]
	i=0
	n=len(sent)
	erro = False
	
	while i<len(sent) and (not erro):
		while sent[i]==' ' and i<len(sent):
			i+=1
		f=i
		while f<n and sent[f]!=' ':
			f+=1
		palavra=sent[i:f]
		if palavra in gram[1]: 			#Se a palavra pertence aos terminais da Gramatica
			sentenca.append(palavra)	#Adiciona aos terminais da sentenca
			i=f+1					#Na proxima iteracao, i comeca apos o final da ultima palavra
		else:
			erro=True
	
	if(erro):
		return -1
	else:
		return sentenca