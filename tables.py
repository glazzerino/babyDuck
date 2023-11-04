from dataclasses import dataclass

class VariableTable:
    def __init__(self):
        self.table = {}

    def insert(self, var_id, var_type, value=None):
        if var_id in self.table:
            raise Exception("Variable already declared")
        self.table[var_id] = {"type": var_type, "value": value}

    def get(self, var_id) -> dict:
        return self.table.get(var_id, None)

    def print(self):
        if not self.table:
            print("Empty Symbol Table")
            return

        header = "| {:<15} | {:<10} | {:<10} |".format("Variable", "Type", "Value")
        print("-" * len(header))
        print(header)
        print("-" * len(header))

        for var_id, details in self.table.items():
            row = "| {:<15} | {:<10} | {:<10} |".format(
                var_id,
                details["type"],
                str(details["value"]) if details["value"] is not None else "N/A",
            )
            print(row)
        print("-" * len(header))


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

class FunctionTable:
    def __init__(self):
        self.table = {}
        self.active_function = None

    def get(self, func_id: FunctionID) -> VariableTable:
        return self.table.get(func_id, None)

    def insert_to_top(self, var_id, var_type, value=None):
        self.table[self.active_function].insert(var_id, var_type, value)
    
    def insert_new_function(self, func_id: FunctionID):
        if func_id in self.table:
            raise Exception("Function already declared")
        self.table[func_id] = VariableTable()
        self.active_function = func_id
    
    def get_active_function_table(self) -> VariableTable:
        return self.table[self.active_function]
    
    def print_all(self):
        for func_id, var_table in self.table.items():
            print("Function: ", func_id.name, func_id.type)
            var_table.print()
            print("\n")