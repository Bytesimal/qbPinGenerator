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