from dataclasses import dataclass
@dataclass
class Quadruple:
    operator: str
    left_operand: any
    right_operand: any
    result: any