# Python program to accept the number of days a member is late in returning a book and display the fine


days = int(input("Enter the number of late days: ")) 
if days == 0: 
  print("No fine.") 
elif days <= 5: 
  print("Fine = Rs.", days * 2)
elif days <= 10: 
  print("Fine = Rs.", days * 3) 
elif days <= 30: 
  print("Fine = Rs.", days * 5) 
else: 
  print("Membership Cancelled.") 