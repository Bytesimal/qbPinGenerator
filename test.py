#  Copyright © 2021 NeuroByte Tech. All rights reserved.
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: qbPinGenerator
#  File Name: test.py
#  Last Modified: 20/01/2021, 21:18

from condition import *

consec_seq = ConsecSeq().filter(["1388", "2434", "2345", "1123", "6789"])
if "2345" in consec_seq or "6789" in consec_seq:
    print(f"ConsecSeq().filter() missed consecutive sequence, producing {consec_seq}")

consec_seq = MoreThan2Consec().filter(["1133", "2226", "6227", "4888", "9879"])
if "2226" in consec_seq or "4888" in consec_seq:
    print(f"MoreThan2Consec().filter() missed consecutive sequence, producing {consec_seq}")
