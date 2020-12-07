import unittest

import sorteio

class TestSorteio(unittest.TestCase):
    def test_atribuir_numero_sorteado(self):
        def gerar_numero():
            for i in range(0, 100):
                yield i
        generator = gerar_numero()
        def sorteador():
            return next(generator)

        for i in range(0, 100):
            candidato = {}
            sorteio.sortear_numero_candidato(candidato, sorteador)
            self.assertEqual(i, candidato['numero_sorteado'])

    def test_atribuir_numeros_sorteados_lista(self):
        def gerar_numero():
            for i in range(0, 100):
                yield i
        generator = gerar_numero()
        def sorteador():
            return next(generator)

        candidatos = []
        for i in range(0, 100):
            candidato = {}
            candidatos.append(candidato)

        sorteio.sortear_numeros_candidatos(candidatos, sorteador)

        for i in range(0, 100):
            candidato = candidatos[i]
            self.assertEqual(i, candidato['numero_sorteado'])
