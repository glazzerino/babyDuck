from Quadruple import Quadruple
from SemanticCube import (
    Operator,
    Type,
    parse_string,
    python_type_to_enum,
    get_result_type,
    rules,
)
from mem_tables import MemoryTable, FunctionID, Value

Operand = Value


class VirtualMachine:
    def __init__(self, quads, memory: MemoryTable):
        print("Initializing Virtual Machine")
        for quad in quads:
            print(quad)
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

    def run(self):
        while self.pc < len(self.quads):
            quad = self.quads[self.pc]
            self.execute(quad)
            self.pc += 1

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

    def execute(self, quad: Quadruple):
        if quad.operator == Operator.PLUS:
            self.add(quad)
        if quad.operator == Operator.ASSIGN:
            self.assign(quad)
        if quad.operator == Operator.PRINT:
            self.print(quad)
        if quad.operator == Operator.PRINT_NEWLINE:
            self.print_newline(quad)
        if quad.operator == Operator.MINUS:
            self.substract(quad)
        if quad.operator == Operator.TIMES:
            self.multiply(quad)
        if quad.operator == Operator.DIVIDE:
            self.divide(quad)
        if quad.operator == Operator.LESS_THAN:
            self.less_than(quad)
        if quad.operator == Operator.GREATER_THAN:
            self.greater_than(quad)
        if quad.operator == Operator.GOTOT:
            self.gotot(quad)
        if quad.operator == Operator.GOTOF:
            self.gotof(quad)
        if quad.operator == Operator.GOTO:
            self.goto(quad)
        if quad.operator == Operator.EQUAL:
            self.equals(quad)

    def greater_than(self, quad: Quadruple):
        return self.calculate(quad, "greater_than")

    def goto(self, quad: Quadruple):
        self.pc = quad.result + 1

    def gotof(self, quad: Quadruple):
        if not self.get_value(quad.left_operand).value:
            self.pc = quad.result

    def equals(self, quad):
        self.calculate(quad, "equals")

    def gotot(self, quad):
        if self.get_value(quad.left_operand).value:
            self.pc = quad.result

    def less_than(self, quad):
        return self.calculate(quad, "less_than")

    def print(self, quad):
        print("🦆" + str(self.get_value(quad.left_operand).value), end="")

    def print_newline(self, quad):
        print()

    def assign(self, quad):
        target = quad.result
        value = quad.left_operand
        self.set(target, self.get_value(value))

    def divide(self, quad):
        left_operand = self.get_value(quad.left_operand)
        right_operand = self.get_value(quad.right_operand)
        result_type = get_result_type(
            left_operand.type, left_operand.type, quad.operator
        )

        result_python = left_operand.value / right_operand.value
        result_value = Value(result_type, result_python)
        self.set(quad.result, result_value)

    def calculate(self, quad, operation):
        left_operand = self.get_value(quad.left_operand)
        right_operand = self.get_value(quad.right_operand)
        result_type = get_result_type(
            left_operand.type, left_operand.type, quad.operator
        )
        if result_type == Type.ERROR:
            raise Exception("Invalid operation")
        if operation == "add":
            result_python = left_operand.value + right_operand.value
        elif operation == "multiply":
            result_python = left_operand.value * right_operand.value
        elif operation == "divide":
            result_python = left_operand.value / right_operand.value
        elif operation == "substract":
            result_python = left_operand.value - right_operand.value
        elif operation == "greater_than":
            result_python = left_operand.value > right_operand.value
        elif operation == "less_than":
            result_python = left_operand.value < right_operand.value
        elif operation == "equals":
            result_python = left_operand.value == right_operand.value

        result_value = Value(result_type, result_python)
        self.set(quad.result, result_value)

    def add(self, quad):
        self.calculate(quad, "add")

    def multiply(self, quad):
        self.calculate(quad, "multiply")

    def divide(self, quad):
        self.calculate(quad, "divide")

    def multiply(self, quad):
        self.calculate(quad, "multiply")

    def substract(self, quad):
        if quad.left_operand is None:
            # unary minus
            quad.left_operand = 0
        self.calculate(quad, "substract")
