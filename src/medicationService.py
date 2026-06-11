"""Serviço de medicamentos usando Supabase."""

from src.storage import load_data, inserir_medicamento, marcar_tomado_db

def adicionar_medicamento(nome, horario):
    """Adiciona um medicamento no banco de dados."""
    if not nome or not horario:
        raise ValueError("Nome e horário são obrigatórios")
    inserir_medicamento(nome, horario)
    return {"nome": nome, "horario": horario, "tomado": False}


def listar_medicamentos():
    """Lista todos os medicamentos do banco de dados."""
    return load_data()


def marcar_como_tomado(nome):
    """Marca um medicamento como tomado."""
    data = load_data()
    for med in data:
        if med["nome"] == nome:
            marcar_tomado_db(nome)
            return True
    return False
