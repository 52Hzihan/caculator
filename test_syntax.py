import unittest
from syntax import *

class TestSyntax(unittest.TestCase):
    def test_syntax(self):
        e1 = ['1', '+', 'sin', '(', '2', ')', '-', '5434', '^', '(', 'sin', '(', 'cos', '(',  '32', '*', '3', '/', '5',')',')',')']
        e2 = ['sin','sin','23345']
        e3 = ['235','/','(','3']
        e4 = ['2','+','-', '3']
        e5 = ['2','+','(','-','3',')']
        e6 = ['52','*','6','^','(','cos','(', 'sin','3',')', ')']
        e7 = ['1','+','+','+','2']
        e8 = ['5.23', '+', '2']
        e9 = ['1', '+']
        e10 = ['(', '2', ')', '3']
        e11 = ['(', '2', '(']

        self.assertEqual(SyntaxCheck(e1), -1)
        self.assertEqual(SyntaxCheck(e2), 1)
        self.assertEqual(SyntaxCheck(e3), 3)
        self.assertEqual(SyntaxCheck(e4), -1)
        self.assertEqual(SyntaxCheck(e5), -1)
        self.assertEqual(SyntaxCheck(e6), 8)
        self.assertEqual(SyntaxCheck(e7), 2)
        self.assertEqual(SyntaxCheck(e8), -1)
        self.assertEqual(SyntaxCheck(e9), 1)
        self.assertEqual(SyntaxCheck(e10), 3)
        self.assertEqual(SyntaxCheck(e11), 2)


if __name__ == '__main__':
    unittest.main()