#  Copyright © 2021 NeuroByte Tech. All rights reserved.
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: qbPinGenerator
#  File Name: main.py
#  Last Modified: 20/01/2021, 21:12

from condition import *
from customer import Customer
from gen import Generator

c = Customer("13659275", "23-05-33", ["1948", "4729", "6758", "3648"])

gen = Generator()
gen.add_cond(MoreThan2Consec())
gen.add_cond(ConsecSeq())
print(gen.gen(c))
