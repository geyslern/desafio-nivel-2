from cidades.base.apps import BaseConfig

def test_base_app_name():
    assert BaseConfig.name == 'base'