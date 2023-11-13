from dataclasses import dataclass
from SemanticCube import Type
@dataclass(frozen=True)
class FunctionID:
    name: str
    type: str

    def __hash__(self):
        return hash((self.name, self.type))

    def __eq__(self, other):
        if not isinstance(other, FunctionID):
            return False
        return self.name == other.name and self.type == other.type

@dataclass(frozen=True)
class Variable:
    type: Type
    value: any
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
    elif baby_duck_type == "string":
        return Type.STRING
    elif baby_duck_type == "error":
        return Type.ERROR
    else:
        raise Exception("Invalid type: {}".format(baby_duck_type))

class MemoryTable:
    def __init__(self):
        self.table = {}
    
    def set(self, function_id: FunctionID, variable: Variable):
        self.table[function_id][variable] = variable
    
    def __getitem__(self, function_id: FunctionID):
        return self.table[function_id]
    
    def __setitem__(self, function_id: FunctionID, variables: dict):
        self.table[function_id] = variables
    
    def print(self):
        print("Memory Table")
        print(self.table)
        print()
    