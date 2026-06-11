"""Interface web do MediReminder usando Flask."""

import os
from flask import Flask, render_template_string, request, redirect
from src.medicationService import (
    adicionar_medicamento,
    listar_medicamentos,
    marcar_como_tomado,
)
from src.api import consultar_cep, formatar_endereco

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>MediReminder</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 40px auto; padding: 0 20px; }
        h1 { color: #2D6A4F; }
        form { margin-bottom: 20px; padding: 15px; background: #D8F3DC; border-radius: 8px; }
        input { padding: 6px; margin: 4px; }
        button { padding: 6px 12px; background: #2D6A4F; color: white; border: none; border-radius: 4px; cursor: pointer; }
        ul { list-style: none; padding: 0; }
        li { padding: 8px; border-bottom: 1px solid #ddd; }
        .tomado { color: green; }
        .pendente { color: #F4845F; }
        a { color: #2D6A4F; }
    </style>
</head>
<body>
    <h1>💊 MediReminder</h1>

    <form method="POST" action="/adicionar">
        <strong>Adicionar medicamento</strong><br>
        Nome: <input name="nome" required>
        Horário: <input name="horario" placeholder="08:00" required>
        <button type="submit">Adicionar</button>
    </form>

    <h2>Medicamentos cadastrados</h2>
    <ul>
    {% for m in medicamentos %}
        <li>
            <strong>{{ m['nome'] }}</strong> — {{ m['horario'] }}
            {% if m['tomado'] %}
                <span class="tomado">[Tomado ✔]</span>
            {% else %}
                <span class="pendente">[Pendente ✘]</span>
                — <a href="/tomado/{{ m['nome'] }}">Marcar como tomado</a>
            {% endif %}
        </li>
    {% else %}
        <li>Nenhum medicamento cadastrado ainda.</li>
    {% endfor %}
    </ul>

    <hr>

    <h2>Consultar CEP do paciente</h2>
    <form method="GET" action="/cep">
        CEP: <input name="cep" placeholder="01310100" required>
        <button type="submit">Consultar</button>
    </form>

    {% if endereco %}
        <p><strong>Endereço encontrado:</strong><br>{{ endereco }}</p>
    {% elif endereco is not none and cep_buscado %}
        <p>CEP não encontrado.</p>
    {% endif %}

</body>
</html>
"""


@app.route("/")
def index():
    medicamentos = listar_medicamentos()
    return render_template_string(TEMPLATE, medicamentos=medicamentos, endereco=None, cep_buscado=False)


@app.route("/adicionar", methods=["POST"])
def adicionar():
    nome = request.form.get("nome")
    horario = request.form.get("horario")
    adicionar_medicamento(nome, horario)
    return redirect("/")


@app.route("/tomado/<nome>")
def tomado(nome):
    marcar_como_tomado(nome)
    return redirect("/")


@app.route("/cep")
def buscar_cep():
    cep = request.args.get("cep", "")
    medicamentos = listar_medicamentos()
    dados = consultar_cep(cep)
    endereco = formatar_endereco(dados).replace("\n", "<br>") if dados else None
    return render_template_string(
        TEMPLATE, medicamentos=medicamentos, endereco=endereco, cep_buscado=True
    )
  if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
