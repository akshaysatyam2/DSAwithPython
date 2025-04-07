"""
Pattern: Upside-down Right Triangle Star Pattern
* * * * * 
* * * * 
* * *
* *
*
"""

for i in range(5):  # Number of rows
    for j in range(5-i):  # Number of columns (decreasing with each row)
        print("*", end=" ")
    print()  # New line after each row