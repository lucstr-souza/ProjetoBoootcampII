"""Testes do serviço de medicamentos com mock do Supabase."""

import unittest
from unittest.mock import patch, MagicMock
from src.medicationService import (
    adicionar_medicamento,
    listar_medicamentos,
    marcar_como_tomado,
)


class TestAdicionarMedicamento(unittest.TestCase):

    @patch("src.armazenamento.get_client")
    def test_adiciona_medicamento_valido(self, mock_client):
        """Medicamento válido deve ser adicionado com sucesso."""
        mock_table = MagicMock()
        mock_client.return_value.table.return_value = mock_table
        mock_table.insert.return_value.execute.return_value = None

        resultado = adicionar_medicamento("Paracetamol", "08:00")
        self.assertEqual(resultado["nome"], "Paracetamol")
        self.assertEqual(resultado["horario"], "08:00")

    def test_adiciona_medicamento_nome_vazio(self):
        """Nome vazio deve lançar exceção."""
        with self.assertRaises(ValueError):
            adicionar_medicamento("", "08:00")

    def test_adiciona_medicamento_horario_vazio(self):
        """Horário vazio deve lançar exceção."""
        with self.assertRaises(ValueError):
            adicionar_medicamento("Paracetamol", "")


class TestListarMedicamentos(unittest.TestCase):

    @patch("src.armazenamento.get_client")
    def test_lista_medicamentos(self, mock_client):
        """Deve retornar lista de medicamentos do banco."""
        mock_data = [
            {"nome": "Paracetamol", "horario": "08:00", "tomado": False},
            {"nome": "Ibuprofeno", "horario": "12:00", "tomado": True},
        ]
        mock_client.return_value.table.return_value\
            .select.return_value.execute.return_value\
            = MagicMock(data=mock_data)

        resultado = listar_medicamentos()
        self.assertEqual(len(resultado), 2)
        self.assertEqual(resultado[0]["nome"], "Paracetamol")

    @patch("src.armazenamento.get_client")
    def test_lista_vazia(self, mock_client):
        """Deve retornar lista vazia quando não há medicamentos."""
        mock_client.return_value.table.return_value\
            .select.return_value.execute.return_value\
            = MagicMock(data=[])

        resultado = listar_medicamentos()
        self.assertEqual(resultado, [])


class TestMarcarComoTomado(unittest.TestCase):

    @patch("src.armazenamento.get_client")
    def test_marca_medicamento_existente(self, mock_client):
        """Medicamento existente deve ser marcado como tomado."""
        mock_data = [{"nome": "Paracetamol", "horario": "08:00", "tomado": False}]
        mock_client.return_value.table.return_value\
            .select.return_value.execute.return_value\
            = MagicMock(data=mock_data)
        mock_client.return_value.table.return_value\
            .update.return_value.eq.return_value\
            .execute.return_value = None

        resultado = marcar_como_tomado("Paracetamol")
        self.assertTrue(resultado)

    @patch("src.armazenamento.get_client")
    def test_marca_medicamento_inexistente(self, mock_client):
        """Medicamento inexistente deve retornar False."""
        mock_client.return_value.table.return_value\
            .select.return_value.execute.return_value\
            = MagicMock(data=[])

        resultado = marcar_como_tomado("Remedionaoexiste")
        self.assertFalse(resultado)


if __name__ == "__main__":
    unittest.main()
