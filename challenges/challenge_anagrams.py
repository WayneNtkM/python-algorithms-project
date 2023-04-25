def merge_sort(word):
    if len(word) < 2:
        return word
    result = []
    mid = int(len(word) / 2)
    y = merge_sort(word[:mid])
    z = merge_sort(word[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return "".join(result)


def is_anagram(first_string, second_string):
    if len(first_string) == 0 and len(second_string) == 0:
        return (first_string, second_string, False)

    sorted_first = merge_sort(first_string.lower())
    sorted_second = merge_sort(second_string.lower())

    anagram = sorted_first == sorted_second

    return (sorted_first, sorted_second, anagram)
