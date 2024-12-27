'''
Author: Jared Harrington
KUID: 2993675
Project: EECS 510 Final Project
'''

from pda import PDA

def main():
    pda = PDA()
    test_expression = "(7-1)-(2+(1+1))"
    formatted_expression = test_expression.replace(" ", "")
    result = pda.run(formatted_expression)
    print(f"The result of the expression '{test_expression}' is {result}.")


if __name__ == "__main__":
    main()
    