""" kata id: https://www.codewars.com/kata/55c6126177c9441a570000cc"""


def order_weight(weight: str) -> str:
    return ' '.join(sorted(sorted(weight.split(), key=str), key=lambda w: sum(map(int, w))))
