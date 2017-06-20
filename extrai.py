import string

#Remove os caracteres ' ', '\n', '\t', '[' e ']', e comentarios ('#' seguido de qualquer sequencia de caracteres)
def limpaLinha(linha):
	linha = linha.replace(' ', '')
	linha = linha.replace('\n', '')
	linha = linha.replace('\t', '')
	linha = linha.replace('[', '')
	linha = linha.replace(']', '')
	
	i = linha.find('#')
	if i != (-1):
		linha=linha[0:i] #Elimina comentario
		
	return linha;

#Semelhante a limpaLinha, mas separa os elementos da string (serve para as producoes)
def leProducao(linha):
	producao=[]

	linha = linha.replace(' ', '')
	linha = linha.replace('\n', '')
	linha = linha.replace('\t', '')
	linha = linha.replace('[', '')
	#Nao elimina ']', para separar as variaveis/terminais que sao produzidos
	
	i = linha.find('#')
	if i != (-1):
		linha=linha[0:i] #Elimina comentario
	
	i = linha.find('>')
	producao.append(linha[0:i-1]) #Insere a variavel a esquerda
	
	dir=linha[i+1:len(linha)] #Dir possui as producoes da variavel a esquerda, separadas por ']'
	
	i=1
	while i != (-1):
		i = dir.find(']')
		if i != (-1):
			producao.append(dir[0:i]) #Insere variavel/terminal
			dir = dir[i+1:len(dir)]
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
		if linha[0]!='[':
			tipo = linha[0]
		else:
			if tipo == 'V':
				V.append(limpaLinha(linha))
			elif tipo == 'T':
				T.append(limpaLinha(linha))
			elif tipo == 'R':
				P.append(leProducao(linha))
			else:
				S=limpaLinha(linha)
	Gramatica = [V,T,P,S]
	return Gramatica;