from condition import *
from customer import Customer
from gen import Generator

# Inputs - change as necessary
CUSTOMER_BANK_ACCOUNT_NUMBER = "13659275"
CUSTOMER_BANK_SORT_CODE = "23-05-33"
CUSTOMER_PREVIOUS_PINS = ["1948", "4729", "6758", "3648"]

# customer and generator construction
c = Customer(CUSTOMER_BANK_ACCOUNT_NUMBER, CUSTOMER_BANK_SORT_CODE, CUSTOMER_PREVIOUS_PINS)
gen = Generator()

# Add more conditions as necessary
gen.add_cond(MoreThan2Consec())
gen.add_cond(ConsecSeq())
gen.add_cond(PrevPins(depth=3))
gen.add_cond(InAccNum())
gen.add_cond(InSortCode())

# running the generator
print(gen.gen(c))
