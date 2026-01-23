def number_pattern(n):
    #validate
    if not isinstance(n, int):
        return "Argument must be an integer value."

    #validates input
    if n < 1:
        return "Argument must be an integer greater than 0."

    #help empty list
    result = []

    for i in range(1, n + 1):
        result.append(str(i))

    return " ".join(result)





