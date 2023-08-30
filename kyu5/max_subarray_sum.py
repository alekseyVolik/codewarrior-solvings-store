"""
Algorithm: Maximum subarray problem:
https://www.youtube.com/watch?v=5WZl3MMT0Eg
kata id: https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c

"""


def max_sequence(arr: list) -> int:
    max_sum, current_sum = 0, 0
    for num in arr:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum
