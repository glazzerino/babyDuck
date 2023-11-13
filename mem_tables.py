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
class Value:
    type: Type
    value: any
    
class MemoryTable:
    def __init__(self):
        self.table = {}
    
    def set(self, function_id: FunctionID, address: str, value: Value):
        self.table[function_id][address] = value
    
    def __getitem__(self, function_id: FunctionID):
        return self.table[function_id]
    
    def __setitem__(self, function_id: FunctionID, variables: dict):
        self.table[function_id] = variables
    
    def print(self):
        print("Memory Table")
        print(self.table)
        print()
    
    def print(self):
        if not self.table:
            print("Empty Memory Table")
            return

        header = "| {:<15} | {:<10} | {:<10} |".format("Value", "Type", "Value")
        print("-" * len(header))
        print(header)
        print("-" * len(header))

        for function_id, variables in self.table.items():
            print(f"Function: {function_id.name}, Type: {function_id.type}")
            for var_id, details in variables.items():
                row = "| {:<15} | {:<10} | {:<10} |".format(
                    var_id,
                    details.type.name.lower(),
                    str(details.value) if details.value is not None else "N/A",
                )
                print(row)
            print("-" * len(header))
