def merge_sort(word):
    if len(word) < 2:
        return word

    mid = int(len(word) / 2)

    first_half = merge_sort(word[:mid])
    second_half = merge_sort(word[mid:])

    i, j = 0, 0
    result = []

    while i < len(first_half) and j < len(second_half):
        if first_half[i] > second_half[j]:
            result.append(second_half[j])
            j += 1
        else:
            result.append(first_half[i])
            i += 1
    result += first_half[i:]
    result += second_half[j:]
    return "".join(result)


def is_anagram(first_string, second_string):
    if len(first_string) == 0 and len(second_string) == 0:
        return (first_string, second_string, False)

    sorted_first = merge_sort(first_string.lower())
    sorted_second = merge_sort(second_string.lower())

    anagram = sorted_first == sorted_second

    return (sorted_first, sorted_second, anagram)
