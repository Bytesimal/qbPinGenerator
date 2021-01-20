import random as rd

from condition import Condition
from customer import Customer

digits = [str(n) for n in range(10)]


class Generator:
    def __init__(self):
        self.conditions = []

    def add_cond(self, cond: Condition):
        self.conditions.append(cond)

    def gen(self, customer: Customer) -> str:
        # generate all combos
        combos = []
        for dig0 in digits:
            for dig1 in digits:
                for dig2 in digits:
                    for dig3 in digits:
                        combos.append(dig0 + dig1 + dig2 + dig3)

        # filter for each condition
        for c in self.conditions:
            combos = c.filter(combos, customer)

        return combos[rd.randint(0, len(combos))]  # return random pin
