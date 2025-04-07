"""
Pattern: Upside-down Right Triangle number Pattern
1 2 3 4 5 
1 2 3 4 
1 2 3
1 2
1
"""

for i in range(5):  # Number of rows
    for j in range(5-i):  # Number of columns (decreasing with each row)
        print(j+1, end=" ")
    print()  # New line after each row