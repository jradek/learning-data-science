from typing import List

Vector = List[float]


def dot(v: Vector, w: Vector) -> float:
    assert len(v) == len(w)
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v: Vector) -> float:
    return dot(v, v)

print(sum_of_squares([1, 2, 3]))

