"""
Pattern: Triangle Star Pattern
        * 
      * * * 
    * * * * *
  * * * * * * *
* * * * * * * * *
This pattern creates a right triangle with stars, where the number of stars in each row increases from 1 to 5, and the stars are right-aligned.
"""

n = 5  # Number of rows
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()