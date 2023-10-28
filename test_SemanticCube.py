import unittest
from SemanticCube import Type, Operator, cube

class TestSemanticCube(unittest.TestCase):
    
    def test_int_float(self):
        self.assertEqual(cube[Type.INT.value][Type.FLOAT.value][Operator.PLUS.value], Type.FLOAT)
        self.assertEqual(cube[Type.INT.value][Type.FLOAT.value][Operator.MINUS.value], Type.FLOAT)
        self.assertEqual(cube[Type.INT.value][Type.FLOAT.value][Operator.TIMES.value], Type.FLOAT)
        self.assertEqual(cube[Type.INT.value][Type.FLOAT.value][Operator.DIVIDE.value], Type.FLOAT)
        self.assertEqual(cube[Type.INT.value][Type.FLOAT.value][Operator.EQUAL.value], Type.ERROR)
        self.assertEqual(cube[Type.INT.value][Type.FLOAT.value][Operator.NOT_EQUAL.value], Type.ERROR)
        
    def test_float_int(self):
        self.assertEqual(cube[Type.FLOAT.value][Type.INT.value][Operator.PLUS.value], Type.FLOAT)
        self.assertEqual(cube[Type.FLOAT.value][Type.INT.value][Operator.MINUS.value], Type.FLOAT)
        self.assertEqual(cube[Type.FLOAT.value][Type.INT.value][Operator.TIMES.value], Type.FLOAT)
        self.assertEqual(cube[Type.FLOAT.value][Type.INT.value][Operator.DIVIDE.value], Type.FLOAT)
        self.assertEqual(cube[Type.FLOAT.value][Type.INT.value][Operator.EQUAL.value], Type.ERROR)
        self.assertEqual(cube[Type.FLOAT.value][Type.INT.value][Operator.NOT_EQUAL.value], Type.ERROR)
        
    def test_int_int(self):
        self.assertEqual(cube[Type.INT.value][Type.INT.value][Operator.PLUS.value], Type.INT)
        self.assertEqual(cube[Type.INT.value][Type.INT.value][Operator.MINUS.value], Type.INT)
        self.assertEqual(cube[Type.INT.value][Type.INT.value][Operator.TIMES.value], Type.INT)
        self.assertEqual(cube[Type.INT.value][Type.INT.value][Operator.DIVIDE.value], Type.INT)
        self.assertEqual(cube[Type.INT.value][Type.INT.value][Operator.EQUAL.value], Type.BOOL)
        self.assertEqual(cube[Type.INT.value][Type.INT.value][Operator.NOT_EQUAL.value], Type.BOOL)
        
    def test_float_float(self):
        self.assertEqual(cube[Type.FLOAT.value][Type.FLOAT.value][Operator.PLUS.value], Type.FLOAT)
        self.assertEqual(cube[Type.FLOAT.value][Type.FLOAT.value][Operator.MINUS.value], Type.FLOAT)
        self.assertEqual(cube[Type.FLOAT.value][Type.FLOAT.value][Operator.TIMES.value], Type.FLOAT)
        self.assertEqual(cube[Type.FLOAT.value][Type.FLOAT.value][Operator.DIVIDE.value], Type.FLOAT)
        self.assertEqual(cube[Type.FLOAT.value][Type.FLOAT.value][Operator.EQUAL.value], Type.BOOL)
        self.assertEqual(cube[Type.FLOAT.value][Type.FLOAT.value][Operator.NOT_EQUAL.value], Type.BOOL)
        
    def test_bool_bool(self):
        self.assertEqual(cube[Type.BOOL.value][Type.BOOL.value][Operator.PLUS.value], Type.ERROR)
        self.assertEqual(cube[Type.BOOL.value][Type.BOOL.value][Operator.MINUS.value], Type.ERROR)
        self.assertEqual(cube[Type.BOOL.value][Type.BOOL.value][Operator.TIMES.value], Type.ERROR)
        self.assertEqual(cube[Type.BOOL.value][Type.BOOL.value][Operator.DIVIDE.value], Type.ERROR)
        self.assertEqual(cube[Type.BOOL.value][Type.BOOL.value][Operator.EQUAL.value], Type.BOOL)
        self.assertEqual(cube[Type.BOOL.value][Type.BOOL.value][Operator.NOT_EQUAL.value], Type.BOOL)
        
if __name__ == '__main__':
    unittest.main()