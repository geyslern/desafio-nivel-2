from django.db import models
from cidades.core.models import Estado, Cidade

def test_estado():
    estado = Estado()
    assert estado is not None

def test_cidade():
    cidade = Cidade()
    assert cidade is not None

def test_estado_nome():
    estado = Estado()
    estado.nome = 'Paraná'
    assert estado.nome == 'Paraná'

def test_estado_sigla():
    estado = Estado()
    estado.sigla = 'PR'
    assert estado.sigla == 'PR'

def test_cidade_nome():
    cidade = Cidade()
    cidade.nome = 'Curitiba'
    assert cidade.nome == 'Curitiba'

def test_estado_cidade_str():
    estado = Estado(nome='Paraná', sigla='PR')
    cidade = Cidade(nome='Curitiba', estado=estado)
    assert str(cidade) == 'Curitiba - PR'

def test_estado_cidade_repr():
    estado = Estado(nome='Paraná', sigla='PR')
    cidade = Cidade(nome='Curitiba', estado=estado)
    assert repr(cidade) == 'Curitiba - PR'