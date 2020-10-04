class Calculator:
    def __init__(self, init_value=0, attribute_limit=10):
        self.__dict__['attribute_limit'] = attribute_limit
        self.__dict__['value'] = init_value

    def __add__(self, *others):
        value = self.value
        for other in others:
            value += other.value if isinstance(other, Calculator) else other
        return Calculator(value)

    def __sub__(self, *others):
        value = self.value
        for other in others:
            value -= other.value if isinstance(other, Calculator) else other
        return Calculator(value)

    def __neg__(self):
        return Calculator(-self.value)

    def __mul__(self, *others):
        value = self.value
        for other in others:
            value *= other.value if isinstance(other, Calculator) else other
        return Calculator(value)

    def __pow__(self, *others):
        value = self.value
        for other in others:
            value **= other.value if isinstance(other, Calculator) else other
        return Calculator(value)

    def __floordiv__(self, *others):
        value = self.value
        for other in others:
            value //= other.value if isinstance(other, Calculator) else other
        return Calculator(value)

    def __truediv__(self, *others):
        value = self.value
        for other in others:
            value /= other.value if isinstance(other, Calculator) else other
        return Calculator(value)

    def __setattr__(self, name, value):
        if len(self.__dict__) >= self.attribute_limit:
            raise AttributeError
        self.__dict__[name] = value

    def __iter__(self):
        return self.value

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.__dict__)
