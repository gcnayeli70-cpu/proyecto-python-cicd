import pytest
from main import calcular_area


def test_area_valores_enteros():
    assert calcular_area(5, 4) == 20


def test_area_valores_decimales():
    assert calcular_area(2.5, 4) == pytest.approx(10.0)


def test_base_negativa():
    with pytest.raises(ValueError):
        calcular_area(-5, 4)


def test_altura_cero():
    with pytest.raises(ValueError):
        calcular_area(5, 0)


def test_cuadrado():
    assert calcular_area(3, 3) == 9
