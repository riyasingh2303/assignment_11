# Get the number from the user
num = input("Enter a number: ")
 
# Initialize a variable to store the sum of digits
sum = 0
 
# Iterate over each digit in the number
for n in num:
  # Add the current digit to the sum
  sum += int(n)
 
# Print the sum of digits
print(sum)