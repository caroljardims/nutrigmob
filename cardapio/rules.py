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
	cardapios = Cardapio_Prep.objects.filter(dia__id=c.dia.id)
	
	prepals = map(lambda ca: map(lambda pa: pa.alimento, Prep_Alimentos.objects.filter(prep__id=ca.prep.id)), cardapios)
	als = []
	for p in prepals:
		#print(','.join(map(lambda a: a.desc, p)))
		als += p
	passou = len(set([x for x in als if als.count(x) > 2])) == 0
	if passou:
		c.r1 = 1
		c.save()
	#print(passou)