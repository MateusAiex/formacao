import unittest
import json
import os
import formacao

class TestAddFormacao(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_formacao.json"
        formacao.PATH = self.test_file
        self.test_data = [{"id": 1, "nome": "Test", "cursos": [1, 2, 3]}]
        with open(self.test_file, 'w') as f:
            json.dump(self.test_data, f)
        formacao.lista_formacoes = self.test_data.copy()

    def tearDown(self):
        os.remove(self.test_file)

    def test_add_formacao_success(self):
        result, id = formacao.add_formacao("Test2", [4, 5, 6])
        self.assertEqual(result, formacao.OPERACAO_REALIZADA_COM_SUCESSO)
        self.assertIn({"id": 2, "nome": "Test2", "cursos": [4, 5, 6]}, formacao.lista_formacoes)

    def test_add_formacao_duplicate(self):
        result, id = formacao.add_formacao("Test", [1, 2, 3])
        self.assertEqual(result, formacao.OPERACAO_REALIZADA_COM_SUCESSO)
        self.assertEqual(formacao.lista_formacoes.count({"id": 1, "nome": "Test", "cursos": [1, 2, 3]}), 1)

if __name__ == '__main__':
    unittest.main()