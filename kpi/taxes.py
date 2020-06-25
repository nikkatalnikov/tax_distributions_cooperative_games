from typing import List


def proportional_tax(B: List[float], C: float) -> List[float]:
    taxes = []
    for i, b in enumerate(B):
        taxes.append(C / sum(B) * b)

    return taxes


def poll_tax(B: List[float], C: float) -> List[float]:
    taxes = []
    n = len(B)

    for i, b in enumerate(B):
        x = min((C - sum(taxes)) / (n - i), b)
        taxes.append(x)

    return taxes


def level_tax(B: List[float], C: float) -> List[float]:
    taxes = []
    n = len(B)

    for i, b in enumerate(B):
        x = b - min((sum(B[i:]) + sum(taxes) - C) / (n - i), b)
        taxes.append(x)

    return taxes


def n_core(B: List[float], C: float) -> List[float]:
    taxes = []
    n = len(B)

    if C < sum(B) / 2:
        for i, b in enumerate(B):
            x = min((C - sum(taxes)) / (n - i), b / 2)
            taxes.append(x)
    else:
        for i, b in enumerate(B):
            x = b - min((sum(B[i:]) + sum(taxes) - C) / (n - i), b / 2)
            taxes.append(x)

    return taxes

