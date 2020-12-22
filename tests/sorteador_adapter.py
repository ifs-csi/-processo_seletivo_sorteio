import unittest

import sorteador_adapter

EXPECTATIVA_NUMEROS_SORTEADOS_SEED_0 = [
    2357136045,
    2546248240,
    3071714934,
    3626093761,
    2588848964,
    3684848380,
    2340255428,
    3638918504,
    1819583498,
    2678185684,
    2774094102,
    1650906867,
    1879422757,
    1277901400,
    3830135879,
    243580377,
    4138900057,
    1171049869,
    1646868795,
    2051556034,
    3400433127,
    3488238120,
    2271586392,
    2061486255,
    2439732825,
    1686997842,
    3975407270,
    3590930970,
    305097550,
    1449105481,
    374217482,
    2783877013,
    86837364,
    1581585361,
    3576074996,
    4110950086,
    3342157823,
    602802000,
    3736673712,
    3736996289,
    4203133779,
    2034131044,
    3432359897,
    3439885490,
    1982038772,
    2235433758,
    3352347284,
    2915765396,
    507984783,
    3095093672,
    2748439841,
    2499755970,
    615697674,
    2308000442,
    4057322112,
    3258229281,
    2241321504,
    454869707,
    1780959477,
    2034098328,
    1136257700,
    800291327,
    3325308364,
    3165039475,
    1959150776,
    930076701,
    2441405219,
    580757633,
    80701569,
    1392175013,
    2652724278,
    642848646,
    2628931111,
    954863081,
    2649711349,
    1659957522,
    4053367120,
    3876630917,
    2928395882,
    1932520491,
    1544074683,
    2633087520,
    1877037945,
    3875557634,
    2996303170,
    426405864,
    258666410,
    4165298234,
    2863741220,
    2805215079,
    2880367736,
    734051084,
    903586223,
    1538251859,
    553734236,
    3224172417,
    1354754447,
    2610612836,
    1562125878,
    1396067213,
]

EXPECTATIVA_NUMEROS_SORTEADOS_SEED_42 = [
    1608637543,
    3421126068,
    4083286877,
    787846415,
    3143890027,
    3348747336,
    2571218621,
    2563451925,
    670094951,
    1914837114,
    669991379,
    429389015,
    249467211,
    1972458955,
    3720198232,
    1433267573,
    2581769316,
    613608296,
    3041148568,
    2795544707,
    88409750,
    242285877,
    4165731074,
    3100961112,
    3575313900,
    4031053214,
    911989542,
    3344770,
    780932288,
    4261516220,
    787716373,
    2652062881,
    1306710476,
    2627030330,
    2253811734,
    30349565,
    1855189740,
    99052377,
    1250819633,
    2253890011,
    2627888187,
    1717389823,
    599121578,
    200427520,
    1254751708,
    4182248124,
    1573512144,
    999745295,
    1958805694,
    389151678,
    3372305071,
    2655947710,
    857592371,
    1642661740,
    2208620087,
    4222944500,
    2544401216,
    2004731385,
    199502979,
    3693415909,
    2609385267,
    2921898631,
    732395541,
    1934879561,
    279394471,
    56972562,
    4075432324,
    4046725721,
    4147358012,
    2419304462,
    3472040178,
    1655351290,
    1308306185,
    68574554,
    419498549,
    991681410,
    2938758484,
    1035196508,
    1890440559,
    2934594492,
    524150215,
    2619915692,
    2126768637,
    3578544904,
    147697583,
    744595491,
    3905501390,
    1679592529,
    1111451556,
    782698034,
    2845511528,
    3244252548,
    1338788866,
    1826030590,
    2233675142,
    893102646,
    2348102762,
    2438254340,
    793943862,
    134489565,
]

def sortear_numeros_array(sorteador, quantidade_numeros):
    numeros_sorteados = []
    for i in range(0, quantidade_numeros):
        numeros_sorteados.append(sorteador.sortear())
    return numeros_sorteados

class TestSorteadorAdapter(unittest.TestCase):
    def test_sortear_numero(self):
        sorteador_seed_0 = sorteador_adapter.Sorteador(0)
        sorteador_seed_42 = sorteador_adapter.Sorteador(42)

        numeros_sorteados_seed_0 = sortear_numeros_array(sorteador_seed_0, 100)
        numeros_sorteados_seed_42 = sortear_numeros_array(
            sorteador_seed_42,
            100
        )

        self.assertEqual(
            EXPECTATIVA_NUMEROS_SORTEADOS_SEED_0,
            numeros_sorteados_seed_0
        )
        self.assertEqual(
            EXPECTATIVA_NUMEROS_SORTEADOS_SEED_42,
            numeros_sorteados_seed_42
        )

    def test_sortear_numeros_paralelo(self):
        sorteador_seed_0 = sorteador_adapter.Sorteador(0)
        sorteador_seed_42 = sorteador_adapter.Sorteador(42)

        self.assertEqual(2357136045, sorteador_seed_0.sortear())
        self.assertEqual(1608637543, sorteador_seed_42.sortear())
        self.assertEqual(2546248240, sorteador_seed_0.sortear())
        self.assertEqual(3421126068, sorteador_seed_42.sortear())
