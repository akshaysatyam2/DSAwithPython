"""
Pattern: Right Triangle number Pattern
1 
1 2 
1 2 3
1 2 3 4
1 2 3 4 5
"""

for i in range(5):  # Number of rows
    for j in range(i + 1):  # Number of columns (increasing with each row)
        print(j+1, end=" ")
    print()  # New line after each row