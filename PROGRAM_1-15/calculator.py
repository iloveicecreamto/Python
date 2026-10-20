#  program to create  & import a calcultor module name 'calc.py'
''' NOTE
  --> create a file calc.py then  import it here
  --> run this prgm 
'''

import calc

while(1):
  print("Menu\n+ : Addition\n- : substraction\n* : multiplication\n/ : division\n0 : to exit")
  x = int(input("Enter value 1st value: "))
  y = int(input("Enter value 2nd value: "))
  choice = input("Enter your choice: ")
  match choice:
    case '+':
      print(f'addition of {x} + {y} = ' ,calc.addition(x,y))
    case '-':
      print(f'Subtraction of {x} - {y} = ' ,calc.subtraction(x,y))
    case '*':
      print(f'Product of {x} * {y} =' ,calc.multiplication(x,y))
    case '/': 
      print(f'Division of {x} / {y} =' ,calc.division(x,y))
    case '0':
      break
    case _:
      print("Invalid Expression...")
      
  print("-----------------------")
