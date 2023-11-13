class ValueParser:

    def parse_value(self, value):
        if value is None:
            return None
        """Attempts to parse the value into int, float, or bool."""
        parsers = [self.parse_int, self.parse_float, self.parse_bool]

        for parser in parsers:
            result = parser(value)
            if result is not None:
                return result

        return value

    def parse_int(self, value):
        """Attempts to parse the value as an integer."""
        try:
            return int(value)
        except ValueError:
            return None

    def parse_float(self, value):
        """Attempts to parse the value as a float."""
        try:
            return float(value)
        except ValueError:
            return None

    def parse_bool(self, value):
        """Attempts to parse the value as a boolean."""
        # Custom logic for boolean, as 'bool' in Python will return True for any non-zero number
        value_str = value.lower() if isinstance(value, str) else str(value).lower()
        if value_str in ["true", "false"]:
            return value_str == "true"
        return None