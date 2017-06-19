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
		
def etapa1(gram):
	d0=[]
	for prod in gram[2]: 			#Para todas as producoes na gramatica
		if prod[0] == gram[3]:		#Caso a variavel a esquerda seja o simbolo inicial
			aux=[prod,1]		#Insere em d0, com marcador na primeira posicao
			d0.append(aux)		#
	
	aumentou = True
	while aumentou:
		aumentou=False
		for dprod in d0:												#Para todas as producoes em d0
			for gprod in gram[2]:										#Para todas as producoes da gramatica
				aux=[gprod,1]
				if dprod[0][1] == gprod[0] and (not (aux in d0)):		#Se um marcador apontar para a mesma variavel a esquerda dessa producao da gramatica, e essa producao nao estiver incluida em d0
					d0.append(aux)										#Adiciona a d0
					aumentou=True										#d0 aumentou
			
	return d0;