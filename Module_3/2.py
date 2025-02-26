import random
def get_numbers_ticket(min, max, quantity):
    empty_set = set()
    if min >= 1 and max <= 1000:
        while len(empty_set) < quantity:
            empty_set.add(random.randrange(min, max))
    return list(empty_set)
