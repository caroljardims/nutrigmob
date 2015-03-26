# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.template import Context, loader
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.forms.models import modelformset_factory
from cardapio.models import *
from cardapio.forms import *
from cardapio.rules import *

    #############
    #           #
    #   Index   #
    #           #
    #############

def index(request):
	Aux(desc='dsdsds', tipo=1)
	context = {}
	return render_to_response('index.html', context)

def home(request):
	nome = "Cardapio"
	context = {'nome':nome}
	return render_to_response('index.html', context)


    ############################
    #                          #
    #   CRUD Tabela Auxiliar   #
    #                          #
    ############################


def aux(request):
	aux_list = Aux.objects.all().order_by('desc')
	context = {'aux_list':aux_list}
	return render_to_response('aux.html', context)

def addaux(request):
	f = modelformset_factory(Aux,AuxForm)
	form = f(request.POST or None)
	if request.method == 'POST':
		f_tipo = request.POST.get('tipo')
		f_desc = request.POST.get('desc')
		auxiliar = Aux(tipo=f_tipo, desc= f_desc)
		auxiliar.save()
		return redirect('/aux')
	context = {'form': form}
	return render(request,"addaux.html", context)

def deleteaux(request,id_aux):
   aux = Aux.objects.get(pk=id_aux).delete()
   context = {'aux':aux}
   return render(request,"delete.html", context)

def editaux(request, id_aux):
	f = modelformset_factory(Aux,AuxForm)
	form = f(request.POST or None)
	aux = get_object_or_404(Aux, pk=id_aux)

	if request.method == 'POST':
		f_tipo = request.POST.get('tipo')
		f_desc = request.POST.get('desc')
		
		aux = get_object_or_404(Aux, pk=id_aux)
		if f_tipo: aux.tipo = f_tipo
		if f_desc: aux.desc = f_desc
		aux.save()
		return redirect('/aux')
	context = {'form': form, 'aux':aux}
	return render(request,"editaux.html", context)


    #############################
    #                           #
    #   CRUD Tabela Alimentos   #
    #                           #
    #############################


def alimentos(request):
	al_list = Alimentos.objects.all().order_by('desc')
	context = {'al_list':al_list}
	return render_to_response('alimentos.html', context)

def addalimento(request):
	aux_list = Aux.objects.all().order_by('desc')
	f = modelformset_factory(Alimentos,AlimentosForm)
	form = f(request.POST or None)
	if request.method == 'POST':
		f_categoria = request.POST.get('categoria')
		f_desc = request.POST.get('desc')
		f_cor = request.POST.get('cor')
		alimento = Alimentos(cat_alimento_id=f_categoria, desc= f_desc, cor=f_cor)
		alimento.save()
		return redirect('/alimentos')
	context = {'form': form, 'aux_list':aux_list}
	return render(request,"addalimento.html", context)

def veralimento(request, id_alimentos):
	al = get_object_or_404(Alimentos, pk=id_alimentos)
	context = {'al':al}
	return render(request,"veralimento.html", context)

def deletealimento(request,id_alimentos):
   alimento = Alimentos.objects.get(pk=id_alimentos).delete()
   context = {'alimento':alimento}
   return render(request,"delete.html", context)

def editalimento(request, id_alimentos):
	aux_list = Aux.objects.all().order_by('desc')
	f = modelformset_factory(Aux,AuxForm)
	form = f(request.POST or None)
	al = get_object_or_404(Alimentos, pk=id_alimentos)

	if request.method == 'POST':
		f_categoria = request.POST.get('categoria')
		f_desc = request.POST.get('desc')
		f_cor = request.POST.get('cor')

		al = get_object_or_404(Alimentos, pk=id_alimentos)
		if f_categoria: al.cat_alimento_id = f_categoria
		if f_desc: al.desc = f_desc
		if f_cor: al.cor = f_cor
		al.save()
		return redirect('/alimentos')
	context = {'form': form, 'aux_list':aux_list, 'al':al}
	return render(request,"editalimento.html", context)




	###########################
    #                         #
    #   CRUD Tabela Prepara   #
    #                         #
    ###########################


