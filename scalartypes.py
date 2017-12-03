# Python scalar types and values

# Int for whole numbers

number = 10  # Decimal
binary = 0b10  # Binary
octo = 0o10  # Octo
hexadecimal = 0x10  # Hexadecimal

# Using the int constructor

integer = int(3.5)
toward_zero = int(-3.5)  # Rounding is towards zero
convert = int("496")  # Conversion of strings to integers
print(integer, toward_zero, convert)

number_base = int("10000", 3)  # Number base when converting from a string
print(number_base)

# Floats for numbers with fractional parts
example_float = 3.25  # Numbers with decimals
speed_light = 3e8  # Use of scientific notations large number
planks_constant = 1.616e-35  # Use in scientific notations small numbers
print(example_float, speed_light)

# Convertion of integers to floats

example_integer = float(7)  # From an integer
fro_string = float("1.2345")  # From a string
not_number = float("nan")  # Special floating point Nan
po_infinity = float("inf")  # Positive infinity
neg_infinity = float("-inf")  # Negative infinity

print(example_float, fro_string, not_number, po_infinity, neg_infinity)

# None an important placeholder value (absence of a value)

test_none = None
test_none = test_none is None  # Test if python is None
print(test_none, test_none)

# Bool used for True and False values

bool_true = True
bool_false = False
print(bool_true, bool_false)

# Bool constructor converts other types to bool same to negatives and floats

falsy = bool(0)
truthy = bool(47)
print(falsy, truthy)

empty_list = bool([])  # Only empty list is False
my_list = bool([1, 3, 5, 6])  # List not Empty
empty_string = bool("")  # Empty String
my_string = bool("something new")

print(empty_list, my_list, my_string, empty_string)
