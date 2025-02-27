import random
def get_numbers_ticket(min, max, quantity):
    empty_set = set()
    if 1 <= min < max <= 1000 and max - min > quantity:
        while len(empty_set) < quantity:
            empty_set.add(random.randrange(min, max))
        result = list(empty_set)
        result.sort()
        return result
    else:
        return list(empty_set)