def prepara(request):
	p_list = Prepara.objects.all().order_by('desc')
	aux_list = Aux.objects.all()
	context = {'p_list':p_list,'aux_list':aux_list}
	return render_to_response('prepara.html', context)

def addprepara(request):
	aux_list = Aux.objects.all().order_by('desc')
	f = modelformset_factory(Alimentos,AlimentosForm)
	form = f(request.POST or None)
	if request.method == 'POST':
		f_desc = request.POST.get('desc')
		f_inNatura = request.POST.get('inNatura')
		f_enxofre = request.POST.get('enxofre')
		f_sodio = request.POST.get('sodio')
		f_tipo = request.POST.get('tipo')
		f_coccao = request.POST.get('coccao')
		f_cor = request.POST.get('cor')
		prepara = Prepara(desc=f_desc,inNatura=f_inNatura,enxofre=f_enxofre,sodio=f_sodio,tipoPrep=f_tipo,coccao=f_coccao,cor=f_cor)
		prepara.save()
		return redirect('/prepara')
	context = {'form': form, 'aux_list':aux_list}
	return render(request,"addprepara.html", context)

def verprepara(request, id_prepara):
	p = get_object_or_404(Prepara, pk=id_prepara)
	al_list = Alimentos.objects.all().order_by('desc')
	lista = Prep_Alimentos.objects.all().order_by('desc')
	prep_al_list = []
	contem_list = []
	for o in lista:
		if o.desc == p.desc:
			prep_al_list.append(o)
	for x in prep_al_list:
		contem_list.append(x.alimento)

	context = {'p':p,'lista':contem_list}
	return render(request,"verprepara.html", context)

def deleteprepara(request,id_prepara):
   prepara = Prepara.objects.get(pk=id_prepara).delete()
   context = {'prepara':prepara}
   return render(request,"delete.html", context)

def editprepara(request, id_prepara):
	aux_list = Aux.objects.all().order_by('desc')
	f = modelformset_factory(Aux,AuxForm)
	form = f(request.POST or None)
	al = get_object_or_404(Prepara, pk=id_prepara)

	if request.method == 'POST':
		f_desc = request.POST.get('desc')
		f_inNatura = request.POST.get('inNatura')
		f_enxofre = request.POST.get('enxofre')
		f_sodio = request.POST.get('sodio')
		f_tipo = request.POST.get('tipo')
		f_coccao = request.POST.get('coccao')
		f_cor = request.POST.get('cor')

		al = get_object_or_404(Prepara, pk=id_prepara)
		if f_tipo: al.tipoPrep = f_tipo
		if f_coccao: al.coccao = f_coccao
		if f_inNatura: al.inNatura = f_inNatura
		if f_enxofre: al.enxofre = f_enxofre
		if f_sodio: al.sodio = f_sodio
		if f_desc: al.desc = f_desc
		if f_cor: al.cor = f_cor
		al.save()
		return redirect('/prepara')
	context = {'form': form, 'aux_list':aux_list, 'al':al}
	return render(request,"editprepara.html", context)


	#############################
    #                           #
    #   Tabela Prep Alimentos   #
    #                           #
    #############################


def prep_alimentos(request,id_prepara):
	al_list = Alimentos.objects.all().order_by('desc')
	prepara = get_object_or_404(Prepara, pk=id_prepara)
	lista = Prep_Alimentos.objects.all().order_by('desc')
	lista1 = Prep_Alimentos.objects.all().order_by('desc')
	prep_al_list = []
	contem_list = []

	for o in lista:
		if o.desc == prepara.desc:
			prep_al_list.append(o)
	for p in prep_al_list:
		contem_list.append(p.alimento)
	
	lista = list(set(al_list)-set(contem_list))

	f = modelformset_factory(Prep_Alimentos,PrepAlimentosForm)
	form = f(request.POST or None)
	

	if request.method == 'POST' and 'add' in request.POST:
		f_alimento = request.POST.get('alimento')
		f_desc = prepara.desc
		f_prep = id_prepara
		PrepAl = Prep_Alimentos(prep_id=f_prep, desc= f_desc, alimento_id= f_alimento)
		PrepAl.save()
		return redirect('/prep_alimentos/' + id_prepara)

	if request.method == 'POST' and 'delete' in request.POST:
		f_alimento = request.POST.get('alimento')
		for a in lista1:
			if a.alimento.desc == f_alimento and a.prep.desc == prepara.desc:
				a.delete()
				return redirect('/prep_alimentos/' + id_prepara)
		
	context = {'form': form,'lista':lista,'p':prepara,'prep_al_list':prep_al_list,'contem_list':contem_list}
	return render(request,"prep-alimentos.html", context)


	#######################
    #                     #
    #   Tabela Cardapio   #
    #                     #
    #######################


