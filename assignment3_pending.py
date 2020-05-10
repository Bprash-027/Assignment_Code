# Design a function that accept 6 values & find the average of those values which are only divisible by 6.

def Average(n1,n2,n3,n4,n5,n6):
  sum = 0
  count = 0
  
  if n1 % 6 == 0:
    sum = sum + n1
    count = count + 1
  if n2 % 6 == 0:
    sum = sum + n2
    count = count + 1
  if n3 % 6 == 0:
    sum = sum + n3
    count = count + 1
  if n4 % 6 == 0:
    sum = sum + n4
    count = count + 1
  if n5 % 6 == 0:
    sum = sum + n5
    count = count + 1
  if n6 % 6 == 0:
    sum = sum + n6
    count = count + 1
    
  Average = sum / count
  print(Average)
  

Average(36,55,24,25,60,54)


print("------------------------------------------------------------------------------------------------------------")


# Define a function that helps to find the square of any number and then add the same number to the squared number only when the number is odd and return the final output.

def calculate_square_add(n):
  if n % 2 != 0:
    square = n * n
    result = square + n
    print(result)

calculate_square_add(3)
calculate_square_add(4)

print("------------------------------------------------------------------------------------------------------------")


# Define a function that helps to print all the numbers between 5 and 50 with interval of 5 for ex. 5, 10, 15 and so on...

# Solve using both types of loop. Make sure to design different function for each loop

print("Using for loop==========")
for num in range(5,51,5):
  print(num)

print("Using while loop==========")
num = 5
while num < 51:
  print(num)
  num = num + 5

print("------------------------------------------------------------------------------------------------------------")


