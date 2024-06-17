import unittest
import formacao

class TestGetFormacoes(unittest.TestCase):
    def setUp(self):
        formacao.lista_formacoes = []
        formacao.formacoes_deletadas = []

    def test_no_formacoes(self):
        self.assertEqual(formacao.get_formacoes(), (formacao.OPERACAO_REALIZADA_COM_SUCESSO, []))

    def test_all_formacoes_deleted(self):
        formacao.lista_formacoes.append({"id": 1, "nome": "Formacao1", "cursos": [1, 2, 3]})
        formacao.formacoes_deletadas.append(formacao.lista_formacoes[0])
        self.assertEqual(formacao.get_formacoes(), (formacao.OPERACAO_REALIZADA_COM_SUCESSO, []))

    def test_no_formacoes_deleted(self):
        formacao.lista_formacoes.append({"id": 1, "nome": "Formacao1", "cursos": [1, 2, 3]})
        self.assertEqual(formacao.get_formacoes(), (formacao.OPERACAO_REALIZADA_COM_SUCESSO, [formacao.lista_formacoes[0]]))

    def test_some_formacoes_deleted(self):
        formacao.lista_formacoes.append({"id": 1, "nome": "Formacao1", "cursos": [1, 2, 3]})
        formacao.lista_formacoes.append({"id": 2, "nome": "Formacao2", "cursos": [4, 5, 6]})
        formacao.formacoes_deletadas.append(formacao.lista_formacoes[0])
        self.assertEqual(formacao.get_formacoes(), (formacao.OPERACAO_REALIZADA_COM_SUCESSO, [formacao.lista_formacoes[1]]))

if __name__ == '__main__':
    unittest.main()