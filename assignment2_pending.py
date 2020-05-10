# Fn to accept 4 values and get the avg. of them
print("------------------------------------------------------------------------------------------------------------")
def sum_of_nos(a,b,c,d):
  x = a,b,c,d
  sum_of_nos = a + b + c + d
  return sum_of_nos
print("Numbers are 10,20,30,40")
print("Sum of 4 nos is ", sum_of_nos(10,20,30,40))

def Average_of_sum():
  Sum=sum_of_nos(10,20,30,40)
  Average = Sum/4
  return Average
print("Average of 4 nos is ", Average_of_sum())

print("------------------------------------------------------------------------------------------------------------")

# Define a function that helps to find the square of any number and then add the same number to the squared number and return the final output.
def calculate_square_add(n):
  square = n * n
  result = square + n
  return result

output = calculate_square_add(4)
print("The value after square and addition is " + str(output))
output = calculate_square_add(8)
print("The value after square and addition is " + str(output))

print("------------------------------------------------------------------------------------------------------------")

