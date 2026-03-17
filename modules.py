import os
import math

# Directorio actual
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

# Entrada usuario
num = int(input("Enter an integer: "))

# Log base 2
log_val = math.log2(num)
print(f"Log base 2 of {num} is: {log_val}")

# Floor y Ceiling
print(f"Floor: {math.floor(log_val)}")
print(f"Ceiling: {math.ceil(log_val)}")