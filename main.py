#  Copyright © 2021 NeuroByte Tech. All rights reserved.
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: qbPinGenerator
#  File Name: main.py
#  Last Modified: 20/01/2021, 21:28
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: qbPinGenerator
#  File Name: main.py
#  Last Modified: 20/01/2021, 21:12

from condition import *
from customer import Customer
from gen import Generator

CUSTOMER_BANK_ACCOUNT_NUMBER = "13659275"
CUSTOMER_BANK_SORT_CODE = "23-05-33"
CUSTOMER_PREVIOUS_PINS = ["1948", "4729", "6758", "3648"]

c = Customer(CUSTOMER_BANK_ACCOUNT_NUMBER, CUSTOMER_BANK_SORT_CODE, CUSTOMER_PREVIOUS_PINS)

gen = Generator()
gen.add_cond(MoreThan2Consec())
gen.add_cond(ConsecSeq())
print(gen.gen(c))
