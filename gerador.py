import string
import random

#Retorna todas as regras que partem de onde o marcador da regrant aponta
def geraRegras(gram,regrant):
	regras=[]
	for gprod in gram[2]:										
		if regrant[0][0][regrant[1]] == gprod[0][0] and (not (gprod in regras)):	
			regras.append(gprod)										
	return regras;
	
	
	
	
#Dado um conjunto de producoes, escolhe uma delas aleatoriamente, considerando os pesos
#Retorna com marcador apontando pra primeira posicao apos o simbolo da esquerda
def sorteio(conjunto):	
	if len(conjunto)>1:																										
		maior=0																												
		for part in conjunto:				#Encontrando qual eh a maior quantidade de casas decimais						
			if len(part[1])-2 > maior:		#																				
				maior=len(part[1])-2 		#																				
		urna=[]																												
		for part in conjunto:																								
			prob = int(float(part[1]) * (10**maior))#Adiciona a producao um numero de vezes proporcional ao seu peso		
			for i in range(0,prob):					#																		
				urna.append(part)					#																		
		index = random.randint(0, len(urna)-1)	#Gera indice aleatorio														
		aux = [urna[index],1]																																															#
	else:																													
		aux = [conjunto[0],1]																								
	return aux;																											


def geraSentencaAux(gram,regra):
	sentenca=""
	while regra[1]<len(regra[0][0])-1:
		if regra[0][0][regra[1]] in gram[0]:		#Se o proximo termo da regra for uma variavel
			dr=geraRegras(gram,regra)
			novaRegra=sorteio(dr)
			sentenca+=geraSentencaAux(gram,novaRegra)
			
			regra[1]+=1
		else:
			sentenca+=regra[0][0][regra[1]]
			regra[1]+=1
	
	return sentenca;
	
	
def geraSentenca(gram):
	urna=[]
	for prod in gram[2]: 			#Para todas as producoes na gramatica	
		if prod[0][0] == gram[3]:		#Caso a variavel a esquerda seja o simbolo inicial
			urna.append(prod)			#Adiciona para o conjunto
	inicial=sorteio(urna)
	
	sentenca=""
	while inicial[1]<len(inicial[0][0])-1: 				#Enquanto a regra inicial nao tiver sido terminada de se analisar
		if inicial[0][0][inicial[1]] in gram[0]:		#Se o proximo termo da regra inicial for uma variavel
			dr=geraRegras(gram,inicial)						#Gera as regras que partem da variavel a ser processada
			novaRegra=sorteio(dr)							#Seleciona uma dessas regras
			sentenca+=geraSentencaAux(gram,novaRegra)		#Concatena o pedaco de sentenca produzida por essa regra a sentenca anterior
			
			inicial[1]+=1									#Avanca o marcador
		else:											#Se o proximo termo da regra inicial for um terminal
			sentenca+=inicial[0][0][inicial[1]]			#Adiciona o terminal a sentenca
			inicial[1]+=1								#Avanca o marcador
	return sentenca;