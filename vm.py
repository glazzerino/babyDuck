from tables import *
from Quadruple import Quadruple
from SemanticCube import cube, Operator, Type, baby_duck_type_to_enum, parse_string_to_type, parse_string
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
            return self.memory.get()
        return parse_string(operand)

    def preprocess_quads(self, quads):
        for quad in quads:
            left = quad.left_operand
            right = quad.right_operand

    def is_identifier(self, operand) -> bool:
        return operand[0] == "$"