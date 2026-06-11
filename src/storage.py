"""Camada de armazenamento usando Supabase."""

import os
from supabase import create_client

SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "")


def get_client():
    """Retorna o cliente Supabase."""
    return create_client(SUPABASE_URL, SUPABASE_KEY)


def load_data():
    """Busca todos os medicamentos do banco de dados."""
    try:
        client = get_client()
        resposta = client.table("medicamentos").select("*").execute()
        return resposta.data
    except Exception:
        return []


def save_data(data):
    """Substitui todos os dados no banco (uso interno)."""
    pass


def inserir_medicamento(nome, horario):
    """Insere um novo medicamento no banco."""
    client = get_client()
    client.table("medicamentos").insert({
        "nome": nome,
        "horario": horario,
        "tomado": False
    }).execute()


def marcar_tomado_db(nome):
    """Marca um medicamento como tomado no banco."""
    client = get_client()
    client.table("medicamentos").update(
        {"tomado": True}
    ).eq("nome", nome).execute()
