
# Define a function that helps to calculate the area of circle with different radius and print the area only when the area is divisible by 4
# 23.48, 56.78, 45.67, 78.28

# calculate the area of circle with different radius
# PI = 3.14

def calculate_area_of_circle(radius):
  area_of_circle = 3.14 * radius * radius
  is_area_of_circle = area_of_circle % 4 == 0 #true/false
  print(is_area_of_circle)

  if is_area_of_circle == True:
    print('The area of circle is ' + str(area_of_circle))
		
    
  #is_area_of_circle = area_of_circle % 4 == 0 #true/false
  
  #	area_of_circle
  
  	

calculate_area_of_circle(23.48)
calculate_area_of_circle(56.78)
calculate_area_of_circle(45.67)
calculate_area_of_circle(78.28)


print("------------------------------------------------------------------------------------------------------------")

# Define a function using Python that helps to find the first five character of string in all the possible ways



#name = 'PRASHANT'
def first_five_char(name):
  print(name[0:5])   
  print(name[:5])
  print(name[-8:-3])

first_five_char('PRASHANT')




print("------------------------------------------------------------------------------------------------------------")

# Define a function using Python that helps to find the last 3 character of string in all the possible ways

def last_3_char(string):
  
  print(string[-3:])
  print(string[5:8])
  print(string[5:])
  
  

last_3_char('PRASHANT')

print("------------------------------------------------------------------------------------------------------------")