def cardapios(request):
	c_list = Dia_Cardapio.objects.all().order_by('dia')
	card = Cardapio_Prep.objects.all()
	mes = []
	for i in range(0,12): mes.append(i+1)
	for j in card: 
		regra1(j)
	context = {'c_list':c_list,'mes':mes}
	return render_to_response('cardapios.html', context)


def addcardapio(request):
	f = modelformset_factory(Dia_Cardapio,DiaCardapioForm)
	form = f(request.POST or None)
	if request.method == 'POST':
		f_dia = request.POST.get('dia')
		f_mes = request.POST.get('mes')
		dia = Dia_Cardapio(dia=f_dia,mes=f_mes,ano=2015)
		dia.save()
		return redirect('/cardapios')
	context = {'form': form}
	return render(request,"addcardapio.html", context)


def vercardapio(request,id_dia_cardapio):
	card = Cardapio_Prep.objects.all()
	c = get_object_or_404(Dia_Cardapio, pk=id_dia_cardapio)
	p_card = []
	for p in card:
		if p.dia.dia == c.dia and p.dia.mes == c.mes and p.dia.ano == c.ano:
			p_card.append(p)

	context = {'p_card':p_card,'c':c}
	return render(request,"vercardapio.html",context)


def deletecardapio(request,id_dia_cardapio):
   dia = Dia_Cardapio.objects.get(pk=id_dia_cardapio).delete()
   context = {'dia':dia}
   return render(request,"delete.html", context)

def editcardapio(request,id_dia_cardapio):
	f = modelformset_factory(Dia_Cardapio,DiaCardapioForm)
	form = f(request.POST or None)
	if request.method == 'POST':
		f_dia = request.POST.get('dia')
		f_mes = request.POST.get('mes')
		data = f_dia + '/' + f_mes
		print data
		c = get_object_or_404(Dia_Cardapio, pk=id_dia_cardapio)
		if f_dia and f_mes:
			c.dia = f_dia
			c.mes = f_mes
			c.save()
			return redirect('/cardapios')
	context = {'form': form}
	return render(request,"editcardapio.html", context)

def prep_cardapio(request,id_dia_cardapio):
	c = get_object_or_404(Dia_Cardapio, pk=id_dia_cardapio)
	prepara = Prepara.objects.all()
	lista = Cardapio_Prep.objects.all()
	lista1 = Cardapio_Prep.objects.all()
	card_list = []
	contem_list = []

	for o in lista:
		if o.dia.dia == c.dia and o.dia.mes == c.mes and o.dia.ano == c.ano:
			card_list.append(o)
	for p in card_list:
		contem_list.append(p.prep)

	lista = list(set(prepara)-set(contem_list))

	f = modelformset_factory(Cardapio_Prep,CardapioPrepForm)
	form = f(request.POST or None)

	if request.method == 'POST' and 'add' in request.POST:
		f_prep = request.POST.get('prep')
		card = Cardapio_Prep(prep_id=f_prep,dia_id=id_dia_cardapio,r1=0,r2=0,r3_1=0,r3_2=0,r4=0,r5=0,r6=0,r7=0,r8=0,r9=0,r10=0)
		card.save()
		return redirect('/prep_cardapio/' + id_dia_cardapio)

	if request.method == 'POST' and 'delete' in request.POST:
		f_prep = request.POST.get('prep')
		for a in lista1:
			if a.prep.desc == f_prep and a.dia.dia == c.dia and a.dia.mes == c.mes and a.dia.ano == c.ano:
				a.delete()
				return redirect('/prep_cardapio/' + id_dia_cardapio)
		
	context = {'form': form,'lista':lista,'c':c,'card_list':card_list,'contem_list':contem_list}
	return render(request,"prep-cardapio.html", context)