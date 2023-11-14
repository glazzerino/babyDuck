import pytest
from SemanticCube import *


def test_parse_operator():
    assert parse_operator("+") == Operator.PLUS
    assert parse_operator("-") == Operator.MINUS
    assert parse_operator("*") == Operator.TIMES
    assert parse_operator("/") == Operator.DIVIDE
    assert parse_operator("==") == Operator.EQUAL
    assert parse_operator("!=") == Operator.NOT_EQUAL
    assert parse_operator("=") == Operator.ASSIGN
    assert parse_operator("<") == Operator.LESS_THAN
    assert parse_operator(">") == Operator.GREATER_THAN
    assert parse_operator("if_false") == Operator.IF_FALSE
    assert parse_operator("goto") == Operator.GOTO
    assert parse_operator("param") == Operator.PARAM
    assert parse_operator("call") == Operator.CALL
    assert parse_operator("print") == Operator.PRINT
    assert parse_operator("print_newline") == Operator.PRINT_NEWLINE
    assert parse_operator("label") == Operator.LABEL
    assert parse_operator("gotot") == Operator.GOTOT
    assert parse_operator("gotof") == Operator.GOTOF
    with pytest.raises(Exception):
        parse_operator("invalid_operator")


def test_parse_string_to_type():
    assert parse_string_to_type(Type.INT, "10") == 10
    assert parse_string_to_type(Type.FLOAT, "3.14") == 3.14
    assert parse_string_to_type(Type.BOOL, "true") == True
    assert parse_string_to_type(Type.BOOL, "false") == False
    assert parse_string_to_type(Type.STRING, "hello") == "hello"
    with pytest.raises(Exception):
        parse_string_to_type(Type.ERROR, "invalid_data")


def test_parse_string():
    assert parse_string("10") == 10
    assert parse_string("3.14") == 3.14
    assert parse_string("true") == True
    assert parse_string("false") == False
    assert parse_string("hello") == "hello"
    assert parse_string(None) == None


def test_get_result_type():
    assert get_result_type(Type.INT, Type.INT, Operator.PLUS) == Type.INT
    assert get_result_type(Type.INT, Type.FLOAT, Operator.PLUS) == Type.FLOAT
    assert get_result_type(Type.FLOAT, Type.INT, Operator.PLUS) == Type.FLOAT
    assert get_result_type(Type.FLOAT, Type.FLOAT, Operator.PLUS) == Type.FLOAT
    assert get_result_type(Type.INT, Type.INT, Operator.EQUAL) == Type.BOOL
    assert get_result_type(Type.INT, Type.FLOAT, Operator.EQUAL) == Type.BOOL
    assert get_result_type(Type.FLOAT, Type.INT, Operator.EQUAL) == Type.BOOL
    assert get_result_type(Type.FLOAT, Type.FLOAT, Operator.EQUAL) == Type.BOOL
    assert get_result_type(Type.BOOL, Type.BOOL, Operator.EQUAL) == Type.BOOL
    assert get_result_type(Type.STRING, Type.STRING, Operator.EQUAL) == Type.BOOL
    assert get_result_type(Type.INT, Type.INT, Operator.NOT_EQUAL) == Type.BOOL
    assert get_result_type(Type.INT, Type.FLOAT, Operator.NOT_EQUAL) == Type.BOOL
    assert get_result_type(Type.FLOAT, Type.INT, Operator.NOT_EQUAL) == Type.BOOL
    assert get_result_type(Type.FLOAT, Type.FLOAT, Operator.NOT_EQUAL) == Type.BOOL
    assert get_result_type(Type.BOOL, Type.BOOL, Operator.NOT_EQUAL) == Type.BOOL
    assert get_result_type(Type.STRING, Type.STRING, Operator.NOT_EQUAL) == Type.BOOL
    assert get_result_type(Type.INT, Type.INT, Operator.LESS_THAN) == Type.BOOL
    assert get_result_type(Type.INT, Type.FLOAT, Operator.LESS_THAN) == Type.BOOL
    assert get_result_type(Type.FLOAT, Type.INT, Operator.LESS_THAN) == Type.BOOL
    assert get_result_type(Type.FLOAT, Type.FLOAT, Operator.LESS_THAN) == Type.BOOL
    assert get_result_type(Type.INT, Type.INT, Operator.GREATER_THAN) == Type.BOOL
    assert get_result_type(Type.INT, Type.FLOAT, Operator.GREATER_THAN) == Type.BOOL
    assert get_result_type(Type.FLOAT, Type.INT, Operator.GREATER_THAN) == Type.BOOL
    assert get_result_type(Type.FLOAT, Type.FLOAT, Operator.GREATER_THAN) == Type.BOOL
    with pytest.raises(Exception):
        get_result_type(Type.ERROR, Type.INT, Operator.PLUS)


def test_python_type_to_enum():
    assert python_type_to_enum(int) == Type.INT
    assert python_type_to_enum(float) == Type.FLOAT
    assert python_type_to_enum(bool) == Type.BOOL
    assert python_type_to_enum(str) == Type.ID
    with pytest.raises(Exception):
        python_type_to_enum(list)


def test_baby_duck_type_to_enum():
    assert baby_duck_type_to_enum("int") == Type.INT
    assert baby_duck_type_to_enum("float") == Type.FLOAT
    assert baby_duck_type_to_enum("bool") == Type.BOOL
    assert baby_duck_type_to_enum("str") == Type.ID
    assert baby_duck_type_to_enum("error") == Type.ERROR
    with pytest.raises(Exception):
        baby_duck_type_to_enum("invalid_type")