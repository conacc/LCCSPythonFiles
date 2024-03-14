# calculatePi.py
# @coneill 14/03/2024

# Initialize number of terms
num = 10000

# Initialize denominator
k = 1
 
# Initialize sum
s = 0
 
for i in range(num):
 
    # even index elements are positive
    if i % 2 == 0:
        s += 4/k
    else:
        # odd index elements are negative
        s -= 4/k
 
    # denominator is odd
    k += 2
     
print(s)
