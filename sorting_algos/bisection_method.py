def square_root_bisection(square_target, tolerance=1e-7, maximum_iterations=100):

    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target

    lower = 0
    upper = square_target if square_target >= 1 else 1

    iterations = 0

    while iterations < maximum_iterations:
        midpoint = (lower + upper) / 2
        square_mid = midpoint * midpoint

        if upper - lower <= tolerance:
            midpoint = (lower + upper) / 2
            print(f"The square root of {square_target} is approximately {midpoint}")
            return midpoint

        if square_mid < square_target:
            lower = midpoint
        else:
            upper = midpoint

        iterations += 1

    print(f"Failed to converge within {maximum_iterations} iterations")
    return None
