def hanoi_solver(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    a = list(range(n, 0, -1))
    b = []
    c = []

    states = [f"{a} {b} {c}"]

    def record():
        states.append(f"{a} {b} {c}")

    def move(k, src, aux, dst):
        if k == 1:
            dst.append(src.pop())
            record()
            return
        move(k - 1, src, dst, aux)
        dst.append(src.pop())
        record()
        move(k - 1, aux, src, dst)

    move(n, a, b, c)
    return "\n".join(states)
