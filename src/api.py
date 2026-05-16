"""Integração com a API pública ViaCEP."""

import json
import urllib.request
import urllib.error


def consultar_cep(cep):
    """Consulta um CEP na API ViaCEP e retorna os dados do endereço.

    Args:
        cep: CEP no formato '01310100' ou '01310-100'.

    Returns:
        Dicionário com os dados do endereço ou None em caso de erro.
    """
    cep_limpo = cep.replace("-", "").strip()

    if len(cep_limpo) != 8 or not cep_limpo.isdigit():
        return None

    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"

    try:
        with urllib.request.urlopen(url, timeout=5) as resposta:
            dados = json.loads(resposta.read().decode("utf-8"))
            if "erro" in dados:
                return None
            return dados

    except Exception:
        return None


def formatar_endereco(dados):
    """Formata os dados do endereço em texto legível.

    Args:
        dados: Dicionário retornado por consultar_cep.

    Returns:
        String formatada com o endereço.
    """
    partes = []

    if dados.get("logradouro"):
        partes.append(f"Logradouro : {dados['logradouro']}")
    if dados.get("bairro"):
        partes.append(f"Bairro     : {dados['bairro']}")
    if dados.get("localidade") and dados.get("uf"):
        partes.append(f"Cidade/UF  : {dados['localidade']} — {dados['uf']}")
    if dados.get("cep"):
        partes.append(f"CEP        : {dados['cep']}")

    return "\n  ".join(partes)
