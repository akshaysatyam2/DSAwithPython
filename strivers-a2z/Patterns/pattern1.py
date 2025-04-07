"""
Pattern 1: Square Star Pattern
* * * * *   
* * * * *
* * * * *
* * * * *
* * * * *
"""

for i in range(5):  # Number of rows
    for j in range(5):  # Number of columns
        print("*", end=" ")
    print()  # New line after each row
    