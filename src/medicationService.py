from src.storage import load_data, save_data

def adicionar_medicamento(nome, horario):
    if not nome or not horario:
        raise ValueError("Nome e horário são obrigatórios")

    data = load_data()

    med = {
        "nome": nome,
        "horario": horario,
        "tomado": False
    }

    data.append(med)
    save_data(data)
    return med

def listar_medicamentos():
    return load_data()

def marcar_como_tomado(nome):
    data = load_data()

    for med in data:
        if med["nome"] == nome:
            med["tomado"] = True
            save_data(data)
            return True

    return False