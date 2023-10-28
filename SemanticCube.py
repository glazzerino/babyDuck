from enum import Enum

class Type(Enum):
    """Represents the type an operand can take"""
    INT = 0
    FLOAT = 1
    BOOL = 2
    ERROR = 3

class Operator(Enum):
    PLUS = 0
    MINUS = 1
    TIMES = 2
    DIVIDE = 3
    EQUAL = 4
    NOT_EQUAL = 5
    
# Semantic Cube. 
# Specifices the result of an operation between two operands.
# The result is determined by the type of the operands and the operator.
#

cube = [[[0 for k in range(10)] for j in range(10)] for i in range(10)]

# INT FLOAT
cube[Type.INT.value][Type.FLOAT.value][Operator.PLUS.value] = Type.FLOAT
cube[Type.INT.value][Type.FLOAT.value][Operator.MINUS.value] = Type.FLOAT
cube[Type.INT.value][Type.FLOAT.value][Operator.TIMES.value] = Type.FLOAT
cube[Type.INT.value][Type.FLOAT.value][Operator.DIVIDE.value] = Type.FLOAT
cube[Type.INT.value][Type.FLOAT.value][Operator.EQUAL.value] = Type.ERROR
cube[Type.INT.value][Type.FLOAT.value][Operator.NOT_EQUAL.value] = Type.ERROR

# FLOAT INT
cube[Type.FLOAT.value][Type.INT.value][Operator.PLUS.value] = Type.FLOAT
cube[Type.FLOAT.value][Type.INT.value][Operator.MINUS.value] = Type.FLOAT
cube[Type.FLOAT.value][Type.INT.value][Operator.TIMES.value] = Type.FLOAT
cube[Type.FLOAT.value][Type.INT.value][Operator.DIVIDE.value] = Type.FLOAT
cube[Type.FLOAT.value][Type.INT.value][Operator.EQUAL.value] = Type.ERROR
cube[Type.FLOAT.value][Type.INT.value][Operator.NOT_EQUAL.value] = Type.ERROR

# INT INT
cube[Type.INT.value][Type.INT.value][Operator.PLUS.value] = Type.INT
cube[Type.INT.value][Type.INT.value][Operator.MINUS.value] = Type.INT
cube[Type.INT.value][Type.INT.value][Operator.TIMES.value] = Type.INT
cube[Type.INT.value][Type.INT.value][Operator.DIVIDE.value] = Type.INT
cube[Type.INT.value][Type.INT.value][Operator.EQUAL.value] = Type.BOOL
cube[Type.INT.value][Type.INT.value][Operator.NOT_EQUAL.value] = Type.BOOL

# FLOAT FLOAT
cube[Type.FLOAT.value][Type.FLOAT.value][Operator.PLUS.value] = Type.FLOAT
cube[Type.FLOAT.value][Type.FLOAT.value][Operator.MINUS.value] = Type.FLOAT
cube[Type.FLOAT.value][Type.FLOAT.value][Operator.TIMES.value] = Type.FLOAT
cube[Type.FLOAT.value][Type.FLOAT.value][Operator.DIVIDE.value] = Type.FLOAT
cube[Type.FLOAT.value][Type.FLOAT.value][Operator.EQUAL.value] = Type.BOOL
cube[Type.FLOAT.value][Type.FLOAT.value][Operator.NOT_EQUAL.value] = Type.BOOL

# BOOL BOOL
cube[Type.BOOL.value][Type.BOOL.value][Operator.PLUS.value] = Type.ERROR
cube[Type.BOOL.value][Type.BOOL.value][Operator.MINUS.value] = Type.ERROR
cube[Type.BOOL.value][Type.BOOL.value][Operator.TIMES.value] = Type.ERROR
cube[Type.BOOL.value][Type.BOOL.value][Operator.DIVIDE.value] = Type.ERROR
cube[Type.BOOL.value][Type.BOOL.value][Operator.EQUAL.value] = Type.BOOL
cube[Type.BOOL.value][Type.BOOL.value][Operator.NOT_EQUAL.value] = Type.BOOL

