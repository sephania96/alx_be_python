def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            return ZeroDivisionError
        else:
            return f"The result of the division is {numerator / denominator}".strip()
    except ValueError:
        return "Please ENter numeric values only"

