def function_with_uncommon_error_solution(a, b):
    try:
        if a == 0:
            return 1 / a
        else:
            return a + b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None  #Return None or another appropriate value

result = function_with_uncommon_error_solution(0,5)
print(result) 