# interface for conditions
class Condition:
    def filter(self, pins, *args):
        return []


class CondConsecutive(Condition):
    def filter(self, pins, *args):
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
