from tables import *
from Quadruple import Quadruple
from SemanticCube import cube, get_type, parse_operator, Operator, Type
from mem_tables import MemoryTable, FunctionID, Variable
# Returns the result type of an operation between two operands.
def get_result_type(left, right, operator: Operator):
        left_type = get_type(left)
        right_type = get_type(right)
        return cube[left_type.value][right_type.value][operator.value]

def check_result_type(type: Type, left, right, operator):
     if type == Type.ERROR:
         raise Exception("Invalid operation. Cannot perform {} {} {}".format(left, operator, right))

class VirtualMachine:
    def __init__(self, quads: list, memory: MemoryTable):
        self.pc = 0
        self.quads = quads
        self.mem = memory
        self.current_function_stack = [FunctionID("global", "void")]

    def mem_set(self, operand, value: (Type, any)):
        if type(operand) in [int, float]:
            return operand
        # if operand is not parsed by now then it is an address
        address = operand
        current_function_id = self.current_function_stack[-1]
        self.mem.set(current_function_id, (address, value))

    def mem_get(self, value_id):
        current_function_id = self.current_function_stack[-1]
        return self.mem[current_function_id][value_id]
    
    def assign(self, quad: Quadruple):
        value = self.mem_get(quad.left_operand)
        self.mem_set(quad.result, value)

    def execute(self, quad: Quadruple):
        print("Executing: {}".format(quad))
        if quad.operator == "+":
            self.add(quad)
        elif quad.operator == "-":
            self.substract(quad)
        elif quad.operator == "=":
            self.assign(quad)
    
    def add(self, quad: Quadruple):
        left = self.mem_get(quad.left_operand)
        right = self.mem_get(quad.right_operand)
        result_type = get_result_type(left, right, Operator.PLUS)
        check_result_type(result_type, left, right, Operator.PLUS)
        result = left + right
        self.mem_set(quad.result, (result_type, result))
        print("Adding {} + {} = {}".format(left, right, result))
    
    def run(self):
        while self.pc < len(self.quads):
            quad = self.quads[self.pc]
            self.execute(quad)
            self.pc += 1


