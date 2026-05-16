"""Testes de integração com a API ViaCEP."""

import unittest
from unittest.mock import patch, MagicMock
import json
from src.api import consultar_cep, formatar_endereco


class TestConsultarCep(unittest.TestCase):

    def test_cep_invalido_letras(self):
        """CEP com letras deve retornar None."""
        resultado = consultar_cep("abcdefgh")
        self.assertIsNone(resultado)

    def test_cep_invalido_curto(self):
        """CEP com menos de 8 dígitos deve retornar None."""
        resultado = consultar_cep("0131")
        self.assertIsNone(resultado)

    def test_cep_invalido_vazio(self):
        """CEP vazio deve retornar None."""
        resultado = consultar_cep("")
        self.assertIsNone(resultado)

    @patch("src.api.urllib.request.urlopen")
    def test_cep_valido_retorna_dados(self, mock_urlopen):
        """CEP válido deve retornar dicionário com os dados do endereço."""
        dados_falsos = {
            "cep": "01310-100",
            "logradouro": "Avenida Paulista",
            "bairro": "Bela Vista",
            "localidade": "São Paulo",
            "uf": "SP"
        }
        mock_cm = MagicMock()
        mock_cm.__enter__ = MagicMock(return_value=mock_cm)
        mock_cm.__exit__ = MagicMock(return_value=False)
        mock_cm.read.return_value = json.dumps(dados_falsos).encode("utf-8")
        mock_urlopen.return_value = mock_cm

        resultado = consultar_cep("01310100")

        self.assertIsNotNone(resultado)
        self.assertEqual(resultado["localidade"], "São Paulo")
        self.assertEqual(resultado["uf"], "SP")

    @patch("src.api.urllib.request.urlopen")
    def test_cep_inexistente_retorna_none(self, mock_urlopen):
        """CEP inexistente (API retorna erro) deve retornar None."""
        dados_falsos = {"erro": True}
        mock_cm = MagicMock()
        mock_cm.__enter__ = MagicMock(return_value=mock_cm)
        mock_cm.__exit__ = MagicMock(return_value=False)
        mock_cm.read.return_value = json.dumps(dados_falsos).encode("utf-8")
        mock_urlopen.return_value = mock_cm

        resultado = consultar_cep("99999999")
        self.assertIsNone(resultado)


class TestFormatarEndereco(unittest.TestCase):

    def test_formata_endereco_completo(self):
        """Endereço completo deve ser formatado corretamente."""
        dados = {
            "logradouro": "Avenida Paulista",
            "bairro": "Bela Vista",
            "localidade": "São Paulo",
            "uf": "SP",
            "cep": "01310-100"
        }
        resultado = formatar_endereco(dados)
        self.assertIn("Avenida Paulista", resultado)
        self.assertIn("São Paulo", resultado)
        self.assertIn("SP", resultado)

    def test_formata_endereco_parcial(self):
        """Endereço sem bairro não deve quebrar."""
        dados = {
            "localidade": "Brasília",
            "uf": "DF",
            "cep": "70040-010"
        }
        resultado = formatar_endereco(dados)
        self.assertIn("Brasília", resultado)
        self.assertIn("DF", resultado)


if __name__ == "__main__":
    unittest.main()
