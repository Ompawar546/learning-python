num = int(input("Enter a number: "))
original_num = num
sum = 0

# Count number of digits
digits = 0
temp = num
while temp > 0:
    digits += 1
    temp //= 10

# Calculate the Armstrong sum
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

# Check if Armstrong
if sum == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")

