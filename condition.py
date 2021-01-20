#  Copyright © 2021 NeuroByte Tech. All rights reserved.
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: qbPinGenerator
#  File Name: condition.py
#  Last Modified: 20/01/2021, 22:00
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: qbPinGenerator
#  File Name: condition.py
#  Last Modified: 20/01/2021, 21:54
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: qbPinGenerator
#  File Name: condition.py
#  Last Modified: 20/01/2021, 21:18


class Condition:
    """interface for conditions"""

    def filter(self, pins, *args) -> list:
        """
        :param pins is a list of 4-digit strings of pins
        :return list of pins from the parameters which satisfy the defined condition
        """
        return pins


class MoreThan2Consec(Condition):
    def filter(self, pins, *args) -> list:
        satisfied = []

        for p in pins:
            valid = True

            for j, c in enumerate(p[:-2]):
                if c == p[j + 1] == p[j + 2]:
                    valid = False
                    break

            if valid:
                satisfied.append(p)

        return satisfied


digits = [str(n) for n in range(10)]
consec_seqs = []
for i in range(len(digits) - 3):
    consec_seqs.append("".join(digits[i: i + 4]))


class ConsecSeq(Condition):
    def filter(self, pins, *args) -> list:
        satisfied = []
        for p in pins:
            if p not in consec_seqs:
                satisfied.append(p)
        return satisfied


class PrevPins(Condition):
    def __init__(self, depth):
        self.d = depth

    def filter(self, pins, *args) -> list:
        return [p for p in pins if p not in args[0].past_pins[-1 * self.d:]]


class InAccNum(Condition):
    def filter(self, pins, *args) -> list:
        return [p for p in pins if p not in args[0].acc]


class InSortCode(Condition):
    def filter(self, pins, *args) -> list:
        return [p for p in pins if p not in args[0].sort.replace("-", "")]
