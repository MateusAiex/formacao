import unittest
import json
import os
import formacao

class TestFormacao(unittest.TestCase):
    def setUp(self):
        self.temp_file = "temp.json"
        with open(self.temp_file, 'w') as f:
            f.write('[]')
        formacao.PATH = self.temp_file

    def tearDown(self):
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)

    def test_inicializar_success(self):
        result = formacao.inicializar()
        self.assertEqual(result, formacao.OPERACAO_REALIZADA_COM_SUCESSO)

    def test_inicializar_file_not_found(self):
        os.remove(self.temp_file)
        result = formacao.inicializar()
        self.assertEqual(result, formacao.ARQUIVO_NAO_ENCONTRADO)

    def test_inicializar_invalid_format(self):
        with open(self.temp_file, 'w') as f:
            f.write('not json')
        result = formacao.inicializar()
        self.assertEqual(result, formacao.ARQUIVO_EM_FORMATO_INVALIDO)

if __name__ == '__main__':
    unittest.main()