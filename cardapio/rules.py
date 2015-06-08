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

def regra3(c):
	cardapios = Cardapio_Prep.objects.filter(dia__id=c.dia.id)
	
	prepals = map(lambda ca: map(lambda pa: pa.alimento, Prep_Alimentos.objects.filter(prep__id=ca.prep.id)), cardapios)
	cardapios = Cardapio_Prep.objects.filter(dia__id=c.dia.id)
	possuiCarneGordurosa = map(lambda ca: map(lambda pa: pa.alimento.cat_alimento.desc, Prep_Alimentos.objects.filter(prep__id=ca.prep.id)), cardapios)
	possuiCarneGordurosa  = filter(lambda ca: "Carne Gordurosa" in ca, possuiCarneGordurosa)
	possuiDoce = map(lambda ca: map(lambda pa: pa.alimento.cat_alimento.desc, Prep_Alimentos.objects.filter(prep__id=ca.prep.id)), cardapios)
	possuiDoce  = filter(lambda ca: "Doce" in ca, possuiDoce)
	possuiFritura = (map(lambda ca: ca.prep.coccao, cardapios)) 
	possuiFritura  = filter(lambda ca: "Frito" in ca, possuiFritura)
	
	passou = None
	if len(possuiCarneGordurosa) == 0 or len(possuiFritura) == 0:
		passou = 1
	elif len(possuiDoce) == 0:
		passou = 0
	else:
		passou = 1

	for card in cardapios:
		card.r3 = passou
		card.save()

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
	#print(passou)

def regra5(c):
	cardapios = Cardapio_Prep.objects.filter(dia__id=c.dia.id)
	possuiDoce = map(lambda ca: map(lambda pa: pa.alimento.cat_alimento.desc, Prep_Alimentos.objects.filter(prep__id=ca.prep.id)), cardapios)
	possuiDoce  = filter(lambda ca: "Doce" in ca, possuiDoce)
	passou = len(possuiDoce) == 0
	if passou:
		passou = 1
	else:
		passou = 0
	for card in cardapios:
		card.r5 = passou
		card.save()

def regra6(c):
	cardapios = Cardapio_Prep.objects.filter(dia__id=c.dia.id)
	possuiFritura = (map(lambda ca: ca.prep.coccao, cardapios)) 
	possuiFritura  = filter(lambda ca: "Frito" in ca, possuiFritura)
	passou = len(possuiFritura) == 0
	if passou:
		passou = 1
	else:
		passou = 0
	for card in cardapios:
		card.r6 = passou
		card.save()


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

def regras(c):
	regra1(c)
	regra2(c)
	regra3(c)
	regra7(c)
	regra4(c)
	regra5(c)
	regra6(c)
	regra8(c)
	regra10(c)
