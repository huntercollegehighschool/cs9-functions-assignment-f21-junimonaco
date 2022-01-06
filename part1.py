'''
******
PART 1
******
The function distinct() below takes three numbers as arguments, and returns True (Boolean value, not the string, so no quotes necessary) if the three numbers are all different, and False (Boolean value, not the string, so no quotes necessary) if not.

However, there are (at least) 7 errors in the code. Fix them so that it runs properly.
'''
a = int(input)("Enter a number: ")
b = int(input)("Enter a second number: ")

def distinct():
  if a != b and b!= c: #a, b, and c are the three parameters (numbers) that will be passed into the function
    return True
  elif a == b and b == c:
    return False