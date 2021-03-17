class IntegerSequence():
    value = 0   # class variable

    @classmethod
    def init_value(cls, value):
        cls.value = value

    @classmethod
    def next_value(cls):
        cls.value += 1
        return cls.value
       

# Verify implementations

IntegerSequence.init_value(0)

assert 1 == IntegerSequence.next_value()
assert 2 == IntegerSequence.next_value()
assert 3 == IntegerSequence.next_value()