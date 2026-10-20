#  Check whether a given number is between a range 


num = int(input("Enter a number: ")) 
lower = int(input("Enter lower limit: ")) 
upper = int(input("Enter upper limit: ")) 
if lower <= num <= upper: 
  print("The number is within the range.") 
else: 
  print("The number is outside the range.") 