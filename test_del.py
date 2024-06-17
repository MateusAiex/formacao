import unittest
import formacao

class TestDelFormacao(unittest.TestCase):
    def setUp(self):
        formacao.lista_formacoes = []
        formacao.formacoes_deletadas = []

    def test_del_formacao_success(self):
        formacao.lista_formacoes.append({"id": 1, "nome": "Formacao1", "cursos": [1, 2, 3]})
        self.assertEqual(formacao.del_formacao(1), (formacao.OPERACAO_REALIZADA_COM_SUCESSO, 1))
        self.assertIn(formacao.lista_formacoes[0], formacao.formacoes_deletadas)
        self.assertIn(formacao.lista_formacoes[0], formacao.lista_formacoes)

    def test_del_formacao_not_found(self):
        self.assertEqual(formacao.del_formacao(1), (formacao.FORMACAO_NAO_ENCONTRADO, 1))

    def test_del_formacao_already_deleted(self):
        formacao.lista_formacoes.append({"id": 1, "nome": "Formacao1", "cursos": [1, 2, 3]})
        formacao.del_formacao(1)
        self.assertEqual(formacao.del_formacao(1), (formacao.FORMACAO_NAO_ATIVO, 1))

if __name__ == '__main__':
    unittest.main()