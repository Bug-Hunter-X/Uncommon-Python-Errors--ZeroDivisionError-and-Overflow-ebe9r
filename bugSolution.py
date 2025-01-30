def function_with_uncommon_error_handled(x):
    try:
        if abs(x) < 1e-9: # Check for very small numbers to prevent overflow
            return float('inf') if x > 0 else float('-inf')
        return 10 / x
    except ZeroDivisionError:
        return float('inf')

result = function_with_uncommon_error_handled(0)
print(result) # Output: inf
result2 = function_with_uncommon_error_handled(1e-10) #testing potential overflow
print(result2) # Output: inf