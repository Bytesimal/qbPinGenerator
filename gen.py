#  Copyright © 2021 NeuroByte Tech. All rights reserved.
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: qbPinGenerator
#  File Name: gen.py
#  Last Modified: 20/01/2021, 17:38

import numpy as np

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

        # remove
        combos = [p for p in combos if
                  p not in customer.past_pins[-3:] and  # previous customer pins
                  p not in customer.acc and  # account number
                  p not in customer.sort.replace("-", "")]  # sort code

        return combos[np.random.randint(0, len(combos))]  # return random pin
