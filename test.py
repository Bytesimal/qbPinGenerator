from condition import *
from customer import Customer

# Inputs - change as necessary
CUSTOMER_BANK_ACCOUNT_NUMBER = "13659275"
CUSTOMER_BANK_SORT_CODE = "23-05-33"
CUSTOMER_PREVIOUS_PINS = ["1948", "4729", "6758", "3648"]

# customer and generator construction
c = Customer(CUSTOMER_BANK_ACCOUNT_NUMBER, CUSTOMER_BANK_SORT_CODE, CUSTOMER_PREVIOUS_PINS)

seq = MoreThan2Consec().filter(["1133", "2226", "6227", "4888", "9879"])
if "2226" in seq or "4888" in seq:
    print(f"MoreThan2Consec().filter() missed consecutive sequence of 2 numbers, producing {seq}")

seq = ConsecSeq().filter(["1388", "2434", "2345", "1123", "6789"])
if "2345" in seq or "6789" in seq:
    print(f"ConsecSeq().filter() missed consecutive sequence, producing {seq}")

seq = PrevPins(3).filter(["1133", "2226", "4729", "4888", "6758"], c)
if "4729" in seq or "6758" in seq:
    print(f"PrevPins().filter() missed previous pins, producing {seq}")

seq = InAccNum().filter(["6592", "2226", "6227", "9275", "9879"])
if "6592" in seq or "9275" in seq:
    print(f"InAccNum().filter() missed pins in account number, producing {seq}")

seq = InSortCode().filter(["1133", "2226", "0533", "4888", "3053"])
if "0533" in seq or "3053" in seq:
    print(f"InSortCode().filter() missed pins in sort code, producing {seq}")
