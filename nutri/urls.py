from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'projeto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'cardapio.views.home', name='home'),
    url(r'^index/', 'cardapio.views.index', name='index'),
    # AUX
    url(r'^aux/', 'cardapio.views.aux', name='aux'),
    url(r'^addaux/', 'cardapio.views.addaux', name='addaux'),
    url(r'editaux/(?P<id_aux>\d+)/$', 'cardapio.views.editaux', name='editaux'),
    url(r'deleteaux/(?P<id_aux>\d+)/$', 'cardapio.views.deleteaux', name='deleteaux'),
    # ALIMENTOS
    url(r'^alimentos/', 'cardapio.views.alimentos', name='alimentos'),
    url(r'^addalimento/', 'cardapio.views.addalimento', name='addalimento'),
    url(r'veralimento/(?P<id_alimentos>\d+)/$', 'cardapio.views.veralimento', name='veralimento'),
    url(r'deletealimento/(?P<id_alimentos>\d+)/$', 'cardapio.views.deletealimento', name='deletealimento'),
    url(r'editalimento/(?P<id_alimentos>\d+)/$', 'cardapio.views.editalimento', name='editalimento'),
    # PREPARA
    url(r'^prepara/', 'cardapio.views.prepara', name='prepara'),
    url(r'^addprepara/', 'cardapio.views.addprepara', name='addprepara'),
    url(r'verprepara/(?P<id_prepara>\d+)/$', 'cardapio.views.verprepara', name='verprepara'),
    url(r'deleteprepara/(?P<id_prepara>\d+)/$', 'cardapio.views.deleteprepara', name='deleteprepara'),
    url(r'editprepara/(?P<id_prepara>\d+)/$', 'cardapio.views.editprepara', name='editprepara'),
    url(r'prep_alimentos/(?P<id_prepara>\d+)/$', 'cardapio.views.prep_alimentos', name='prep_alimentos'),
    # CARDAPIOS
    url(r'^cardapios/$', 'cardapio.views.cardapios', name='cardapios'),
    url(r'^addcardapio/', 'cardapio.views.addcardapio', name='addcardapio'),
    url(r'vercardapio/(?P<id_dia_cardapio>\d+)/$', 'cardapio.views.vercardapio', name='vercardapio'),
    url(r'deletecardapio/(?P<id_dia_cardapio>\d+)/$', 'cardapio.views.deletecardapio', name='deletecardapio'),
    url(r'editcardapio/(?P<id_dia_cardapio>\d+)/$', 'cardapio.views.editcardapio', name='editcardapio'),
    url(r'prep_cardapio/(?P<id_dia_cardapio>\d+)/$', 'cardapio.views.prep_cardapio', name='prep_cardapio'),

 ]
