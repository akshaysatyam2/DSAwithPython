"""
Pattern: Right Triangle Star Pattern
*
* *
* * *
* * * *
* * * * *
"""

for i in range(5):  # Number of rows
    for j in range(i + 1):  # Number of columns (increasing with each row)
        print("*", end=" ")
    print()  # New line after each row