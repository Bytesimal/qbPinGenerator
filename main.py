from condition import *
from customer import Customer
from gen import Generator

c = Customer("13659275", "23-05-33", ["1948", "4729", "6758", "3648"])

gen = Generator()
gen.add_cond(Cond2Consec())
gen.add_cond(ConsecSeq())
print(gen.gen(c))
