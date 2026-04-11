import pytest
import os
from src.medicationService import adicionar_medicamento, marcar_como_tomado
from src.storage import FILE

@pytest.fixture(autouse=True)
def limpar():
    if os.path.exists(FILE):
        os.remove(FILE)
    yield
    if os.path.exists(FILE):
        os.remove(FILE)

def test_adicionar():
    med = adicionar_medicamento("Dipirona", "08:00")
    assert med["nome"] == "Dipirona"

def test_invalido():
    with pytest.raises(ValueError):
        adicionar_medicamento("", "")

def test_marcar():
    adicionar_medicamento("Paracetamol", "12:00")
    assert marcar_como_tomado("Paracetamol") is True