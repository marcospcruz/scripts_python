import os, sys
from stat import *
from datetime import date,datetime
import time, datetime

EOL_CHAR="\n"

COLUNAS=[
	'Approved',
	'Blocked Balance',
	'Cross-reading',
	'Duplicated',
	'Invalid Data'
]
linhas=[]
logContent=[]
logDic={}

	
def readFile(filePath):
	arquivo=open(filePath,'r')
	texto=arquivo.readlines()
	trn_qt=0
	i=0
	while i<len(texto):
		line=texto[i]
		linhas.append(line)
		i+=1

'''
Function responsible to log the information in a list
'''
def writeLog(line):
	logContent.append(line)
	
	
def saveLog():
	now=datetime.datetime.now()
	year=now.year
	month=now.month
	day=now.day
	hour=now.hour
	minute=now.minute
	second=now.second
	filename=str(year)+str(month)+str(day)+str(hour)+str(minute)+str(second)+".log"
	file=open(filename,'w')
	file.write(convertListToString(logContent))
	file.close()

def convertListToString(lista):
	retorno=""
	for line in lista:
		#print(lista[line])
		retorno+=line+'\n'
	return retorno

def separaColunas():

	for indiceColuna in range(0,len(COLUNAS)):
		coluna=COLUNAS[indiceColuna]

		for  i in range(0,len(linhas)):
			linha=linhas[i]
			key=extraiValorColuna(';',1,linha)
			if i==0:
				continue
			if logDic.has_key(key):
				row=logDic[key]
			else:
				row=['0','0','0','0','0']

			coluna2=extraiValorColuna(';',2,linha)
			if coluna2==coluna:
				#row.insert(indiceColuna,extraiValorColuna(';',3,linha))
				row[indiceColuna]=extraiValorColuna(';',3,linha)
				logDic[key]=row






def extraiValorColuna(separador,indiceColuna,string):
	initPosicao=0
	stringTemp=''
	coluna=1
	for caractere in string:

		if caractere==separador or caractere==EOL_CHAR:
			if indiceColuna==coluna:
				return stringTemp
			coluna+=1
			stringTemp=''
			continue

		stringTemp+=caractere

def geraCSV():
	label='passage time;'
	for colLabel in COLUNAS:
		label+=colLabel+';'
	logContent.append(label)

	for key in sorted(logDic):
		linha=key+';'
		row=logDic[key]
		#
		for valor in row:
			linha+=valor+';'
		logContent.append(linha)
		linha=''


readFile('d:\\sgmp_compensation_20160121.csv')
separaColunas()
geraCSV()
saveLog()