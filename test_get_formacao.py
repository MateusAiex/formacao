import unittest
import json
import os
import formacao

class TestGetFormacao(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_formacao.json"
        formacao.PATH = self.test_file
        self.test_data = [{"id": 1, "nome": "Test", "cursos": [1, 2, 3]}]
        with open(self.test_file, 'w') as f:
            json.dump(self.test_data, f)
        formacao.lista_formacoes = self.test_data.copy()

    def tearDown(self):
        os.remove(self.test_file)

    def test_get_formacao_exists_active(self):
        result, data = formacao.get_formacao(1)
        self.assertEqual(result, formacao.OPERACAO_REALIZADA_COM_SUCESSO)
        self.assertEqual(data, self.test_data[0])

    def test_get_formacao_exists_inactive(self):
        formacao.formacoes_deletadas.append(self.test_data[0])
        result, data = formacao.get_formacao(1)
        self.assertEqual(result, formacao.FORMACAO_NAO_ATIVO)
        self.assertEqual(data, self.test_data[0])

    def test_get_formacao_not_exists(self):
        result, data = formacao.get_formacao(2)
        self.assertEqual(result, formacao.FORMACAO_NAO_ENCONTRADO)
        self.assertIsNone(data)

if __name__ == '__main__':
    unittest.main()