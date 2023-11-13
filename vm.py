from tables import *
from Quadruple import Quadruple
from SemanticCube import (
    cube,
    Operator,
    Type,
    parse_string,
    python_type_to_enum,
    get_result_type,
)
from mem_tables import MemoryTable, FunctionID, Value

Operand = Value


class VirtualMachine:
    # def parse_operator(self, operator):

    # def is_id(self, operand):
    def __init__(self, quads, memory: MemoryTable):
        self.memory = memory
        self.quads = quads
        self.pc = 0
        self.current_function_stack = [FunctionID("global", "void")]

    def get_value(self, identifier) -> Value:
        current_function = self.current_function_stack[-1]
        return self.memory[current_function][identifier].value

    def parse_operand_raw_to_value(self, operand):
        if self.is_identifier(operand):
            return self.get(operand).value
        return parse_string(operand)

    def is_identifier(self, operand) -> bool:
        return isinstance(operand, str) and operand[0] == "$"

    def execute(self, quad: Quadruple):
        if quad.operator == Operator.PLUS:
            self.add(quad)
        if quad.operator == Operator.ASSIGN:
            self.assign(quad)
        
    def run(self):
        while self.pc < len(self.quads):
            quad = self.quads[self.pc]
            self.execute(quad)
            self.pc += 1
        self.memory.print()

    def get(self, addr) -> Value:
        func = self.current_function_stack[-1]
        return self.memory[func][addr]

    def set(self, addr, value: Value):
        func = self.current_function_stack[-1]
        self.memory.set(func, addr, value)

    def get_value(self, token) -> Value:
        if self.is_identifier(token):
            return self.get(token)
        else:
            # its a constant
            parsed_token = parse_string(token)
            cte_type = python_type_to_enum(type(parsed_token))
            return Value(cte_type, parsed_token)
        
    def assign(self, quad):
        target = quad.result
        value = quad.left_operand
        self.set(target, self.get_value(value))

    def add(self, quad):
        print("Adding {}".format(quad))
        left_operand = self.get_value(quad.left_operand)
        right_operand = self.get_value(quad.right_operand)
        print("Values: {} {}".format(left_operand, right_operand))
        self.memory.print()
        result_type = get_result_type(
            left_operand.type, left_operand.type, quad.operator
        )

        result_python = left_operand.value + right_operand.value
        result_value = Value(result_type, result_python)
        self.set(quad.result, result_value)
        
