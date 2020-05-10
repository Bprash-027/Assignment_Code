# Define a function which calculate the age of any individual from current date
print("------------------------------------------------------------------------------------------------------------")
def calculate_age(birth_year):
  
  current_year = 2020
  age = current_year - birth_year
  print(age)

calculate_age(1987)
calculate_age(1992)  
calculate_age(1990)  
calculate_age(1998)

print("------------------------------------------------------------------------------------------------------------")

  
# Define a function which gonna convert Temperature from celcius to fahrenheit and vice versa

def temp_to_far(celcius_temp):
  far_temp = (celcius_temp * 9/5) + 32
  print(far_temp)

temp_to_far(100)

def far_to_temp(far_temp):
  celcius_temp = (far_temp - 32) * 5/9
  print(celcius_temp)
  
far_to_temp(212)

print("------------------------------------------------------------------------------------------------------------")


# Define a function where you have to find whether the given number is odd or even

def even_or_odd(number):
  is_even = number % 2 == 0
  print(is_even)
  
  if is_even == True:
    print("Number is " + str(number) + " and it's even")
  else:
    print("Number is " + str(number) + " and it's odd")

even_or_odd(8)
even_or_odd(5)
even_or_odd(66)
even_or_odd(51)

print("------------------------------------------------------------------------------------------------------------")