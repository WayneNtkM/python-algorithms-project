def study_schedule(permanence_period, target_time):
    c = 0

    if target_time is None:
        return None

    if not all(isinstance(a, int) and isinstance(b, int)
               for a, b in permanence_period):
        return None

    for a, b in permanence_period:
        if a <= target_time <= b:
            c += 1
    return c
