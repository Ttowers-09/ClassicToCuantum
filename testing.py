import unittest
import numpy as np
import math
import sistemascuanticos as mt

class TestSistemasCuanticos(unittest.TestCase):

    def test_sistema_determinista(self):
        v = np.array([1, 0, 0, 0, 0, 0])
        m = np.array([[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0]])
        clicks = 2
        expected = np.array([0, 0, 0, 1, 0, 0])
        result = mt.sistema_determinista(v, m, clicks)
        np.testing.assert_almost_equal(result, expected)

        v = np.array([1, 0, 0, 0, 0, 0])
        m = np.array([[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1],[0, 1, 0, 0, 0, 0]])
        clicks = 2
        expected = np.array([0, 0, 0, 0, 0, 1])
        result = mt.sistema_determinista(v, m, clicks)
        np.testing.assert_almost_equal(result, expected)

    def test_sistema_probabilistico(self):
        v2 = np.array ([1,0,0,0,0,0,0,0,0,0,0])
        m2 = np.array ([[0,0,0,0,0,0,0,0,0,0,0],[1/3,0,0,0,0,0,0,0,0,0,0],[1/3,0,0,0,0,0,0,0,0,0,0],[1/3,0,0,0,0,0,0,0,0,0,0],[0,1/3,0,0,1,0,0,0,0,0,0],[0,1/3,0,0,0,1,0,0,0,0,0], [0,1/3,1/3,0,0,0,1,0,0,0,0],[0,0,1/3,0,0,0,0,1,0,0,0],[0,0,1/3,1/3,0,0,0,0,1,0,0],[0,0,0,1/3,0,0,0,0,0,1,0],[0,0,0,1/3,0,0,0,0,0,0,1]])
        clicks = 2
        expected = np.array([0, 0, 0, 0, 0.11111111, 0.11111111,0.2222222,0.11111111,0.2222222,0.11111111,0.11111111])
        result = mt.sistema_probabilistico(v2, m2, clicks)
        np.testing.assert_almost_equal(result, expected)

        v2 = np.array([1, 0, 0])
        m2 = np.array([[0,2/5,3/5],[1/5,2/5,2/5],[4/5,1/5,0]])
        clicks = 2
        expected = np.array([0.56, 0.4, 0.04])
        result = mt.sistema_probabilistico(v2, m2, clicks)
        np.testing.assert_almost_equal(result, expected)

    def test_sistema_cuantico(self):
        v3 = np.array([1, 0, 0, 0, 0, 0, 0, 0])
        m3 = np.array(
            [[0, 0, 0, 0, 0, 0, 0, 0], [1 / math.sqrt(2), 0, 0, 0, 0, 0, 0, 0], [1 / math.sqrt(2), 0, 0, 0, 0, 0, 0, 0],
             [0, complex(-1, 1) / math.sqrt(6), 0, 1, 0, 0, 0, 0],
             [0, complex(-1, -1) / math.sqrt(6), 0, 0, 1, 0, 0, 0],
             [0, complex(1, -1) / math.sqrt(6), complex(-1, 1) / math.sqrt(6), 0, 0, 1, 0, 0],
             [0, 0, complex(-1, -1) / math.sqrt(6), 0, 0, 0, 1, 0],
             [0, 0, complex(1, -1) / math.sqrt(6), 0, 0, 0, 0, 1]])
        clicks = 2
        expected = np.array([complex(0,0),complex(0,0),complex(0,0),complex(-0.28867513, 0.28867513),complex(-0.28867513, -0.28867513),complex(0,0),complex(-0.28867513, -0.28867513),complex(0.28867513, -0.28867513)])
        result = mt.sistema_cuantico(v3, m3, clicks)
        np.testing.assert_almost_equal(result, expected)

        v3 = np.array([1, 0, 0])
        m3 = np.array([[1 / math.sqrt(2), 1 / math.sqrt(2), 0], [complex(0, -1 / math.sqrt(2)), complex(0, 1 / math.sqrt(2)), 0],[0, 0, complex(0, 1)]])
        clicks = 2
        expected = np.array([complex(0.5,-0.5), complex(0.5,-0.5), complex(0,0)])
        result = mt.sistema_cuantico(v3, m3, clicks)
        np.testing.assert_almost_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
