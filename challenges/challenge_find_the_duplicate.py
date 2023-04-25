from collections import Counter


def find_duplicate(nums):
    if len(nums) < 2:
        return False

    if not all(isinstance(n, int) for n in nums):
        return False

    if any(n < 0 for n in nums):
        return False

    counter = Counter(nums)

    if all(d == 1 for d in counter.values()):
        return False

    return counter.most_common(1)[0][0]
