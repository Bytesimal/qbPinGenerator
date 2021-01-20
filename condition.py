# interface for conditions
class Condition:
    def filter(self, pins, *args) -> list:
        return []


class Cond2Consec(Condition):
    def filter(self, pins, *args) -> list:
        satisfied = []

        for p in pins:
            valid = True

            for i, c in enumerate(p[:-2]):
                if c == p[i + 1] == p[i + 2]:
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
