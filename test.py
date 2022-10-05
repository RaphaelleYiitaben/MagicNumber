MAGIC_NUMBER = 11
ans = 0

while ans not in (range(1, 10)) or ans != MAGIC_NUMBER:
    try:
        print("enter an integer between 1 and 20")
        ans = int(input())

        if ans < MAGIC_NUMBER:
            print(f"the number {ans} is smaller than our Magic Number")
        elif ans > MAGIC_NUMBER:
            print(f"the number {ans} is greater than our Magic Number")

    except:
        print("verify your number")

print('''\nWOW
O O
---
\n\nCONGRATULATIONS''')
