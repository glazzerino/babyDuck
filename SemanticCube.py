from enum import Enum
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
    ASSIGN = 6
    LESS_THAN = 7
    GREATER_THAN = 8
    IF_FALSE = 9
    GOTO = 10
    PARAM = 11
    CALL = 12
    PRINT = 13
    PRINT_NEWLINE = 14
    LABEL = 15


def parse_operator(operator: str):
    if operator == "+":
        return Operator.PLUS
    elif operator == "-":
        return Operator.MINUS
    elif operator == "*":
        return Operator.TIMES
    elif operator == "/":
        return Operator.DIVIDE
    elif operator == "==":
        return Operator.EQUAL
    elif operator == "!=":
        return Operator.NOT_EQUAL
    elif operator == "=":
        return Operator.ASSIGN
    elif operator == "<":
        return Operator.LESS_THAN
    elif operator == ">":
        return Operator.GREATER_THAN
    elif operator == "if_false":
        return Operator.IF_FALSE
    elif operator == "goto":
        return Operator.GOTO
    elif operator == "param":
        return Operator.PARAM
    elif operator == "call":
        return Operator.CALL
    elif operator == "print":
        return Operator.PRINT
    elif operator == "print_newline":
        return Operator.PRINT_NEWLINE
    elif operator == "label":
        return Operator.LABEL
    else:
        raise Exception("Invalid operator: {}".format(operator))
    
def parse_string_to_type(data_type: Type, data: str):
    if data_type == Type.INT:
        return int(data)
    elif data_type == Type.FLOAT:
        return float(data)
    elif data_type == Type.CHAR:
        return data[0]
    elif data_type == Type.BOOL:
        return data.lower() == "true"
    elif data_type == Type.STRING:
        return data
    else:
        raise Exception("Invalid data type: {}".format(data_type))
    
def parse_string(data: str):
    try:
        return int(data)
    except ValueError:
        pass
    try:
        return float(data)
    except ValueError:
        pass
    if data.lower() == "true":
        return True
    elif data.lower() == "false":
        return False
    else:
        return data
    
def baby_duck_type_to_enum(baby_duck_type: str):
    if baby_duck_type == "int":
        return Type.INT
    elif baby_duck_type == "float":
        return Type.FLOAT
    elif baby_duck_type == "char":
        return Type.CHAR
    elif baby_duck_type == "bool":
        return Type.BOOL
    elif baby_duck_type == "void":
        return Type.VOID
    elif baby_duck_type == "str":
        return Type.STRING
    elif baby_duck_type == "error":
        return Type.ERROR
    else:
        raise Exception("Invalid type: {}".format(baby_duck_type))
    

    
# Semantic Cube. 
# Specifices the result of an operation between two operands.
# The result is determined by the type of the operands and the operator.

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

