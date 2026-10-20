#   Prgm to create to menu to  - perfrom addition,sub,multiplication,division.

def addition(a,b):
  return a + b


def subtraction(a,b):
  return a - b


def multiplication(a,b):
  return a * b


def division(a,b):
  try:
    return a / b
  except ZeroDivisionError as e:
    print("!!!! Error: ",e )




while(1):
  print("Menu\n+ : Addition\n- : substraction\n* : multiplication\n/ : division\n0 : to exit")
  x = int(input("Enter value 1st value: "))
  y = int(input("Enter value 2nd value: "))
  choice = input("Enter your choice: ")
  match choice:
    case '+':
      print(f'addition of {x} + {y} = ' ,addition(x,y))
    case '-':
      print(f'Subtraction of {x} - {y} = ' ,subtraction(x,y))
    case '*':
      print(f'Product of {x} * {y} =' ,multiplication(x,y))
    case '/': 
      print(f'Division of {x} / {y} =' ,division(x,y))
    case '0':
      break
    case _:
      print("Invalid Expression...")
      
  print("-----------------------")
