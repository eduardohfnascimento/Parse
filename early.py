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
		if sent[i]=='"':
			f=i+1
			while f<n and sent[f] != '"':
				f+=1
			palavra=sent[i+1:f]
		else:
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
		
#Imprime um conjunto Dr do algoritmo de Early		
def printDr(dr,r):
	print 'D',r,' ='
	for prod in dr:
		fim = True
		aux=""
		for i in range(1,len(prod[0])-1):
			if prod[1] == i:	#Coloca '*' onde o marcador aponta
				aux=aux+'*'		#
				fim = False
			aux=aux+prod[0][i]+' '
		if fim:
			print prod[0][0],'>',aux,'*/',prod[2]
		else:
			print prod[0][0],'>',aux,'/',prod[2]
	print ' '
	return;
		
#Primeira etapa do algoritmo de Early
#Conjunto D0 possui elementos no formato:
#[producao, marcador, conjunto], onde
#producao: producao da gramatica
#marcador: determina que ponto da producao esta sendo analisada (no caso, sempre inicializado em 1)
#conjunto: determina em qual conjunto esse elemento foi inserido pela primeira vez (no caso, sempre inicializado em 0, d0)
def etapa1(gram):
	d0=[]
	for prod in gram[2]: 			#Para todas as producoes na gramatica
		if prod[0] == gram[3]:		#Caso a variavel a esquerda seja o simbolo inicial
			aux=[prod,1,0]		#Insere em d0, com marcador na primeira posicao, conjunto 0
			d0.append(aux)		#
	
	aumentou = True
	while aumentou:
		aumentou=False
		for dprod in d0:												#Para todas as producoes em d0
			for gprod in gram[2]:										#Para todas as producoes da gramatica
				aux=[gprod,1, 0]
				if dprod[0][1] == gprod[0] and (not (aux in d0)):		#Se um marcador apontar para a mesma variavel a esquerda dessa producao da gramatica, e essa producao nao estiver incluida em d0
					d0.append(aux)										#Adiciona a d0
					aumentou=True										#d0 aumentou
	printDr(d0,0)		
	return d0;
	
#Segunda etapa do algoritmo de Early
#Conjuntos Dr seguem a mesma estrutura da etapa anterior
def etapa2(d0,sent,gram):
	drs=[d0]
	dr=[]
	for r in range(1,len(sent)+1):
		dr=[]
		for prod in drs[r-1]:						#Para todas as producoes do conjunto anterior
			if prod[0][prod[1]] == sent[r-1]:		#Se elas produzirem o terminal em questao
				aux = [prod[0],prod[1]+1,prod[2]]	#Adiciona ao novo conjunto, movendo o marcador
				dr.append(aux)						#
		
		aumentou = True
		while aumentou:
			aumentou = False
			for dprod in dr:
				for gprod in gram[2]:
					aux=[gprod,1,r]
					if dprod[0][dprod[1]] == gprod[0] and (not (aux in dr)):
						dr.append(aux)
						aumentou = True
			for dprod in dr:
				if dprod[1] == len(dprod[0])-1: 			#Se o marcador estiver no final da regra
					for prodant in drs[dprod[2]]:			#Vai no grupo em que essa regra foi criada
						aux=[prodant[0],prodant[1]+1,prodant[2]]
						if dprod[0][0]==prodant[0][prodant[1]] and (not (aux in dr)):
							dr.append(aux)
							aumentou = True
		printDr(dr,r)
		drs.append(dr)
		
	return dr;
	
#Funcao principal do algoritmo de Early
#Chama as duas etapas, e verifica se sent pertence a gram
#Retorna True caso pertenca, False caso contrario
def early(sent,gram):
	d0=etapa1(gram)
	dr=etapa2(d0,sent,gram)
	aceita = False
	for prod in dr:
		if prod[0][0] == gram[3] and prod[1] == len(prod[0])-1 and prod[2] == 0: 	#Respectivamente: Parte do simbolo inicial da gramatica; Analisou toda a regra; Foi criada no conjunto inicial
			aceita = True
	return aceita;