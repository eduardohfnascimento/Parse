import string

#Retorna uma variavel, terminal ou o simbolo inicial, descartando as demais informacoes da linha
def limpaLinha(linha):
	i = linha.find('[')
	j = linha.find(']')
		
	return linha[i+2:j-1]; #Ignora os colchetes e o espaco depois do primeiro e o antes do segundo

#Semelhante a limpaLinha, mas separa os elementos da string (serve para as producoes)
def leProducao(linha):
	producao=[]

	i = linha.find('#')
	if i != (-1):
		linha=linha[0:i] #Elimina comentario
	
	i=linha.find('[')
	j=linha.find(']')
	producao.append(linha[i+2:j-1]) #Insere a variavel a esquerda
	
	i = linha.find('>')
	
	dir=linha[i+1:len(linha)] #Dir possui as producoes da variavel a esquerda
	
	i=1
	while i != (-1):
		i = dir.find('[')
		j = dir.find(']')
		if i != (-1) and j != (-1):
			producao.append(dir[i+2:j-1]) #Insere variavel/terminal
			dir = dir[j+1:len(dir)]
	producao.append('\\')
	return producao;
	
#Extrai a gramatica contida em um arquivo
#Retorna um array com 4 elementos, sendo eles:
#[V,T,P,S], onde:
#V: array com as variaveis da gramatica
#T: array com os terminais da gramatica
#P: array de arrays, com as producoes da gramatica, sendo que o primeiro elemento eh a variavel a esquerda, e os demais a producao desta variavel
#S: string, simbolo inicial da gramatica
def leGramatica(nomeArq):
	arq = open(nomeArq,'r')
	V=[]
	T=[]
	P=[]
	S=""
	
	tipo=''
	arquivo = arq.readlines()
	arq.close()
	for linha in arquivo:
		if linha[0]!='[' and linha[0]!='#':		# Caso a linha seja um comentario, ignora o seu conteudo
			tipo = linha[0]
		else:
			if tipo == 'V' and linha[0]!='#': 	#
				V.append(limpaLinha(linha))
			elif tipo == 'T' and linha[0]!='#': #
				T.append(limpaLinha(linha))
			elif tipo == 'R' and linha[0]!='#': #
				P.append(leProducao(linha))
			else:
				if linha[0]!='#':				#
					S=limpaLinha(linha)
	Gramatica = [V,T,P,S]
	return Gramatica;