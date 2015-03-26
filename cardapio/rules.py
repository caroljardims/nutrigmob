# -*- coding:utf-8 -*-

from cardapio.models import *

"""

 > criar regras de pontos dos cardápios do dia
 > cada regra será de valor booleano, sendo validadas apenas se a preparação seguir sua condição
 > ao final, os pontos serão somados e indicarão a classificação da qualidade de cada prato:
 > muito satisfatório .... ]8__10]
 > satisfatório .......... ]6__8]
 > insatisfatório ........ ]5__6]
 > muito insatisfatório .. ]0__5] 

"""


	##############
    #            #
    #   REGRAS   #
    #            #
    ##############

"""

 Regra 1: Alimentos repetidos
 > Contar em grupo os Alimentos.
 > Se contador > 1, então FALSE 

 """

def regra1(c):
	cardapio = Cardapio_Prep.objects.all()
	lista = []
	#print str(c.dia.dia) + "/" + str(c.dia.mes)
	for i in cardapio:
		if i.dia.id == c.dia.id:
			lista.append(i)
	for l in lista:
		print l.dia.dia