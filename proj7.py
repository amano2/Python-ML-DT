n = int(input("Enter the value of n: "))

total = 0
for i in range(1, n+1):
    term = i
    if i == 4:
        term = 10
    elif i > 4:
        term = 2 * term + 6
    total += term

print("Total sum of the series for first", n, "terms is:", total)

# Calculate the 99th term
term_99 = 99
if term_99 > 4:
    term_99 = 2 * term_99 + 6

print("99th term of the series is:", term_99)
