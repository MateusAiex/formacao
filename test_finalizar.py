import unittest
import json
import os
import formacao

class TestFinalizar(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_formacao.json"
        formacao.PATH = self.test_file
        self.test_data = [{"id": 1, "nome": "Test", "cursos": [1, 2, 3]}]
        with open(self.test_file, 'w') as f:
            json.dump(self.test_data, f)
        formacao.lista_cursos = self.test_data.copy()

    def tearDown(self):
        os.remove(self.test_file)

    def test_finalizar(self):
        result = formacao.finalizar()
        self.assertEqual(result, formacao.OPERACAO_REALIZADA_COM_SUCESSO)
        with open(self.test_file, 'r') as f:
            data = json.load(f)
        self.assertEqual(data, self.test_data)

if __name__ == '__main__':
    unittest.main()