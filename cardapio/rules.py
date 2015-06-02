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
	
	for card in cardapios:
		if passou:
			card.r1 = 1
		else:
			card.r1 = 0
		card.save()
	#print(passou)

def regra2(c):
	cardapios = Cardapio_Prep.objects.filter(dia__id=c.dia.id)
	
	cores = (map(lambda ca: ca.prep.cor, cardapios)) 
	aux = []
	for p in cores:
		#print(','.join(map(lambda a: a.desc, p)))
		aux.append(p) 
	
	passou = len(set([x for x in aux if aux.count(x) > 2])) == 0
	
	for card in cardapios:
		if passou:
			card.r2 = 1
		else:
			card.r2 = 0
		card.save()

"""

 Regra 7: Preparação rica em sódio
 > Verificar se preparação é rica em sódio

 """

def regra7(c):
	cardapios = Cardapio_Prep.objects.filter(dia__id=c.dia.id)

	ricoEmSodio = (map(lambda ca: ca.prep.sodio, cardapios)) 
	passou = None
	if 1 in ricoEmSodio:
		passou = 0
	else:
		passou = 1
	for card in cardapios:
		card.r7 = passou
		card.save()

def regra8(c):
	cardapios = Cardapio_Prep.objects.filter(dia__id=c.dia.id)

	ricoEmEnxofre = (map(lambda ca: ca.prep.enxofre, cardapios)) 
	passou = None
	if 1 in ricoEmEnxofre:
		passou = 0
	else:
		passou = 1
	for card in cardapios:
		card.r8 = passou
		card.save()

<<<<<<< HEAD
def regra4(c):
	cardapios = Cardapio_Prep.objects.filter(dia__id=c.dia.id)
	possuiCarneGordurosa = map(lambda ca: map(lambda pa: pa.alimento.cat_alimento.desc, Prep_Alimentos.objects.filter(prep__id=ca.prep.id)), cardapios)
	possuiCarneGordurosa  = filter(lambda ca: "Carne Gordurosa" in ca, possuiCarneGordurosa)
	passou = len(possuiCarneGordurosa) == 0
	if passou:
		passou = 1
	else:
		passou = 0
	for card in cardapios:
		card.r4 = passou
		card.save()
	print(passou)
=======
def regra10(c):
	cardapios = Cardapio_Prep.objects.filter(dia__id=c.dia.id)
	
	cocs = (map(lambda ca: ca.prep.coccao, cardapios)) 
	ccs = []
	for p in cocs:
		#print(','.join(map(lambda a: a.desc, p)))
		ccs += p
	passou = len(set([x for x in ccs if ccs.count(x) > 1])) == 0
	
	for card in cardapios:
		if passou:
			card.r10 = 1
		else:
			card.r10 = 0
		card.save()
>>>>>>> 824120e24201177aea705411b9e95257f2fd22fa

def regras(c):
	regra1(c)
	regra2(c)
	regra7(c)
<<<<<<< HEAD
	regra4(c)
	regra8(c)

=======
	regra8(c)
	regra10(c)
>>>>>>> 824120e24201177aea705411b9e95257f2fd22fa
