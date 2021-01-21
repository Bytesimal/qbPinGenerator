# QuantBet "QuantBank" Challenge

### Challenge Description

QuantBet is opening a new bank called QuantBank and require you to write a piece of software to generate new PINs for
customer cards. When generating a PIN, you will be provided with the customer's personal details (eg name, date of
birth), and the details of the bank account (eg sort code, account number). The generated PIN must satisfy the following
rules:

- It should be 4 digits long
- It must not contain more than two consecutive numbers (eg 1112, 1111 are not allowed; 1211 is allowed)
- It must not contain a complete consecutive number sequence (eg 1234, 3456 are not allowed)
- It is distinct from the user's past three PINs (you may assume that a sufficient history is provided alongside the
  bank account details)
- It cannot be contained in the user's bank account number or sort code (eg for an account with sort code 71-13-13 and
  account number 13561342, the PINs 1356, 1342 and 7113 are all not allowed)

### Installation

- This solution has been developed and tested on `Python 3.8.5`. However, it should be compatible with all Python 3
  installations
- To run the main script, use `python main.py` after altering the parameters in the file to suit your needs.
- To run tests on the code, use `python test.py`.

### Design

- `main.py` - contains the runnable script
- `test.py` - contains the tests that can be performed to check for bugs
- `gen.py` - contains the configuration for the `Generator` class
- `condition.py` - contains the definition of `Condition` interface as well as classes which satisfy it. More
  definitions for custom conditions can be added to this file.
- `customer.py` - defines the basic `Customer` construct which contains information which may be used in conditions.

This project has been designed with modularity and usability in mind in order to simplify the addition of new
`Condition` classes.

The generator has been designed so that valid lists of pins "cascade" through the layers of conditions. It is the
blueprint by which any numbers of conditions can be used since all conditions must satisfy the
`Condition` interface - thus ensuring they have the correct methods.

This ensures that there is sufficient modularity that different conditions can be used at different times, without
affecting the rest of the code. This means that any security auditing only has to be done on the added code of the
condition rather than checking the whole application. After a condition has been designed and implemented, one
only has to add it to the generator using the `add_cond()` method, and the run code for the generator can remain
unchanged.

For example, if I wanted to add a condition which ensures that the pin cannot start with a "0", all I would have to do
is define the code for the condition as a class which implements the `Condition` interface and add it to
`condition.py`, like this:

```python
# condition.py

class First0Digit(Condition):
    def filter(self, pins, *args) -> list:
        satisfied = []

        for p in pins:
            if p[0] != "0":
                satisfied.append(p)
        return satisfied
```

Then I would go to `main.py` and add a constructed condition to the generator with
```python
gen.add_cond(First0Digit())
```
in the section which is clearly labeled as the place to add this code.

There! That was easy!
